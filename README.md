# Harvest Index — 2026-11-08 10:47:19 

## TL;DR

- **State:** ❗1 failed · 🔍0 suspicious · ⚠9 warnings · ✅10 clean · 🚫2 not-built
- **⚠ Integrity issues:** 1 build(s) affected — see `## 🧱 Integrity issues` below
- **Action needed (1):**
    - 2 builds · 8 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
- **Informational:** 4 build-system signature(s) — no driver fix needed

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 22 — ❗1 failed, 🔍0 suspicious, ⚠9 warn, ✅10 clean, 🚫2 not-built
- **Warning signatures:** 5 total — 1 actionable across multiple builds, 4 informational, 0 unique to one build
- **Suspicious signatures:** 2  ·  **integrity issues:** 1 builds  ·  **integrity notes:** 0 builds

## Legend

| Symbol | Status | Meaning |
|:------:|--------|---------|
| ❗ | failed     | make.log contains real errors — **blocker** |
| 🔍 | suspicious | no errors, but suspicious lines or integrity issues |
| ⚠  | warnings   | built, no errors, non-noise warnings to review |
| ✅ | clean      | built, no errors, only known noise |
| 🚫 | not-built  | no make.log at all |
| 🧪 | utils      | userspace utils failure, mpatch debug archived |

Per-build detail lives in the harvest tree, one directory per kernel: `00-header.txt`, `01-errors.txt`, `02-warnings.txt`, `03-noise.txt`, `04-suspicious.txt`, `summary.txt`.

For non-clean builds (warnings, suspicious, failures), the raw `make.log` is archived in the same directory as `make.log.zst` (or `.gz` / plain).

## Status table

| # | Branch | Variant | Kernel | Driver | Status | Err | Clean (uniq/total) | Susp | Noise | Integ |
|---|--------|---------|--------|--------|:------:|----:|-------------------:|-----:|------:|:-----:|
| 1 | 340xx | normal | 6.1.191-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.115-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.60-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.161-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 5 | 340xx | normal | 7.2.14-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 0 |  |
| 6 | 340xx | normal | 7.3.1-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 0 |  |
| 7 | 340xx | normal | linux-next-nvidia-340xx | — | ❗ failed | 11 | 0 / 0 | 3 | 0 | ! |
| 8 | 340xx | normal | linux71-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 9 | 340xx | rt | 6.1.190-1-rt70-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 10 | 340xx | rt | 6.12.111-1-rt21-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 11 | 340xx | rt | 6.6.159-1-rt82-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 12 | 390xx | normal | 6.1.191-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164940 |  |
| 13 | 390xx | normal | 6.12.115-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.18.60-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 15 | 390xx | normal | 6.6.161-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.2.14-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 17 | 390xx | normal | 7.3.1-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 18 | 390xx | normal | 7.4.0-rc1-next-20261105-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 19 | 390xx | normal | linux71-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 20 | 390xx | rt | 6.1.190-1-rt70-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 21 | 390xx | rt | 6.12.111-1-rt21-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 22 | 390xx | rt | 6.6.159-1-rt82-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |

## 🧱 Integrity issues

Structural problems detected between the **log** and the **build tree** — these likely indicate a silent failure.

### 340xx / normal / linux-next-nvidia-340xx

Path: `340xx/normal/linux-next-nvidia-340xx`  ·  modules on disk: 0 [—]  ·  log LD [M]: ['nvidia']

- log claims to link modules ['nvidia'] but no matching .ko/.ko.zst found on disk

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 340xx / normal / linux-next-nvidia-340xx — ?  (11 errors)

Path: `340xx/normal/linux-next-nvidia-340xx`

```
268: make[4]: *** [/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/scripts/Makefile.modpost:147: Module.symvers] Error 1
269: make[3]: *** [/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/Makefile:2188: modpost] Error 2
270: make[2]: *** [/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/Makefile:248: __sub-make] Error 2
272: make[1]: *** [Makefile:248: __sub-make] Error 2
274: make: *** [Makefile:224: nvidia.ko] Error 2
295: make[5]: *** No rule to make target 'Makefile'.  Stop.
296: make[4]: *** [/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/Makefile:2261: .] Error 2
297: make[3]: *** [/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/Makefile:248: __sub-make] Error 2
299: make[2]: *** [Makefile:248: __sub-make] Error 2
301: make[1]: *** [Makefile:224: nvidia.ko] Error 2
303: make: *** [Makefile:226: ../Module.symvers] Error 2
```

## 🔍 Suspicious signatures

Lines that are **not** errors and **not** warnings, but contain keywords that often indicate real problems (missing files, permissions, OOM, crashes, missing deps).

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 1 | 2 | `mkdir: cannot create directory '.tmp_NNN': Permission denied` | 340xx/normal |
| 2 | 1 | 1 | `/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |

<details><summary>Context excerpts (first few hits per signature)</summary>

**`mkdir: cannot create directory '.tmp_NNN': Permission denied`**

```
[340xx/normal/linux-next-nvidia-340xx] 290: mkdir: cannot create directory ‘.tmp_25407’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 291: mkdir: cannot create directory ‘.tmp_25410’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 294: /usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
```

**`/usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux-next-nvidia-340xx] 290: mkdir: cannot create directory ‘.tmp_25407’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 291: mkdir: cannot create directory ‘.tmp_25410’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 294: /usr/lib/modules/7.4.0-rc1-next-20261105-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
```

</details>

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 2 | 8 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt |

### ⚙️ Informational (build system / Makefile)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 6 | 6 | `warning: ignoring old recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 2 | 6 | 6 | `warning: overriding recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 3 | 3 | 3 | `warning: ignoring old recipe for target 'Module.symvers'` | 340xx/normal |
| 4 | 3 | 3 | `warning: overriding recipe for target 'Module.symvers'` | 340xx/normal |

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

## 🚫 Not built (no make.log)

- `340xx / normal / linux71-nvidia-340xx`
- `390xx / normal / linux71-nvidia-390xx`

---
_End of index. Per-build detail files live in the harvest tree._

## ⚠ EOL / Out-of-sync packages

| Package | Repo version | Manjaro version | Status |
|---------|--------------|-----------------|--------|
| `linux71` | — | — | not-in-manjaro |

