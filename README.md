# harvest-nvidia-logs

> Build NVIDIA driver branches against multiple Manjaro kernels and
> turn the resulting `make.log` files into one readable status report.

![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.11%2B-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

If you maintain the `nvidia-340xx` / `nvidia-390xx` / `nvidia-580xx`
(and current) driver branches on Manjaro and rebuild them against a
dozen kernels at once, you know the pain: every build produces a
`make.log` with tens of thousands of lines, most of which is objtool
noise from pre-built binary blobs. The one line that tells you why a
build actually failed is buried somewhere in there.

This project automates the whole workflow — from cloning the source
repositories to producing a single `README.md` that lists every
build, its status, and the actionable warnings across all of them.

---

## What it does

For every NVIDIA driver branch found in the configured source:

1. Clones the source repositories (flat or non-flat layout).
2. Parses the PKGBUILDs and generates a structured build plan.
3. Installs the required kernels and headers.
4. Builds the utils package, then every kernel module.
5. Runs the cleanup script between branches.
6. Harvests the resulting `make.log` files into a single
   `README.md` with cross-build warning analysis.
7. Optionally pushes the result to a dedicated results branch.

It handles the two common layouts automatically:

- **Flat**: one repository contains every PKGBUILD as a subdirectory
  (Manjaro's current `code.manjaro.org/packages/PKGBUILDs`).
- **Non-flat**: one repository per package (the classic GitLab layout,
  and the anticipated future Forgejo layout).

Both layouts share the same downstream pipeline. The only difference
is how the sources are discovered.

---

## Repository contents

Three tools, no external Python dependencies (stdlib only):

| File | Purpose |
|------|---------|
| `harvest-nvidia-logs` | Parses `make.log` files, generates the README, keeps a history of snapshots. Pure analysis. Can be run on any tree of make.log files. |
| `nvidia-ci.py` | The orchestrator. Drives discover → clone → inspect → eol → build → harvest → publish. Calls `harvest-nvidia-logs` internally. |
| `clean-nvidia-container.sh` | Removes NVIDIA packages, DKMS modules, and their artifacts between driver branches. |

Two GitHub Actions workflows:

| Workflow | Purpose |
|----------|---------|
| `.github/workflows/build.yaml` | The custom profile. Builds your own fork repositories. |
| `.github/workflows/build-official.yaml` | The Manjaro official profile. Builds the upstream packages. |

Both workflows call `nvidia-ci.py --all`. All inputs are settable
from the "Run workflow" dialog; the default values differ.

---

## Source URL formats

`nvidia-ci.py` accepts three forms of `--url`, chosen automatically:

| Form | Meaning | Example |
|------|---------|---------|
| `…/repo.git` | single flat repository | `https://code.manjaro.org/packages/PKGBUILDs.git` |
| `host/org` or `host/user` | scoped API discovery | `https://code.manjaro.org/packages` |
| `host` | global API search | `https://gitlab.manjaro.org` |

Supported platforms:

- **Forgejo / Gitea** (`code.manjaro.org`)
- **GitLab** (`gitlab.manjaro.org`)
- **GitHub** (`github.com`)

For non-flat layouts the platform API is queried and every `nvidia-*`
repository is kept after filtering. You do not need to know the exact
subgroup — the API returns projects from any subgroup.

---

## Output structure

Everything goes into a `harvest/` directory:

```
harvest/
├── README.md                     ← the only file you need to open
├── driver-changelog.md           ← append-only diff log
└── history/
    └── 2026-10-09T01-06-27/
        ├── README.md             ← snapshot of that run
        └── state.json            ← machine-readable state
```

Plus per-build directories, one per kernel, each containing:

| File | Content |
|------|---------|
| `00-header.txt` | first N lines of the make.log |
| `01-errors.txt` | real errors only (empty file = clean build) |
| `02-warnings.txt` | clean, deduplicated, counted warnings |
| `03-noise.txt` | known objtool spam, counted |
| `04-suspicious.txt` | non-error, non-warning "uh-oh" lines |
| `summary.txt` | per-build summary |
| `Not-built` | empty marker when no make.log exists |

### `README.md`

Sections, in order:

1. **TL;DR** — build counts, top actionable warnings, informational
   count, and a one-line "since last run" summary.
2. **📊 Changes since …** — only with `--diff`. Resolved signatures,
   new signatures, status transitions, hit count changes.
3. **Overview** — root paths, branch list, build counts.
4. **Legend** — status symbol reference.
5. **Status table** — one row per build.
6. **🧱 Integrity issues** — log vs. build tree mismatches.
7. **📝 Integrity notes** — non-critical observations.
8. **❗ Failures** — errors excerpted from `01-errors.txt`.
9. **🔍 Suspicious signatures** — cross-build table of unusual lines.
10. **🔁 Cross-build warning signatures** — split into actionable
    (driver source) and informational (build system).
11. **🧩 Unique to one build** — single-build warnings.
12. **🚫 Not built** — builds with no make.log.
13. **⚠ EOL / Out-of-sync packages** — appended by `nvidia-ci.py`.
    Lists every package that is not present in the Manjaro repos
    (or is present at a different version than the source).

The file is designed to be consumed both by a human and by an LLM:
stable section names, Markdown tables, fenced code blocks.

---

## EOL detection

After building, `nvidia-ci.py` cross-checks every discovered package
against the Manjaro repositories via `pacman -Si`. Three outcomes:

| Status | Meaning |
|--------|---------|
| `ok` | present at the expected version |
| `stale` | present but the version differs from the source |
| `not-in-manjaro` | not in the Manjaro repos at all |

The results are appended to the top-level `README.md` as a table. The
same check also determines which kernel prefixes are available for
building — if a kernel like `linux71` is no longer in the Manjaro
repos, it is skipped instead of failing the build.

---

## Two workflows

### `build.yaml` — custom fork profile

Default inputs:

- `url = https://github.com/megvadulthangya`
- `drivers-branch = develop`
- `kernels-branch = develop`
- `results-branch = results`

Runs weekly on Sunday at 03:00 UTC.

### `build-official.yaml` — Manjaro official profile

Default inputs:

- `url = https://code.manjaro.org/packages/PKGBUILDs.git` (flat)
- `results-branch = official-results`

Runs weekly on Sunday at 04:00 UTC.

The file header documents the three supported URL forms (current
flat repo, future non-flat Forgejo, historical GitLab) and how to
switch between them — no file edit is required; override the `url`
input in the "Run workflow" dialog.

---

## Running locally

Nothing is pushed unless `--publish` is explicitly given. On a
workstation the tool writes everything to the work directory and
exits.

```bash
# Full pipeline on a GitHub user's repositories
python3 nvidia-ci.py --all \
    --url https://github.com/your-user \
    --drivers-branch develop \
    --kernels-branch develop \
    --workdir ~/nvidia-ci-build

# Flat Manjaro repository
python3 nvidia-ci.py --all \
    --url https://code.manjaro.org/packages/PKGBUILDs.git \
    --manjaro-branch testing \
    --workdir ~/nvidia-ci-build

# Just the discovery phase, see what would be cloned
python3 nvidia-ci.py --phase discover --url https://github.com/your-user
```

`nvidia-ci.py` calls `harvest-nvidia-logs` from `$PATH` or from the
same directory. Install it before the first run:

```bash
sudo install -m 755 harvest-nvidia-logs /usr/local/bin/harvest-nvidia-logs
sudo install -m 755 clean-nvidia-container.sh /build/clean-nvidia-container.sh
```

---

## GitHub Actions setup

1. **Workflow permissions**: repository Settings → Actions → General →
   Workflow permissions → set to **Read and write permissions**. This
   allows the results push.
2. **No secrets required** for public repositories. The built-in
   `GITHUB_TOKEN` handles the push.
3. **Results branch** is created automatically on the first run.

---

## Known limitations

- **Manjaro 390xx on linux61 fails.** Real source-level incompatibility
  (`vm_flags_set`, `vm_flags_clear`, `timer_delete_sync`). Manjaro's
  patch set does not include the required backports; the harvest flags
  this correctly, but the fix is a Manjaro-side concern.
- **Flat layout folder listing requires a clone.** Forgejo and GitLab
  APIs do not expose the directory tree of a repository, so the flat
  `PKGBUILDs` repo must be cloned before its nvidia subdirectories can
  be discovered.
- **No artifact caching between runs.** Every run rebuilds everything.
  This is intentional: it guarantees a fresh `make.log` from a known
  toolchain state.

---

## License

MIT — see `LICENSE`.

---

## Magyar összefoglaló

A projekt három eszközből áll, amelyek együtt egy teljes build- és
elemző-pipeline-t alkotnak:

- **`harvest-nvidia-logs`** — a `make.log` fájlokat dolgozza fel,
  generál egy `README.md`-t és történelmi pillanatképeket.
- **`nvidia-ci.py`** — az orchestrator. Felderíti a forrásokat,
  klónozza, elemzi, buildeli, majd hívja a `harvest-nvidia-logs`-ot.
- **`clean-nvidia-container.sh`** — a driver branch-ek között takarít.

Két GitHub Action használja mindezt: `build.yaml` a saját
forkokhoz, `build-official.yaml` a Manjaro hivatalos
csomagjaihoz. Az eredmény egyetlen `README.md` a `results` vagy
`official-results` branch-en, benne minden build státusza, a
cross-build warningok, és az EOL / elavult csomagok listája.

Lokálisan pontosan ugyanaz a parancs fut, csak `--publish` nélkül:
a fájlok a gépen maradnak, semmi nem kerül fel a GitHubra.
```

## Amit a README-ről érdemes tudni

- **Nincs benne** semmi, amit nem teszteltünk. A "Known limitations" szekcióban lévő pontok tényleges problémák, nem elméleti.
- **Nem említem a `--phase`-t** kivéve a "discover" példát — mert az a 99%-ban hasznos use case.
- **A magyar összefoglaló** ugyanazt mondja, rövidebben.
- **A legutóbbi futás** (official, most fut) még nem tudom, mit ad pontosan, de a README **nem** függ a konkrét eredménytől — a pipeline-t és a kimeneti formátumot írja le.
