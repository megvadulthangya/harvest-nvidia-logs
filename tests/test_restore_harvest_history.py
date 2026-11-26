#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "restore_harvest_history.py"
SPEC = importlib.util.spec_from_file_location("restore_harvest_history", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RestoreHistoryTests(unittest.TestCase):
    def test_restores_history_and_changelog_but_not_current_readme(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            previous = root / "previous"
            harvest = root / "harvest"
            (previous / "history" / "2026-11-01T10-00-00").mkdir(parents=True)
            (previous / "history" / "2026-11-01T10-00-00" / "state.json").write_text(
                '{"timestamp":"old"}\n', encoding="utf-8"
            )
            (previous / "driver-changelog.md").write_text("old changelog\n", encoding="utf-8")
            (previous / "README.md").write_text("old report\n", encoding="utf-8")
            harvest.mkdir()
            (harvest / "README.md").write_text("current report\n", encoding="utf-8")

            restored = MODULE.restore_from_directory(previous, harvest)

            self.assertEqual(restored, ["history", "driver-changelog.md"])
            self.assertTrue((harvest / "history" / "2026-11-01T10-00-00" / "state.json").is_file())
            self.assertEqual((harvest / "driver-changelog.md").read_text(), "old changelog\n")
            self.assertEqual((harvest / "README.md").read_text(), "current report\n")

    def test_replaces_existing_history_instead_of_merging_stale_snapshots(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            previous = root / "previous"
            harvest = root / "harvest"
            (previous / "history" / "new-snapshot").mkdir(parents=True)
            (previous / "history" / "new-snapshot" / "state.json").write_text("new")
            (harvest / "history" / "stale-snapshot").mkdir(parents=True)
            (harvest / "history" / "stale-snapshot" / "state.json").write_text("stale")

            MODULE.restore_from_directory(previous, harvest)

            self.assertTrue((harvest / "history" / "new-snapshot" / "state.json").exists())
            self.assertFalse((harvest / "history" / "stale-snapshot").exists())

    def test_missing_persistent_files_is_a_clean_first_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            previous = root / "empty-previous"
            previous.mkdir()
            harvest = root / "harvest"

            restored = MODULE.restore_from_directory(previous, harvest)

            self.assertEqual(restored, [])
            self.assertTrue(harvest.is_dir())


if __name__ == "__main__":
    unittest.main(verbosity=2)
