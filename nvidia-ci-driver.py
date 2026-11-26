#!/usr/bin/env python3
"""Run the central NVIDIA builder for one utils repo and one kernel repo.

Unlike nvidia-ci.py's repository discovery mode, this entry point is intended
for reusable GitHub Actions. It clones exactly the requested utils commit and
exactly one matching kernel-module repository/branch, then reuses the existing
inspect, EOL, build, harvest and publish implementation.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from restore_harvest_history import restore_harvest_history


SCRIPT_DIR = Path(__file__).resolve().parent
NVIDIA_CI_PATH = SCRIPT_DIR / "nvidia-ci.py"


def load_nvidia_ci():
    spec = importlib.util.spec_from_file_location("nvidia_ci_central", NVIDIA_CI_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load central builder: {NVIDIA_CI_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def validate_repository(value: str, expected_name: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        raise ValueError(f"Invalid GitHub repository: {value!r}")
    if value.split("/", 1)[1] != expected_name:
        raise ValueError(
            f"Repository must be named {expected_name!r}, received {value!r}"
        )
    return value


def validate_ref(value: str, description: str) -> str:
    if not value or value.startswith("-"):
        raise ValueError(f"Invalid {description}: {value!r}")
    checked = subprocess.run(
        ["git", "check-ref-format", f"refs/heads/{value}"],
        text=True,
        capture_output=True,
        check=False,
    )
    if checked.returncode != 0:
        raise ValueError(f"Invalid {description}: {value!r}")
    return value


def run_git(args: list[str], *, cwd: Path | None = None) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=cwd, text=True, capture_output=True, check=False
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return proc.stdout.strip()


def checkout_exact_commit(remote: str, branch: str, commit: str, target: Path) -> None:
    """Fetch a branch shallowly, then check out the exact event commit."""
    if not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise ValueError(f"Invalid source commit SHA: {commit!r}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir(parents=True, exist_ok=False)
    run_git(["init", "--quiet", str(target)])
    run_git(["remote", "add", "origin", remote], cwd=target)

    branch_ref = f"refs/heads/{branch}"
    run_git(
        ["fetch", "--quiet", "--depth=1", "--no-tags", "origin", branch_ref],
        cwd=target,
    )

    # Usually the push SHA is the branch tip and is already present. If a
    # newer commit arrived while this run was queued, try fetching the event
    # SHA directly. Some servers reject unadvertised SHAs; in that case,
    # deepen the pushed branch and verify that the event commit is reachable.
    has_commit = subprocess.run(
        ["git", "-C", str(target), "cat-file", "-e", f"{commit}^{{commit}}"],
        check=False,
        capture_output=True,
    ).returncode == 0
    if not has_commit:
        direct_fetch = subprocess.run(
            ["git", "-C", str(target), "fetch", "--quiet", "--depth=1", "--no-tags", "origin", commit],
            text=True,
            capture_output=True,
            check=False,
        )
        if direct_fetch.returncode != 0:
            run_git(
                ["fetch", "--quiet", "--unshallow", "--no-tags", "origin", branch_ref],
                cwd=target,
            )

    has_commit = subprocess.run(
        ["git", "-C", str(target), "cat-file", "-e", f"{commit}^{{commit}}"],
        check=False,
        capture_output=True,
    ).returncode == 0
    if not has_commit:
        raise RuntimeError(
            f"The event commit {commit} is not available from branch {branch}; "
            "refusing to build a different revision"
        )

    run_git(["checkout", "--quiet", "--detach", commit], cwd=target)
    actual = run_git(["rev-parse", "HEAD"], cwd=target)
    if actual.lower() != commit.lower():
        raise RuntimeError(
            f"Source checkout mismatch: requested {commit}, checked out {actual}"
        )


def clone_exact_commit(repository: str, branch: str, commit: str, target: Path) -> None:
    remote = f"https://github.com/{repository}.git"
    checkout_exact_commit(remote, branch, commit, target)


def clone_branch(repository: str, branch: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    remote = f"https://github.com/{repository}.git"
    run_git([
        "clone", "--quiet", "--depth=1", "--single-branch", "--no-tags",
        "--branch", branch, remote, str(target),
    ])
    actual_branch = run_git(["branch", "--show-current"], cwd=target)
    if actual_branch != branch:
        raise RuntimeError(
            f"Kernel repository branch mismatch: requested {branch}, checked out {actual_branch}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--driver-family", required=True, help="e.g. 340xx, 390xx, 470xx")
    parser.add_argument("--source-repository", required=True, help="owner/nvidia-NNNxx-utils")
    parser.add_argument("--source-branch", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--kernel-repository", required=True, help="owner/nvidia-NNNxx")
    parser.add_argument("--kernel-branch", default="develop")
    parser.add_argument("--manjaro-branch", choices=["stable", "testing", "unstable"], default="testing")
    parser.add_argument("--results-branch", required=True)
    parser.add_argument("--workdir", type=Path, default=Path("/build"))
    parser.add_argument("--history-keep", type=int, default=30)
    parser.add_argument("--raw-logs", choices=["none", "non-clean", "all"], default="all")
    parser.add_argument("--raw-logs-format", choices=["auto", "zstd", "gzip", "none"], default="auto")
    parser.add_argument("--kernels", default="", help="Optional comma-separated kernel prefix whitelist")
    parser.add_argument("--no-publish", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if not re.fullmatch(r"[0-9]+xx", args.driver_family):
            raise ValueError(f"Invalid driver family: {args.driver_family!r}")
        validate_ref(args.source_branch, "source branch")
        validate_ref(args.kernel_branch, "kernel branch")
        validate_ref(args.results_branch, "results branch")
        source_repo = validate_repository(
            args.source_repository, f"nvidia-{args.driver_family}-utils"
        )
        kernel_repo = validate_repository(
            args.kernel_repository, f"nvidia-{args.driver_family}"
        )
        if args.history_keep < 0:
            raise ValueError("--history-keep must be zero or greater")

        run_started_utc = datetime.now(timezone.utc).isoformat()
        ci = load_nvidia_ci()
        workdir = args.workdir.expanduser().resolve()
        sources_dir = workdir / ci.DEFAULT_SOURCES_SUBDIR
        sources_dir.mkdir(parents=True, exist_ok=True)
        utils_dir = sources_dir / f"nvidia-{args.driver_family}-utils"
        kernel_dir = sources_dir / f"nvidia-{args.driver_family}"

        print(f"[driver-build] family: {args.driver_family}")
        print(f"[driver-build] source: {source_repo}@{args.source_branch} ({args.source_sha})")
        print(f"[driver-build] kernels: {kernel_repo}@{args.kernel_branch}")
        clone_exact_commit(source_repo, args.source_branch, args.source_sha, utils_dir)
        clone_branch(kernel_repo, args.kernel_branch, kernel_dir)

        kernel_filter = [k.strip() for k in args.kernels.split(",") if k.strip()]
        cfg = ci.Config(
            url=f"https://github.com/{source_repo}",
            workdir=workdir,
            drivers=[args.driver_family],
            kernels=kernel_filter,
            manjaro_branch=args.manjaro_branch,
            publish=not args.no_publish,
            results_branch=args.results_branch,
            history_keep=args.history_keep,
            raw_logs=args.raw_logs,
            raw_logs_format=args.raw_logs_format,
        )

        plan = ci.phase_inspect(cfg)
        if len(plan.utils_plans) != 1:
            found = [up.utils.name for up in plan.utils_plans]
            raise RuntimeError(
                f"Expected exactly one {args.driver_family} utils package, found: {found}"
            )
        up = plan.utils_plans[0]
        modules = up.closed_modules + up.open_modules
        if not modules:
            raise RuntimeError(
                f"No {args.driver_family} kernel-module PKGBUILDs found in {kernel_repo}@{args.kernel_branch}"
            )
        if up.utils.pkgver in ("", "0"):
            raise RuntimeError("The selected utils PKGBUILD has no valid pkgver")

        kernel_matrix = [
            {"kernel": m.kernel_prefix, "variant": m.variant, "package": m.name}
            for m in modules
        ]
        print(
            "[driver-build] kernel packages: "
            + ", ".join(f"{m.kernel_prefix}{' (RT)' if m.variant == 'rt' else ''}" for m in modules)
        )

        harvest_dir = cfg.harvest_dir
        harvest_dir.mkdir(parents=True, exist_ok=True)
        metadata = {
            "driver_family": args.driver_family,
            "source_repository": source_repo,
            "source_branch": args.source_branch,
            "source_sha": args.source_sha.lower(),
            "kernel_repository": kernel_repo,
            "kernel_branch": args.kernel_branch,
            "manjaro_branch": args.manjaro_branch,
            "utils_pkgver": up.utils.pkgver,
            "utils_pkgrel": up.utils.pkgrel,
            "kernel_matrix": kernel_matrix,
            "run_started_utc": run_started_utc,
        }
        (harvest_dir / "build-metadata.json").write_text(
            json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
        )

        ci.phase_eol(cfg, plan)
        ci.phase_build(cfg, plan)

        if cfg.publish:
            repository = os.environ.get("GITHUB_REPOSITORY", "")
            token = os.environ.get("GITHUB_TOKEN")
            if not repository:
                raise RuntimeError("GITHUB_REPOSITORY is required when publishing")
            restore_harvest_history(repository, cfg.results_branch, harvest_dir, token)

        ci.phase_harvest(cfg)
        if not (harvest_dir / "README.md").is_file():
            raise RuntimeError(
                "harvest did not generate README.md; no recognizable build logs were found"
            )
        if cfg.publish:
            ci.phase_publish(cfg)
        else:
            print("[driver-build] publishing disabled")
        print("[driver-build] completed")
        return 0
    except Exception as exc:  # noqa: BLE001 - report an actionable workflow error
        print(f"[driver-build][error] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
