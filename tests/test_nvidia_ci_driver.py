#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "nvidia-ci-driver.py"
SPEC = importlib.util.spec_from_file_location("nvidia_ci_driver", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def git(*args: str, cwd: Path | None = None) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=cwd, text=True, capture_output=True, check=False
    )
    if proc.returncode:
        raise AssertionError(proc.stderr or proc.stdout)
    return proc.stdout.strip()


class InputValidationTests(unittest.TestCase):
    def test_accepts_supported_repository_names(self) -> None:
        self.assertEqual(
            MODULE.validate_repository("megvadulthangya/nvidia-470xx-utils", "nvidia-470xx-utils"),
            "megvadulthangya/nvidia-470xx-utils",
        )
        self.assertEqual(
            MODULE.validate_repository("megvadulthangya/nvidia-470xx", "nvidia-470xx"),
            "megvadulthangya/nvidia-470xx",
        )

    def test_rejects_wrong_repo_family(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.validate_repository("megvadulthangya/nvidia-390xx-utils", "nvidia-470xx-utils")

    def test_rejects_invalid_repository_syntax(self) -> None:
        for value in ("nvidia-470xx-utils", "owner/name/extra", "owner/../repo", "owner/name.git"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.validate_repository(value, "name")

    def test_accepts_branch_names_with_slashes(self) -> None:
        self.assertEqual(MODULE.validate_ref("feature/kernel-test", "branch"), "feature/kernel-test")

    def test_rejects_unsafe_ref_names(self) -> None:
        for value in ("", "-bad", "bad/", "a..b", "white space", r"bad\\ref", "name?bad"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                MODULE.validate_ref(value, "branch")

    def test_rejects_non_sha_before_creating_checkout(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "source"
            with self.assertRaises(ValueError):
                MODULE.checkout_exact_commit("https://example.invalid/repo.git", "main", "not-a-sha", target)
            self.assertFalse(target.exists())


class ExactCommitCheckoutTests(unittest.TestCase):
    def test_checks_out_event_sha_not_newer_branch_tip(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            work = root / "work"
            remote = root / "remote.git"
            checkout = root / "checkout"
            work.mkdir()
            git("init", "--quiet", "-b", "main", cwd=work)
            git("config", "user.name", "Test", cwd=work)
            git("config", "user.email", "test@example.invalid", cwd=work)
            (work / "file.txt").write_text("event commit\n", encoding="utf-8")
            git("add", "file.txt", cwd=work)
            git("commit", "--quiet", "-m", "event commit", cwd=work)
            event_sha = git("rev-parse", "HEAD", cwd=work)
            (work / "file.txt").write_text("newer branch tip\n", encoding="utf-8")
            git("commit", "--quiet", "-am", "newer commit", cwd=work)
            git("clone", "--quiet", "--bare", str(work), str(remote))

            MODULE.checkout_exact_commit(str(remote), "main", event_sha, checkout)

            self.assertEqual(git("rev-parse", "HEAD", cwd=checkout), event_sha)
            self.assertEqual((checkout / "file.txt").read_text(encoding="utf-8"), "event commit\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
