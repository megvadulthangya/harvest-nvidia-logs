#!/usr/bin/env python3
"""
nvidia-ci
=========

One-stop orchestrator for building and harvesting NVIDIA driver
branches across multiple Manjaro kernels.

Phases (each independently runnable via --phase, or all via --all):

  discover   Resolve an input URL (flat repo OR user/org/group) into a
             concrete list of source repositories to clone.
  clone      git clone each discovered repository.
  inspect    Parse every PKGBUILD, build a structured build plan, and
             determine the DKMS multiplicity of each utils package.
  eol        Cross-check every discovered package against the Manjaro
             repositories (pacman -Ss) to spot EOL / stale packages.
  build      Execute the build plan (utils + kernel modules) in the
             correct order, handling simple and complex (dual-DKMS)
             branches.
  harvest    Invoke `harvest-nvidia-logs` on the resulting build tree.
  publish    Push README.md + history/ to the results branch.
             ONLY runs when --publish is given.

Designed to run both inside GitHub Actions and on a local workstation.
Nothing is pushed unless --publish is explicitly set.

Sources support:
  - Flat layout:   single repo URL (…/PKGBUILDs.git)
  - Non-flat:      GitHub user, GitLab group, Forgejo org
  - Any git URL:   direct clone target

Platform APIs used for non-flat discovery:
  - Forgejo / Gitea  (code.manjaro.org)
  - GitLab           (gitlab.manjaro.org)
  - GitHub           (github.com)

Configuration via CLI args and/or a TOML file:

  nvidia-ci --config ci-config.toml --all
  nvidia-ci --all --url https://github.com/user --drivers 340xx,390xx
  nvidia-ci --phase discover --url https://code.manjaro.org/packages

Dependencies: Python 3.11+ (for tomllib), git, curl or urllib.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


__version__ = "0.1.1"


# ---------------------------------------------------------------------------
# Default paths and constants
# ---------------------------------------------------------------------------

DEFAULT_WORKDIR = Path("/build")
DEFAULT_SOURCES_SUBDIR = "sources"
DEFAULT_HARVEST_SUBDIR = "harvest"

DEFAULT_MANJARO_BRANCH = "testing"
DEFAULT_HISTORY_KEEP = 30

DEFAULT_SOURCE_URL = "https://code.manjaro.org/packages/PKGBUILDs.git"
DEFAULT_RESULTS_BRANCH = "results"

HARVEST_BINARY = "harvest-nvidia-logs"

SOURCE_EXCLUDE_PATTERNS = [
    r"-settings$",
    r"driver-assistant",
    r"graphics-drivers",
    r"^lib32-",
    r"bumblebee",
    r"harvest-nvidia-logs",
]

SOURCE_INCLUDE_PATTERNS = [
    re.compile(r"^nvidia$"),
    re.compile(r"^nvidia-open$"),
    re.compile(r"^nvidia-utils$"),
    re.compile(r"^nvidia-\d+xx$"),
    re.compile(r"^nvidia-\d+xx-utils$"),
    re.compile(r"^nvidia-\d+xx-open$"),
]

KERNEL_NAMESPACE_PATTERN = re.compile(r"linux\d+(-rt)?-extramodules$")


# ---------------------------------------------------------------------------
# Logging helpers
# ---------------------------------------------------------------------------

QUIET = False


def log(msg: str) -> None:
    if not QUIET:
        print(f"[nvidia-ci] {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"[nvidia-ci][warn] {msg}", file=sys.stderr)


def die(msg: str, code: int = 1) -> None:
    print(f"[nvidia-ci][error] {msg}", file=sys.stderr)
    sys.exit(code)


def run(cmd: list[str], check: bool = True, capture: bool = False) -> subprocess.CompletedProcess:
    log(f"$ {' '.join(str(c) for c in cmd)}")
    if capture:
        return subprocess.run(cmd, check=check, text=True, capture_output=True)
    return subprocess.run(cmd, check=check)


def looks_like_placeholder(token: str) -> bool:
    """Detect tokens that obviously are not real (docs examples etc.)."""
    low = token.lower()
    for marker in ("xxx", "your_token", "example", "changeme", "placeholder"):
        if marker in low:
            return True
    # Real GitHub tokens are 40+ chars; anything shorter is suspicious
    if len(token) < 20:
        return True
    return False


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class SourceRepo:
    url: str
    branch: str
    target: Path
    kind: str
    label: str = ""


@dataclass
class PackageInfo:
    name: str
    pkgver: str
    pkgrel: str
    source_dir: Path
    pkgbuild_path: Path
    dkms_names: list[str]
    kind: str
    branch_label: str = ""
    kernel_prefix: str = ""
    variant: str = ""
    makedepends: list[str] = field(default_factory=list)
    depends: list[str] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    provides: list[str] = field(default_factory=list)
    required_dkms: str = ""


@dataclass
class UtilsPlan:
    utils: PackageInfo
    closed_dkms: str | None
    open_dkms: str | None
    closed_modules: list[PackageInfo] = field(default_factory=list)
    open_modules: list[PackageInfo] = field(default_factory=list)
    clean_label: str = ""


@dataclass
class BuildPlan:
    utils_plans: list[UtilsPlan] = field(default_factory=list)
    kernels: list[str] = field(default_factory=list)
    eol_packages: list[dict] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class Config:
    url: str = DEFAULT_SOURCE_URL
    workdir: Path = DEFAULT_WORKDIR
    source_branch: str | None = None
    drivers_branch: str | None = None
    kernels_branch: str | None = None
    drivers: list[str] = field(default_factory=list)
    exclude_drivers: list[str] = field(default_factory=list)
    kernels: list[str] = field(default_factory=list)
    exclude_kernels: list[str] = field(default_factory=list)
    manjaro_branch: str = DEFAULT_MANJARO_BRANCH
    publish: bool = False
    results_branch: str = DEFAULT_RESULTS_BRANCH
    history_keep: int = DEFAULT_HISTORY_KEEP
    header_lines: int = 10
    quiet: bool = False

    @property
    def sources_dir(self) -> Path:
        return self.workdir / DEFAULT_SOURCES_SUBDIR

    @property
    def harvest_dir(self) -> Path:
        return self.workdir / DEFAULT_HARVEST_SUBDIR


def load_config(path: Path | None) -> dict:
    if path is None:
        return {}
    if not path.is_file():
        die(f"config file not found: {path}")
    with path.open("rb") as f:
        return tomllib.load(f)


def merge_config(args: argparse.Namespace, toml: dict) -> Config:
    cfg = Config()

    src = toml.get("source", {})
    if "url" in src:
        cfg.url = src["url"]

    branches = toml.get("branches", {})
    cfg.source_branch = branches.get("source")
    cfg.drivers_branch = branches.get("drivers")
    cfg.kernels_branch = branches.get("kernels")

    filt = toml.get("filters", {})
    cfg.drivers = list(filt.get("drivers", []))
    cfg.exclude_drivers = list(filt.get("exclude_drivers", []))
    cfg.kernels = list(filt.get("kernels", []))
    cfg.exclude_kernels = list(filt.get("exclude_kernels", []))

    manj = toml.get("manjaro", {})
    if "branch" in manj:
        cfg.manjaro_branch = manj["branch"]

    harvest = toml.get("harvest", {})
    if "history_keep" in harvest:
        cfg.history_keep = int(harvest["history_keep"])
    if "header_lines" in harvest:
        cfg.header_lines = int(harvest["header_lines"])

    pub = toml.get("publish", {})
    if "enabled" in pub:
        cfg.publish = bool(pub["enabled"])
    if "results_branch" in pub:
        cfg.results_branch = pub["results_branch"]

    if args.url:
        cfg.url = args.url
    if args.workdir:
        cfg.workdir = Path(args.workdir).expanduser().resolve()
    if args.source_branch:
        cfg.source_branch = args.source_branch
    if args.drivers_branch:
        cfg.drivers_branch = args.drivers_branch
    if args.kernels_branch:
        cfg.kernels_branch = args.kernels_branch
    if args.drivers:
        cfg.drivers = [d.strip() for d in args.drivers.split(",") if d.strip()]
    if args.exclude_drivers:
        cfg.exclude_drivers = [
            d.strip() for d in args.exclude_drivers.split(",") if d.strip()
        ]
    if args.kernels:
        cfg.kernels = [k.strip() for k in args.kernels.split(",") if k.strip()]
    if args.exclude_kernels:
        cfg.exclude_kernels = [
            k.strip() for k in args.exclude_kernels.split(",") if k.strip()
        ]
    if args.manjaro_branch:
        cfg.manjaro_branch = args.manjaro_branch
    if args.publish:
        cfg.publish = True
    if args.results_branch:
        cfg.results_branch = args.results_branch
    if args.history_keep is not None:
        cfg.history_keep = args.history_keep
    if args.header_lines is not None:
        cfg.header_lines = args.header_lines
    if args.quiet:
        cfg.quiet = True

    return cfg


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def http_json(url: str, token: str | None = None) -> object:
    """Fetch JSON from a URL. If a token is provided but rejected (401),
    retry without it so public repos still work."""
    headers = {"User-Agent": f"nvidia-ci/{__version__}"}
    use_token = token and not looks_like_placeholder(token)
    if use_token:
        headers["Authorization"] = f"Bearer {token}"

    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        if e.code == 401 and use_token:
            warn(f"HTTP 401 with token; retrying without auth for {url}")
            return http_json(url, None)
        die(f"HTTP {e.code} for {url}: {e.reason}")
    except URLError as e:
        die(f"network error for {url}: {e.reason}")


def paginated_json(base_url: str, token: str | None, page_param: str = "page",
                   limit_param: str = "per_page", limit: int = 100,
                   max_pages: int = 20) -> list:
    results: list = []
    for page in range(1, max_pages + 1):
        sep = "&" if "?" in base_url else "?"
        url = f"{base_url}{sep}{limit_param}={limit}&{page_param}={page}"
        data = http_json(url, token)
        if not isinstance(data, list):
            break
        if not data:
            break
        results.extend(data)
        if len(data) < limit:
            break
    return results


# ---------------------------------------------------------------------------
# Platform detection
# ---------------------------------------------------------------------------

def detect_platform(url: str) -> str:
    low = url.lower()
    if "github.com" in low or "api.github.com" in low:
        return "github"
    if "gitlab" in low:
        return "gitlab"
    if "code.manjaro.org" in low or "gitea" in low or "forgejo" in low:
        return "forgejo"
    return "unknown"


def is_repo_url(url: str) -> bool:
    low = url.lower()
    if low.endswith(".git"):
        return True
    m = re.match(r"^https?://[^/]+/([^/]+)/([^/]+?)/?$", url)
    if m:
        return True
    return False


# ---------------------------------------------------------------------------
# Phase 1 — discover
# ---------------------------------------------------------------------------

def discover_flat_repo(url: str, cfg: Config) -> list[SourceRepo]:
    branch = cfg.source_branch or "HEAD"
    name = url.rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]
    target = cfg.sources_dir / name
    return [SourceRepo(
        url=url,
        branch=branch,
        target=target,
        kind="flat",
        label=name,
    )]


def discover_non_flat(url: str, cfg: Config, token: str | None) -> list[SourceRepo]:
    platform = detect_platform(url)
    repos: list[dict] = []

    if platform == "github":
        m = re.match(r"^https?://github\.com/([^/]+)/?$", url)
        if not m:
            die(f"cannot parse GitHub URL: {url}")
        owner = m.group(1)
        api = f"https://api.github.com/users/{owner}/repos"
        repos = paginated_json(api, token)
        for r in repos:
            r["_clone_url"] = r["clone_url"]
            r["_default_branch"] = r.get("default_branch", "main")
            r["_name"] = r["name"]

    elif platform == "gitlab":
        m = re.match(r"^https?://([^/]+)/(.+?)/?$", url)
        if not m:
            die(f"cannot parse GitLab URL: {url}")
        host, group_path = m.group(1), m.group(2)
        encoded_group = quote(group_path, safe="")
        api = (
            f"https://{host}/api/v4/groups/{encoded_group}/projects"
            f"?include_subgroups=true"
        )
        repos = paginated_json(api, token)
        for r in repos:
            r["_clone_url"] = r["http_url_to_repo"]
            r["_default_branch"] = r.get("default_branch") or "main"
            r["_name"] = r["path"]

    elif platform == "forgejo":
        m = re.match(r"^https?://([^/]+)/([^/]+)/?$", url)
        if not m:
            die(f"cannot parse Forgejo URL: {url}")
        host, org = m.group(1), m.group(2)
        api = f"https://{host}/api/v1/orgs/{org}/repos"
        repos = paginated_json(api, token, page_param="page", limit_param="limit")
        for r in repos:
            r["_clone_url"] = r["clone_url"]
            r["_default_branch"] = r.get("default_branch") or "main"
            r["_name"] = r["name"]

    else:
        die(f"unsupported URL for non-flat discovery: {url}")

    selected: list[dict] = []
    for r in repos:
        name = r["_name"]
        if not any(p.match(name) for p in SOURCE_INCLUDE_PATTERNS):
            continue
        if any(re.search(x, name) for x in SOURCE_EXCLUDE_PATTERNS):
            continue
        selected.append(r)

    log(f"platform={platform}  total={len(repos)}  selected={len(selected)}")

    out: list[SourceRepo] = []
    for r in selected:
        name = r["_name"]
        kind = "unknown"
        branch = cfg.drivers_branch or r["_default_branch"]
        if name.endswith("-utils"):
            kind = "utils"
        elif name.endswith("-open") or name == "nvidia" or re.match(r"^nvidia-\d+xx$", name):
            kind = "kernel"
            branch = cfg.kernels_branch or r["_default_branch"]

        out.append(SourceRepo(
            url=r["_clone_url"],
            branch=branch,
            target=cfg.sources_dir / name,
            kind=kind,
            label=name,
        ))
    return out


def discover_gitlab_kernel_namespaces(url: str, cfg: Config, token: str | None) -> list[SourceRepo]:
    platform = detect_platform(url)
    if platform != "gitlab":
        return []

    m = re.match(r"^https?://([^/]+)/(.+?)/?$", url)
    if not m:
        return []
    host, group_path = m.group(1), m.group(2)

    encoded = quote(group_path, safe="")
    api = f"https://{host}/api/v4/groups/{encoded}/subgroups?per_page=100"
    try:
        subgroups = paginated_json(api, token)
    except SystemExit:
        return []

    out: list[SourceRepo] = []
    for sg in subgroups:
        if not isinstance(sg, dict):
            continue
        sg_path = sg.get("full_path", "")
        if not KERNEL_NAMESPACE_PATTERN.search(sg_path):
            continue
        encoded_sg = quote(sg_path, safe="")
        proj_api = (
            f"https://{host}/api/v4/groups/{encoded_sg}/projects"
            f"?per_page=100"
        )
        try:
            projects = paginated_json(proj_api, token)
        except SystemExit:
            continue
        for p in projects:
            if not isinstance(p, dict):
                continue
            name = p.get("path", "")
            if not name.startswith("nvidia"):
                continue
            if any(re.search(x, name) for x in SOURCE_EXCLUDE_PATTERNS):
                continue
            out.append(SourceRepo(
                url=p["http_url_to_repo"],
                branch=cfg.kernels_branch or p.get("default_branch", "main"),
                target=cfg.sources_dir / sg_path.replace("/", "__") / name,
                kind="kernel",
                label=f"{sg_path}/{name}",
            ))
    return out


def phase_discover(cfg: Config, token: str | None) -> list[SourceRepo]:
    cfg.sources_dir.mkdir(parents=True, exist_ok=True)

    if is_repo_url(cfg.url):
        sources = discover_flat_repo(cfg.url, cfg)
    else:
        sources = discover_non_flat(cfg.url, cfg, token)
        sources.extend(discover_gitlab_kernel_namespaces(cfg.url, cfg, token))

    manifest = cfg.sources_dir / "sources.json"
    manifest.write_text(json.dumps([asdict(s) for s in sources], indent=2, default=str))

    log(f"discover: {len(sources)} source(s) -> {manifest}")
    return sources


# ---------------------------------------------------------------------------
# Phase 2 — clone
# ---------------------------------------------------------------------------

def phase_clone(cfg: Config) -> None:
    manifest = cfg.sources_dir / "sources.json"
    if not manifest.is_file():
        die("no sources manifest — run discover first")
    data = json.loads(manifest.read_text())
    sources = [SourceRepo(
        url=d["url"],
        branch=d["branch"],
        target=Path(d["target"]),
        kind=d["kind"],
        label=d.get("label", ""),
    ) for d in data]

    for s in sources:
        if s.target.is_dir() and (s.target / ".git").is_dir():
            log(f"already cloned: {s.target}")
            continue
        s.target.parent.mkdir(parents=True, exist_ok=True)
        cmd = ["git", "clone", "--depth=1"]
        if s.branch and s.branch != "HEAD":
            cmd += ["--branch", s.branch]
        cmd += [s.url, str(s.target)]
        try:
            run(cmd)
        except subprocess.CalledProcessError as e:
            warn(f"clone failed for {s.url} @ {s.branch}: {e}")
            continue
    log("clone: done")


# ---------------------------------------------------------------------------
# PKGBUILD parsing
# ---------------------------------------------------------------------------

_RE_ASSIGN = re.compile(
    r"^\s*(pkgname|pkgbase|pkgver|pkgrel|depends|makedepends|conflicts|provides)\s*=\s*(.+)$"
)

_RE_ARRAY_ITEM = re.compile(r"'([^']*)'|\"([^\"]*)\"|(\S+)")


def _parse_array_literal(raw: str) -> list[str]:
    items: list[str] = []
    for m in _RE_ARRAY_ITEM.finditer(raw):
        val = m.group(1) or m.group(2) or m.group(3) or ""
        val = val.strip().rstrip(",")
        if not val:
            continue
        if val.startswith("$") or val.startswith("(") or val.endswith(")"):
            continue
        items.append(val)
    return items


def _extract_array(text: str, varname: str) -> str:
    pattern = re.compile(rf"^\s*{varname}\s*=\s*\(", re.MULTILINE)
    m = pattern.search(text)
    if not m:
        return ""
    start = m.end() - 1
    depth = 0
    i = start
    in_single = False
    in_double = False
    while i < len(text):
        c = text[i]
        if c == "'" and not in_double:
            in_single = not in_single
        elif c == '"' and not in_single:
            in_double = not in_double
        elif not in_single and not in_double:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return text[start + 1:i]
        i += 1
    return ""


def parse_pkgbuild(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    normalized = re.sub(r"\\\n", " ", text)

    result: dict = {
        "pkgbase": None,
        "pkgname": [],
        "pkgver": None,
        "pkgrel": None,
        "depends": [],
        "makedepends": [],
        "conflicts": [],
        "provides": [],
    }

    for line in normalized.splitlines():
        m = _RE_ASSIGN.match(line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()

        if key == "pkgbase":
            result["pkgbase"] = raw.strip("'\"")
        elif key == "pkgver":
            result["pkgver"] = raw.strip("'\"")
        elif key == "pkgrel":
            result["pkgrel"] = raw.strip("'\"")
        elif key == "pkgname":
            if raw.startswith("("):
                result["pkgname"] = _parse_array_literal(_extract_array(text, "pkgname"))
            else:
                result["pkgname"] = [raw.strip("'\"")]
        elif key in ("depends", "makedepends", "conflicts", "provides"):
            if raw.startswith("("):
                result[key] = _parse_array_literal(_extract_array(text, key))
            else:
                result[key] = [raw.strip("'\"")]

    return result


# ---------------------------------------------------------------------------
# Phase 3 — inspect
# ---------------------------------------------------------------------------

def _branch_label_from_utils_name(name: str) -> str:
    if name == "nvidia-utils":
        return "current"
    m = re.match(r"^nvidia-(\d+xx)-utils$", name)
    if m:
        return m.group(1)
    return name


def _branch_label_from_kernel_dir(name: str, prefix: str) -> str:
    if name in ("nvidia", "nvidia-open"):
        return name
    m = re.match(r"^nvidia-(\d+xx)(-open)?$", name)
    if m:
        return m.group(1) + (m.group(2) or "")
    return name


def _kernel_prefix_variant(prefix_dir_name: str) -> tuple[str, str]:
    base = prefix_dir_name[: -len("-extramodules")]
    variant = "rt" if base.endswith("-rt") else "normal"
    return base, variant


def _parse_all_pkgbuilds(cfg: Config) -> list[PackageInfo]:
    out: list[PackageInfo] = []
    root = cfg.sources_dir

    for pkgbuild in sorted(root.rglob("PKGBUILD")):
        parent = pkgbuild.parent
        if ".git" in parent.parts:
            continue
        try:
            meta = parse_pkgbuild(pkgbuild)
        except Exception as e:
            warn(f"failed to parse {pkgbuild}: {e}")
            continue

        pkgname_list: list[str] = meta.get("pkgname") or []
        pkgbase: str | None = meta.get("pkgbase")
        top_name = pkgbase or (pkgname_list[0] if pkgname_list else parent.name)

        dkms_names = [n for n in pkgname_list if n.endswith("-dkms")]

        kind = "unknown"
        branch_label = ""
        kernel_prefix = ""
        variant = ""

        extramod_idx = None
        for i, p in enumerate(parent.parts):
            if p.endswith("-extramodules"):
                extramod_idx = i
                break

        if extramod_idx is not None and extramod_idx + 1 < len(parent.parts):
            kernel_prefix, variant = _kernel_prefix_variant(parent.parts[extramod_idx])
            nv_dir = parent.parts[extramod_idx + 1]
            branch_label = _branch_label_from_kernel_dir(nv_dir, kernel_prefix)
            kind = "kernel"
        elif top_name.endswith("-utils"):
            branch_label = _branch_label_from_utils_name(top_name)
            kind = "utils"
        elif re.match(r"^nvidia(-\d+xx)?(-open)?$", top_name):
            branch_label = _branch_label_from_kernel_dir(top_name, "")
            kind = "kernel"

        required_dkms = ""
        for dep in meta.get("makedepends", []) + meta.get("depends", []):
            base = dep.split("=", 1)[0].split(">", 1)[0].split("<", 1)[0].strip()
            if base.endswith("-dkms"):
                required_dkms = base
                break

        out.append(PackageInfo(
            name=top_name,
            pkgver=meta.get("pkgver", "0"),
            pkgrel=meta.get("pkgrel", "1"),
            source_dir=parent,
            pkgbuild_path=pkgbuild,
            dkms_names=dkms_names,
            kind=kind,
            branch_label=branch_label,
            kernel_prefix=kernel_prefix,
            variant=variant,
            makedepends=meta.get("makedepends", []),
            depends=meta.get("depends", []),
            conflicts=meta.get("conflicts", []),
            provides=meta.get("provides", []),
            required_dkms=required_dkms,
        ))

    return out


def _apply_filters(pkgs: list[PackageInfo], cfg: Config) -> list[PackageInfo]:
    out = pkgs
    if cfg.drivers:
        wanted = set(cfg.drivers)
        out = [p for p in out if p.branch_label in wanted]
    if cfg.exclude_drivers:
        skip = set(cfg.exclude_drivers)
        out = [p for p in out if p.branch_label not in skip]
    if cfg.kernels:
        wanted = set(cfg.kernels)
        out = [p for p in out
               if p.kind != "kernel" or p.kernel_prefix in wanted]
    if cfg.exclude_kernels:
        skip = set(cfg.exclude_kernels)
        out = [p for p in out
               if p.kind != "kernel" or p.kernel_prefix not in skip]
    return out


def _build_plan(pkgs: list[PackageInfo]) -> BuildPlan:
    plan = BuildPlan()

    kernels: set[str] = set()
    for p in pkgs:
        if p.kind == "kernel" and p.kernel_prefix:
            kernels.add(p.kernel_prefix)
    plan.kernels = sorted(kernels)

    utils_pkgs = [p for p in pkgs if p.kind == "utils"]
    kernel_pkgs = [p for p in pkgs if p.kind == "kernel"]

    for u in sorted(utils_pkgs, key=lambda x: x.branch_label):
        closed = None
        open_dkms = None
        for d in u.dkms_names:
            if d.endswith("-open-dkms"):
                open_dkms = d
            elif d.endswith("-dkms"):
                closed = d

        closed_modules: list[PackageInfo] = []
        open_modules: list[PackageInfo] = []

        for k in kernel_pkgs:
            if k.branch_label != u.branch_label and \
               not (u.branch_label == "current" and k.branch_label == "nvidia"):
                continue
            if k.required_dkms == closed:
                closed_modules.append(k)
            elif open_dkms and k.required_dkms == open_dkms:
                open_modules.append(k)
            elif k.required_dkms == "":
                if k.source_dir.name.endswith("-open"):
                    open_modules.append(k)
                else:
                    closed_modules.append(k)

        plan.utils_plans.append(UtilsPlan(
            utils=u,
            closed_dkms=closed,
            open_dkms=open_dkms,
            closed_modules=sorted(closed_modules, key=lambda x: x.kernel_prefix),
            open_modules=sorted(open_modules, key=lambda x: x.kernel_prefix),
            clean_label=u.branch_label,
        ))

    return plan


def phase_inspect(cfg: Config) -> BuildPlan:
    log("inspect: parsing PKGBUILDs...")
    all_pkgs = _parse_all_pkgbuilds(cfg)
    log(f"inspect: found {len(all_pkgs)} PKGBUILD(s)")

    filtered = _apply_filters(all_pkgs, cfg)
    log(f"inspect: {len(filtered)} after filter")

    plan = _build_plan(filtered)
    log(f"inspect: {len(plan.utils_plans)} utils plan(s), "
        f"kernels: {', '.join(plan.kernels) or '—'}")

    for up in plan.utils_plans:
        kind = "complex" if up.open_dkms else "simple"
        log(f"  {up.utils.name} [{kind}] "
            f"closed_modules={len(up.closed_modules)} "
            f"open_modules={len(up.open_modules)}")

    plan_path = cfg.workdir / "build-plan.json"
    plan_path.write_text(json.dumps({
        "kernels": plan.kernels,
        "utils_plans": [
            {
                "utils_name": up.utils.name,
                "utils_dir": str(up.utils.source_dir),
                "utils_pkgver": up.utils.pkgver,
                "utils_pkgrel": up.utils.pkgrel,
                "closed_dkms": up.closed_dkms,
                "open_dkms": up.open_dkms,
                "clean_label": up.clean_label,
                "closed_modules": [
                    {
                        "name": m.name,
                        "dir": str(m.source_dir),
                        "kernel_prefix": m.kernel_prefix,
                        "variant": m.variant,
                        "required_dkms": m.required_dkms,
                    }
                    for m in up.closed_modules
                ],
                "open_modules": [
                    {
                        "name": m.name,
                        "dir": str(m.source_dir),
                        "kernel_prefix": m.kernel_prefix,
                        "variant": m.variant,
                        "required_dkms": m.required_dkms,
                    }
                    for m in up.open_modules
                ],
            }
            for up in plan.utils_plans
        ],
    }, indent=2, default=str))

    log(f"inspect: plan written to {plan_path}")
    return plan


# ---------------------------------------------------------------------------
# Phase 4 — EOL check
# ---------------------------------------------------------------------------

def _pacman_query(name: str) -> tuple[str, str] | None:
    try:
        proc = subprocess.run(
            ["pacman", "-Si", name],
            text=True, capture_output=True, check=False,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    version = ""
    repo = ""
    for line in proc.stdout.splitlines():
        if line.startswith("Repository"):
            repo = line.split(":", 1)[1].strip()
        elif line.startswith("Version"):
            version = line.split(":", 1)[1].strip()
    if version:
        return version, repo
    return None


def phase_eol(cfg: Config, plan: BuildPlan) -> list[dict]:
    log("eol: querying pacman for each package...")
    results: list[dict] = []
    seen: set[str] = set()

    for up in plan.utils_plans:
        candidates: list[str] = [up.utils.name]
        candidates.extend(up.utils.dkms_names)
        for m in up.closed_modules + up.open_modules:
            candidates.append(m.name)

        for name in candidates:
            if name in seen:
                continue
            seen.add(name)
            hit = _pacman_query(name)
            if hit is None:
                results.append({
                    "package": name,
                    "repo_version": None,
                    "manjaro_version": None,
                    "status": "not-in-manjaro",
                })
            else:
                manjaro_ver, repo = hit
                results.append({
                    "package": name,
                    "repo_version": None,
                    "manjaro_version": manjaro_ver,
                    "repo_name": repo,
                    "status": "ok",
                })

    for up in plan.utils_plans:
        expected = f"{up.utils.pkgver}-{up.utils.pkgrel}"
        for r in results:
            if r["package"] == up.utils.name:
                r["repo_version"] = expected
                if r["manjaro_version"] and \
                        not r["manjaro_version"].startswith(up.utils.pkgver):
                    r["status"] = "stale"

    for prefix in plan.kernels:
        hit = _pacman_query(prefix)
        results.append({
            "package": prefix,
            "repo_version": None,
            "manjaro_version": hit[0] if hit else None,
            "status": "ok" if hit else "not-in-manjaro",
        })

    eol_path = cfg.workdir / "eol-list.json"
    eol_path.write_text(json.dumps(results, indent=2))

    n_bad = sum(1 for r in results if r["status"] != "ok")
    log(f"eol: {n_bad}/{len(results)} package(s) flagged -> {eol_path}")
    return results


# ---------------------------------------------------------------------------
# Phase 5 — build
# ---------------------------------------------------------------------------

def _makepkg(dir_: Path, install: bool) -> bool:
    args = ["makepkg"]
    args.append("-si" if install else "-s")
    args += ["--noconfirm", "--skippgpcheck"]
    try:
        subprocess.run(args, cwd=dir_, check=True)
        return True
    except subprocess.CalledProcessError as e:
        warn(f"makepkg failed in {dir_}: exit {e.returncode}")
        return False


def _pacman_install(files: Iterable[Path]) -> bool:
    files = [f for f in files if f.is_file()]
    if not files:
        return False
    try:
        subprocess.run(
            ["sudo", "pacman", "-U", "--noconfirm"] + [str(f) for f in files],
            check=True,
        )
        return True
    except subprocess.CalledProcessError as e:
        warn(f"pacman -U failed: exit {e.returncode}")
        return False


def _cleanup(cfg: Config, label: str) -> None:
    script = cfg.workdir / "clean-nvidia-container.sh"
    if not script.is_file():
        alt = Path(__file__).parent / "clean-nvidia-container.sh"
        if alt.is_file():
            script = alt
    if not script.is_file():
        warn(f"cleanup script not found, skipping ({label})")
        return
    try:
        subprocess.run(["sudo", "bash", str(script), label], check=False)
    except FileNotFoundError:
        warn("sudo not available; cleanup skipped")


def _glob_artifacts(dir_: Path, patterns: list[str]) -> list[Path]:
    out: list[Path] = []
    for pat in patterns:
        out.extend(sorted(dir_.glob(pat)))
    return out


def phase_build(cfg: Config, plan: BuildPlan) -> None:
    for up in plan.utils_plans:
        log(f"=== build: {up.utils.name} ===")
        is_complex = up.open_dkms is not None

        if not is_complex:
            if not _makepkg(up.utils.source_dir, install=True):
                warn(f"skipping kernel modules for {up.utils.name}")
                _cleanup(cfg, up.clean_label)
                continue
            for m in up.closed_modules:
                _makepkg(m.source_dir, install=False)
            _cleanup(cfg, up.clean_label)
            continue

        if not _makepkg(up.utils.source_dir, install=False):
            warn(f"skipping kernel modules for {up.utils.name}")
            _cleanup(cfg, up.clean_label)
            continue

        base = up.utils.name[:-len("-utils")]
        closed_files = _glob_artifacts(up.utils.source_dir, [
            f"{base}-utils-*.pkg.tar.zst",
            f"opencl-{base}-*.pkg.tar.zst",
            f"{up.closed_dkms}-*.pkg.tar.zst",
            f"mhwd-{base}-*.pkg.tar.zst",
        ])
        _pacman_install(closed_files)

        for m in up.closed_modules:
            _makepkg(m.source_dir, install=False)

        _cleanup(cfg, up.clean_label)

        userspace_files = _glob_artifacts(up.utils.source_dir, [
            f"{base}-utils-*.pkg.tar.zst",
        ])
        _pacman_install(userspace_files)

        open_files = _glob_artifacts(up.utils.source_dir, [
            f"{up.open_dkms}-*.pkg.tar.zst",
        ])
        _pacman_install(open_files)

        for m in up.open_modules:
            _makepkg(m.source_dir, install=False)

        _cleanup(cfg, up.clean_label)

    log("build: done")


# ---------------------------------------------------------------------------
# Phase 6 — harvest
# ---------------------------------------------------------------------------

def phase_harvest(cfg: Config) -> None:
    cfg.harvest_dir.mkdir(parents=True, exist_ok=True)

    binary = shutil.which(HARVEST_BINARY)
    if not binary:
        alt = Path(__file__).parent / HARVEST_BINARY
        if alt.is_file():
            binary = str(alt)
    if not binary:
        die(f"{HARVEST_BINARY} not found in PATH or alongside this script")

    changelog = cfg.harvest_dir / "driver-changelog.md"
    run([
        binary,
        "-d", str(cfg.sources_dir),
        "-o", str(cfg.harvest_dir),
        "--diff",
        "--changelog", str(changelog),
        "--history-keep", str(cfg.history_keep),
        "-n", str(cfg.header_lines),
        "-q",
    ])

    index = cfg.harvest_dir / "INDEX.md"
    if index.is_file():
        (cfg.harvest_dir / "README.md").write_text(index.read_text())
    for d in sorted((cfg.harvest_dir / "history").glob("*/")):
        idx = d / "INDEX.md"
        if idx.is_file():
            (d / "README.md").write_text(idx.read_text())

    eol_path = cfg.workdir / "eol-list.json"
    if eol_path.is_file():
        eol_data = json.loads(eol_path.read_text())
        bad = [r for r in eol_data if r["status"] != "ok"]
        if bad:
            lines = ["", "## ⚠ EOL / Out-of-sync packages", ""]
            lines.append("| Package | Repo version | Manjaro version | Status |")
            lines.append("|---------|--------------|-----------------|--------|")
            for r in bad:
                rv = r.get("repo_version") or "—"
                mv = r.get("manjaro_version") or "—"
                lines.append(
                    f"| `{r['package']}` | {rv} | {mv} | {r['status']} |"
                )
            lines.append("")
            readme = cfg.harvest_dir / "README.md"
            readme.write_text(readme.read_text() + "\n".join(lines) + "\n")
            log(f"harvest: appended {len(bad)} EOL row(s) to README.md")

    log(f"harvest: output in {cfg.harvest_dir}")


# ---------------------------------------------------------------------------
# Phase 7 — publish
# ---------------------------------------------------------------------------

def phase_publish(cfg: Config) -> None:
    if not cfg.publish:
        log("publish: disabled (--publish not set)")
        return

    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        die("publish: GITHUB_TOKEN and GITHUB_REPOSITORY must be set")
    if looks_like_placeholder(token):
        die("publish: GITHUB_TOKEN looks like a placeholder")

    remote_url = f"https://x-access-token:{token}@github.com/{repo}.git"
    tmp = Path("/tmp/nvidia-ci-publish")
    if tmp.exists():
        shutil.rmtree(tmp)

    run(["git", "clone", remote_url, str(tmp)])
    subprocess.run(
        ["git", "config", "user.email",
         "github-actions[bot]@users.noreply.github.com"],
        cwd=tmp, check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "github-actions[bot]"],
        cwd=tmp, check=True,
    )

    has_branch = subprocess.run(
        ["git", "ls-remote", "--exit-code", "origin", cfg.results_branch],
        cwd=tmp, capture_output=True,
    ).returncode == 0

    if has_branch:
        subprocess.run(
            ["git", "fetch", "--depth", "1", "origin", cfg.results_branch],
            cwd=tmp, check=True,
        )
        subprocess.run(
            ["git", "checkout", "-B", cfg.results_branch,
             f"origin/{cfg.results_branch}"],
            cwd=tmp, check=True,
        )
    else:
        subprocess.run(
            ["git", "checkout", "-B", cfg.results_branch],
            cwd=tmp, check=True,
        )

    for child in tmp.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    for child in cfg.harvest_dir.iterdir():
        dst = tmp / child.name
        if child.is_dir():
            shutil.copytree(child, dst)
        else:
            shutil.copy2(child, dst)

    subprocess.run(["git", "add", "-A"], cwd=tmp, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=tmp)
    if diff.returncode == 0:
        log("publish: no changes to commit")
        return

    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    subprocess.run(["git", "commit", "-m", f"harvest: {ts}"], cwd=tmp, check=True)
    subprocess.run(["git", "push", "origin", cfg.results_branch], cwd=tmp, check=True)
    log(f"publish: pushed to {cfg.results_branch}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nvidia-ci",
        description="Build and harvest NVIDIA driver branches across "
                    "multiple Manjaro kernels.",
    )
    p.add_argument("--url", help="Source URL (repo .git, or user/org/group)")
    p.add_argument("--workdir", help=f"Work directory (default: {DEFAULT_WORKDIR})")
    p.add_argument("--config", help="TOML config file")

    p.add_argument("--all", action="store_true",
                   help="Run all phases")
    p.add_argument("--phase", choices=[
        "discover", "clone", "inspect", "eol", "build", "harvest", "publish",
    ], help="Run a single phase")

    p.add_argument("--source-branch",
                   help="Branch override for the source repo (flat)")
    p.add_argument("--drivers-branch",
                   help="Branch override for drivers/ dirs (non-flat)")
    p.add_argument("--kernels-branch",
                   help="Branch override for kernel modules (non-flat)")

    p.add_argument("--drivers", help="Comma-separated driver whitelist")
    p.add_argument("--exclude-drivers", help="Comma-separated driver blacklist")
    p.add_argument("--kernels", help="Comma-separated kernel prefix whitelist")
    p.add_argument("--exclude-kernels", help="Comma-separated kernel prefix blacklist")

    p.add_argument("--manjaro-branch",
                   choices=["stable", "testing", "unstable"],
                   help=f"Manjaro branch (default: {DEFAULT_MANJARO_BRANCH})")

    p.add_argument("--publish", action="store_true",
                   help="Push results to the results branch (GitHub Actions only)")
    p.add_argument("--results-branch",
                   help=f"Results branch (default: {DEFAULT_RESULTS_BRANCH})")
    p.add_argument("--history-keep", type=int,
                   help=f"History snapshots to keep (default: {DEFAULT_HISTORY_KEEP})")
    p.add_argument("--header-lines", type=int, help="Header lines per make.log")

    p.add_argument("-q", "--quiet", action="store_true")
    p.add_argument("--version", action="version",
                   version=f"%(prog)s {__version__}")
    return p


def main(argv: list[str] | None = None) -> int:
    global QUIET

    args = build_parser().parse_args(argv)
    toml = load_config(Path(args.config)) if args.config else {}
    cfg = merge_config(args, toml)
    QUIET = cfg.quiet

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITLAB_TOKEN")

    plan: BuildPlan | None = None

    def get_plan() -> BuildPlan:
        nonlocal plan
        if plan is None:
            plan = phase_inspect(cfg)
        return plan

    if args.phase == "discover":
        phase_discover(cfg, token)
        return 0
    if args.phase == "clone":
        phase_clone(cfg)
        return 0
    if args.phase == "inspect":
        phase_inspect(cfg)
        return 0
    if args.phase == "eol":
        phase_eol(cfg, get_plan())
        return 0
    if args.phase == "build":
        phase_build(cfg, get_plan())
        return 0
    if args.phase == "harvest":
        phase_harvest(cfg)
        return 0
    if args.phase == "publish":
        phase_publish(cfg)
        return 0

    if args.all:
        phase_discover(cfg, token)
        phase_clone(cfg)
        plan = phase_inspect(cfg)
        phase_eol(cfg, plan)
        phase_build(cfg, plan)
        phase_harvest(cfg)
        if cfg.publish:
            phase_publish(cfg)
        return 0

    build_parser().print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())