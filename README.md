# harvest-nvidia-logs

> Collect, normalize and summarize `make.log` files produced by DKMS
> when building legacy NVIDIA driver branches (340xx, 390xx, …) against
> multiple Manjaro kernels.

![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

If you maintain the `nvidia-340xx` / `nvidia-390xx` (or any other legacy
NVIDIA branch) packages on Manjaro and build them against a dozen
kernels at once, you know the pain: each build produces a `make.log` that
can be mutiple 10000+ lines long, of which **99 % is objtool noise** from the
driver's pre-built binary blobs (`ENDBR` relocation warnings, `naked
return` warnings, `missing int3 after ret`, etc.). Buried somewhere in
there is the one line that tells you why a build actually *failed*.

`harvest-nvidia-logs` walks your diag tree, finds every `make.log`,
splits the content into **errors / clean warnings / known noise**,
deduplicates and normalizes each warning into a stable signature, and
produces a single `INDEX.md` that tells you — at a glance — what to fix
first.

---

## Why

The script was born from a real workflow: maintaining
[`nvidia-340xx`](https://aur.archlinux.org/packages/?K=nvidia-340xx) and
`nvidia-390xx` legacy driver packages on Manjaro, rebuilt against every
current kernel (6.1, 6.6, 6.12, 7.x, plus RT variants). Every build
produces a `make.log` with tens of thousands of objtool warnings from
the NVIDIA kernel module, drowning out the few lines that matter.

Tools like [`buildlog-consultant`](https://github.com/jelmer/buildlog-consultant)
or OpenCanary extract the interesting bits from a *single* build log,
but none of them answer the question a packager really asks:

> *"I have 20 builds. Which warning, if fixed once, unblocks the most
> of them?"*

`harvest-nvidia-logs` answers exactly that.

---

## Features

- **Auto-discovery** — scans `<diag-root>/nvidia-*/{normal-kernels,rt-kernels}/`
  and picks up any new branch (`nvidia-470xx`, `nvidia-580xx`, …) with
  no code changes.
- **Noise filtering** — known objtool spam is separated into
  `03-noise.txt` and counted, never silently dropped.
- **Signature normalization** — every warning is reduced to a stable
  form: paths stripped, `symbol+0xHEX` collapsed to `<func>+0xADDR`,
  hex literals collapsed to `0xADDR`. This makes "the same warning
  across 20 builds" actually groupable.
- **Cross-build analysis** — the `INDEX.md` shows which signatures
  appear in more than one build (fix-first candidates) and which are
  unique to a single build (usually kernel-specific, low priority).
- **Not-built markers** — builds that failed before DKMS produced a
  log (e.g. only a `PKGBUILD` exists) get a zero-byte `Not-built`
  marker and a `summary.txt` explaining it.
- **Zero dependencies** — Python 3.10+ stdlib only. No `pip install`.
- **LLM-friendly output** — stable section names, Markdown tables,
  fenced code blocks. Works well when pasted into an LLM for triage.

---

## Requirements

- Python **3.10+** (uses `X | Y` type syntax; 3.8/3.9 users can adjust
  one line at the top of the file)
- A Unix-like system (Linux, macOS, WSL)
- A directory tree with NVIDIA driver builds, e.g.:

```
~/diag/
├── nvidia-340xx/
│   ├── normal-kernels/
│   │   ├── linux61-nvidia-340xx/
│   │   │   ├── src/nvidia/340.108/6.1.187-2-MANJARO/x86_64/log/make.log
│   │   │   └── PKGBUILD
│   │   └── linux66-nvidia-340xx/
│   │       └── ...
│   └── rt-kernels/
│       └── linux61-rt-nvidia-340xx/
│           └── ...
└── nvidia-390xx/
    ├── normal-kernels/
    └── rt-kernels/
```

The exact nesting under `src/` doesn't matter — the script uses
`rglob("make.log")` to find it.

---

## Installation

### Manual (recommended for now)

```bash
git clone https://github.com/<you>/harvest-nvidia-logs.git
cd harvest-nvidia-logs
sudo install -m 755 harvest-nvidia-logs /usr/local/bin/harvest-nvidia-logs
```

### Just run it in place

```bash
./harvest-nvidia-logs -d ~/diag
```

---

## Usage

```bash
# Default: scan ~/diag, write to ~/diag/harvest/
harvest-nvidia-logs

# Explicit diag root
harvest-nvidia-logs -d /home/gabi/diag

# Custom output location
harvest-nvidia-logs -d ~/diag -o /tmp/harvest

# Quiet mode (cron-friendly)
harvest-nvidia-logs -q

# Longer header excerpt per build (default: 10)
harvest-nvidia-logs -n 20

# Show help
harvest-nvidia-logs -h
```

| Flag | Env | Default | Meaning |
|------|-----|---------|---------|
| `-d`, `--diag-root` | `DIAG_ROOT` | `$HOME/diag` | Where to look for `nvidia-*` branches |
| `-o`, `--harvest-dir` | — | `<diag-root>/harvest` | Where to write the output |
| `-n`, `--header-lines` | — | `10` | Lines from top of each `make.log` to save |
| `-q`, `--quiet` | — | off | Suppress progress on stderr |

---

## Output

```
~/diag/harvest/
├── INDEX.md                        ← start here
├── 340xx/
│   ├── normal/
│   │   └── 6.1.187-2-MANJARO/
│   │       ├── 00-header.txt       ← first N lines of make.log
│   │       ├── 01-errors.txt       ← real errors only (0 bytes = OK)
│   │       ├── 02-warnings.txt     ← clean, dedup'd, counted
│   │       ├── 03-noise.txt        ← known objtool spam, counted
│   │       └── summary.txt
│   └── rt/
│       └── 6.1.182-1-rt67-MANJARO/
│           └── ...
└── 390xx/
    ├── normal/
    └── rt/
        └── linux66-rt-nvidia-390xx/
            ├── Not-built           ← empty, marker only
            └── summary.txt         ← explains why
```

### `INDEX.md` — the only file you need to open

Sections, in order:

1. **Overview** — branch list, build counts by status, signature counts.
2. **Legend** — symbol reference.
3. **Status table** — one row per build, sortable by eye.
4. **❗ Failures** — errors from `01-errors.txt`, 15-line excerpt each.
5. **🔁 Cross-build signatures** — warnings seen in **more than one**
   build, sorted by number of affected builds. **This is the "fix
   this first" list.**
6. **🧩 Unique to one build** — kernel- or config-specific warnings,
   usually not worth chasing.
7. **🚫 Not built** — builds with no `make.log` at all.

---

## How the noise filtering works

A raw warning line like:

```
/home/testelek/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/nvidia.o: warning: objtool: .rodata+0x9e38: data relocation to !ENDBR: _nv023101rm+0x0
```

is normalized to:

```
warning: objtool: .rodata+0xADDR: data relocation to !ENDBR: <func>+0xADDR
```

Rules applied, in order:

1. Everything before `warning:` is dropped (path prefix).
2. Anything in single quotes is replaced with `'<path>'`
   (fixes `Module.symvers` warnings, which otherwise differ per build).
3. Any `symbol+0xHEX` becomes `<func>+0xADDR`.
4. Any remaining `0xHEX` becomes `0xADDR`.

After normalization, lines matching one of the `NOISE_PATTERNS` regexes
(see top of the script) are moved to `03-noise.txt`. Everything else
lands in `02-warnings.txt`. Both are `Counter`-counted and sorted by
frequency.

To add a new noise pattern, edit `NOISE_PATTERNS` at the top of the
script. Patterns are matched against the *normalized* signature.

---

## What "cross-build signature" means

If a normalized warning signature appears in N > 1 different builds,
it's a **cross-build signature**. Fixing it (once) benefits N builds.

The `INDEX.md` sorts these by N descending. Typical output for the
`nvidia-390xx` branch across 7 kernels:

```
| # | Builds | Hits  | Signature                                                       |
|---|-------:|------:|-----------------------------------------------------------------|
| 1 | 10     | 65375 | warning: objtool: <func>+0xADDR: relocation to !ENDBR: ...      |
| 2 | 6      | 39714 | warning: objtool: <func>+0xADDR: 'naked' return found in ...    |
| 3 | 2      | 39714 | warning: objtool: <func>+0xADDR: missing int3 after ret         |
```

A fix in the driver source that silences signature #1 clears ~65 000
lines of noise from every one of the 10 builds at once.

---

## Customization

- **Noise patterns**: edit `NOISE_PATTERNS` (list of compiled regexes).
- **Default diag root**: change `DEFAULT_DIAG_ROOT` in the script, or
  set `DIAG_ROOT` in your shell.
- **Different driver branches**: nothing to do — any `nvidia-*`
  directory under the diag root is picked up automatically.

If you want the harvest to also work on **non-NVIDIA** kernel module
builds, the only NVIDIA-specific parts are the branch naming convention
(`nvidia-*`) and the noise patterns. Both are trivial to generalize.

---

## Limitations

- **NVIDIA-oriented noise list.** The default patterns target the
  objtool warnings produced by the legacy 340xx / 390xx binary blobs.
  Other drivers will produce different noise — add patterns as needed.
- **Regex-only matching.** A warning signature is a string, not an
  AST. Two semantically identical warnings with different wording will
  appear as two signatures.
- **No build orchestration.** The tool only analyzes logs that already
  exist. It does not run DKMS or `makepkg`.

---

## Roadmap

- [ ] Optional JSON output (`--json`) for programmatic consumption
- [ ] `--diff` mode: compare the current harvest against a previous one
- [ ] Config file (`~/.config/harvest-nvidia-logs.toml`) for noise
      patterns and per-branch rules
- [ ] Packaged as `harvest-nvidia-logs` AUR package

---

## Contributing

Issues and PRs welcome. If you maintain a different legacy NVIDIA
branch (470xx, 580xx) and want to contribute noise patterns, open a
PR with a sample `make.log` snippet in the description.

---

## License

MIT — see `LICENSE`.

---

## Magyar összefoglaló

A `harvest-nvidia-logs` egy Python script, ami a Manjaro alatt
buildelt **NVIDIA legacy driver** (340xx, 390xx, …) DKMS
`make.log` fájljait dolgozza fel. Végigjárja a `~/diag/nvidia-*/`
mappát, minden kernel buildhez szétválogatja a logot:

- **`01-errors.txt`** — tényleges hibák (üres = sikeres build)
- **`02-warnings.txt`** — valódi, javítandó warningok (dedupolva)
- **`03-noise.txt`** — ismert objtool zaj (ENDBR, naked return, stb.)
- **`00-header.txt`** — az első pár sor a logból
- **`summary.txt`** — build-szintű összefoglaló

Végül generál egy **`INDEX.md`-t**, ami az összes buildet egy fájlban
mutatja: státusz táblázat, bukott buildek, cross-build signature-ök
(fix-first sorrendben), és egyedi warningok. Ezt a fájlt elég
megnyitni — nem kell a 100 külön mappát böngészni.

Telepítés: `sudo install -m 755 harvest-nvidia-logs /usr/local/bin/`
Használat: `harvest-nvidia-logs` (opcionálisan `-d`, `-o`, `-q`, `-n`)
