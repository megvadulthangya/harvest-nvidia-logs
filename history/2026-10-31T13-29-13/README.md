# Harvest Index — 2026-10-31 13:29:13 

## TL;DR

- **State:** ❗4 failed · 🔍0 suspicious · ⚠6 warnings · ✅10 clean · 🚫2 not-built
- **⚠ Integrity issues:** 1 build(s) affected — see `## 🧱 Integrity issues` below
- **Action needed (1):**
    - 2 builds · 8 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
- **Informational:** 2 build-system signature(s) — no driver fix needed

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 22 — ❗4 failed, 🔍0 suspicious, ⚠6 warn, ✅10 clean, 🚫2 not-built
- **Warning signatures:** 5 total — 1 actionable across multiple builds, 2 informational, 2 unique to one build
- **Suspicious signatures:** 4  ·  **integrity issues:** 1 builds  ·  **integrity notes:** 0 builds

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

The raw `make.log` is also archived in every build directory as `make.log.zst` (or `.gz` / plain).

## Status table

| # | Branch | Variant | Kernel | Driver | Status | Err | Clean (uniq/total) | Susp | Noise | Integ |
|---|--------|---------|--------|--------|:------:|----:|-------------------:|-----:|------:|:-----:|
| 1 | 340xx | normal | 6.1.191-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.115-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 3 | 340xx | normal | 6.6.161-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 4 | 340xx | normal | linux-next-nvidia-340xx | — | ❗ failed | 5 | 2 / 2 | 0 | 0 | ! |
| 5 | 340xx | normal | linux618-nvidia-340xx | — | ❗ failed | 12 | 0 / 0 | 30 | 0 |  |
| 6 | 340xx | normal | linux71-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 7 | 340xx | normal | linux72-nvidia-340xx | — | ❗ failed | 12 | 0 / 0 | 26 | 0 |  |
| 8 | 340xx | normal | linux73-nvidia-340xx | — | ❗ failed | 12 | 0 / 0 | 27 | 0 |  |
| 9 | 340xx | rt | 6.1.190-1-rt70-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 10 | 340xx | rt | 6.12.111-1-rt21-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 11 | 340xx | rt | 6.6.159-1-rt82-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 12 | 390xx | normal | 6.1.191-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 13 | 390xx | normal | 6.12.115-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.18.60-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 15 | 390xx | normal | 6.6.161-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.2.14-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 17 | 390xx | normal | 7.3.0-next-20261027-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 18 | 390xx | normal | 7.3.1-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 19 | 390xx | normal | linux71-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 20 | 390xx | rt | 6.1.190-1-rt70-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 21 | 390xx | rt | 6.12.111-1-rt21-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 22 | 390xx | rt | 6.6.159-1-rt82-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |

## 🧱 Integrity issues

Structural problems detected between the **log** and the **build tree** — these likely indicate a silent failure.

### 340xx / normal / linux-next-nvidia-340xx

Path: `340xx/normal/linux-next-nvidia-340xx`  ·  modules on disk: 0 [—]  ·  log LD [M]: ['nvidia', 'nvidia-uvm']

- log claims to link modules ['nvidia', 'nvidia-uvm'] but no matching .ko/.ko.zst found on disk

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 340xx / normal / linux-next-nvidia-340xx — ?  (5 errors)

Path: `340xx/normal/linux-next-nvidia-340xx`

```
477: make[4]: *** [/usr/lib/modules/7.3.0-next-20261027-1-MANJARO/build/scripts/Makefile.modpost:147: Module.symvers] Error 1
478: make[3]: *** [/usr/lib/modules/7.3.0-next-20261027-1-MANJARO/build/Makefile:2194: modpost] Error 2
479: make[2]: *** [/usr/lib/modules/7.3.0-next-20261027-1-MANJARO/build/Makefile:248: __sub-make] Error 2
481: make[1]: *** [Makefile:248: __sub-make] Error 2
483: make: *** [Makefile:223: nvidia-uvm.ko] Error 2
```

### 340xx / normal / linux618-nvidia-340xx — ?  (12 errors)

Path: `340xx/normal/linux618-nvidia-340xx`

```
231: nv-mmap.c:479:6: error: redefinition of ‘nv_vma_start_write’
237: make[4]: *** [/usr/lib/modules/6.18.60-1-MANJARO/build/scripts/Makefile.build:287: nv-mmap.o] Error 1
239: make[3]: *** [/usr/lib/modules/6.18.60-1-MANJARO/build/Makefile:2050: .] Error 2
240: make[2]: *** [/usr/lib/modules/6.18.60-1-MANJARO/build/Makefile:248: __sub-make] Error 2
242: make[1]: *** [Makefile:248: __sub-make] Error 2
244: make: *** [Makefile:224: nvidia.ko] Error 2
291: make[5]: *** No rule to make target 'Makefile'.  Stop.
292: make[4]: *** [/usr/lib/modules/6.18.60-1-MANJARO/build/Makefile:2050: .] Error 2
293: make[3]: *** [/usr/lib/modules/6.18.60-1-MANJARO/build/Makefile:248: __sub-make] Error 2
295: make[2]: *** [Makefile:248: __sub-make] Error 2
297: make[1]: *** [Makefile:224: nvidia.ko] Error 2
299: make: *** [Makefile:226: ../Module.symvers] Error 2
```

### 340xx / normal / linux72-nvidia-340xx — ?  (12 errors)

Path: `340xx/normal/linux72-nvidia-340xx`

```
231: nv-mmap.c:479:6: error: redefinition of ‘nv_vma_start_write’
237: make[4]: *** [/usr/lib/modules/7.2.14-1-MANJARO/build/scripts/Makefile.build:289: nv-mmap.o] Error 1
239: make[3]: *** [/usr/lib/modules/7.2.14-1-MANJARO/build/Makefile:2198: .] Error 2
240: make[2]: *** [/usr/lib/modules/7.2.14-1-MANJARO/build/Makefile:248: __sub-make] Error 2
242: make[1]: *** [Makefile:248: __sub-make] Error 2
244: make: *** [Makefile:224: nvidia.ko] Error 2
287: make[5]: *** No rule to make target 'Makefile'.  Stop.
288: make[4]: *** [/usr/lib/modules/7.2.14-1-MANJARO/build/Makefile:2198: .] Error 2
289: make[3]: *** [/usr/lib/modules/7.2.14-1-MANJARO/build/Makefile:248: __sub-make] Error 2
291: make[2]: *** [Makefile:248: __sub-make] Error 2
293: make[1]: *** [Makefile:224: nvidia.ko] Error 2
295: make: *** [Makefile:226: ../Module.symvers] Error 2
```

### 340xx / normal / linux73-nvidia-340xx — ?  (12 errors)

Path: `340xx/normal/linux73-nvidia-340xx`

```
231: nv-mmap.c:479:6: error: redefinition of ‘nv_vma_start_write’
237: make[4]: *** [/usr/lib/modules/7.3.1-1-MANJARO/build/scripts/Makefile.build:290: nv-mmap.o] Error 1
239: make[3]: *** [/usr/lib/modules/7.3.1-1-MANJARO/build/Makefile:2229: .] Error 2
240: make[2]: *** [/usr/lib/modules/7.3.1-1-MANJARO/build/Makefile:248: __sub-make] Error 2
242: make[1]: *** [Makefile:248: __sub-make] Error 2
244: make: *** [Makefile:224: nvidia.ko] Error 2
288: make[5]: *** No rule to make target 'Makefile'.  Stop.
289: make[4]: *** [/usr/lib/modules/7.3.1-1-MANJARO/build/Makefile:2229: .] Error 2
290: make[3]: *** [/usr/lib/modules/7.3.1-1-MANJARO/build/Makefile:248: __sub-make] Error 2
292: make[2]: *** [Makefile:248: __sub-make] Error 2
294: make[1]: *** [Makefile:224: nvidia.ko] Error 2
296: make: *** [Makefile:226: ../Module.symvers] Error 2
```

## 🔍 Suspicious signatures

Lines that are **not** errors and **not** warnings, but contain keywords that often indicate real problems (missing files, permissions, OOM, crashes, missing deps).

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 3 | 80 | `mkdir: cannot create directory '.tmp_NNN': Permission denied` | 340xx/normal |
| 2 | 1 | 1 | `/usr/lib/modules/6.18.60-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory` | 340xx/normal |
| 3 | 1 | 1 | `/usr/lib/modules/7.2.14-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory` | 340xx/normal |
| 4 | 1 | 1 | `/usr/lib/modules/7.3.1-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |

<details><summary>Context excerpts (first few hits per signature)</summary>

**`mkdir: cannot create directory '.tmp_NNN': Permission denied`**

```
[340xx/normal/linux618-nvidia-340xx] 260: mkdir: cannot create directory ‘.tmp_87667’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 261: mkdir: cannot create directory ‘.tmp_87670’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 262: mkdir: cannot create directory ‘.tmp_87673’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 263: mkdir: cannot create directory ‘.tmp_87676’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 264: mkdir: cannot create directory ‘.tmp_87679’: Permission denied
```

**`/usr/lib/modules/6.18.60-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory`**

```
[340xx/normal/linux618-nvidia-340xx] 260: mkdir: cannot create directory ‘.tmp_87667’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 261: mkdir: cannot create directory ‘.tmp_87670’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 262: mkdir: cannot create directory ‘.tmp_87673’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 263: mkdir: cannot create directory ‘.tmp_87676’: Permission denied
[340xx/normal/linux618-nvidia-340xx] 264: mkdir: cannot create directory ‘.tmp_87679’: Permission denied
```

**`/usr/lib/modules/7.2.14-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory`**

```
[340xx/normal/linux72-nvidia-340xx] 260: mkdir: cannot create directory ‘.tmp_120152’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 261: mkdir: cannot create directory ‘.tmp_120155’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 262: mkdir: cannot create directory ‘.tmp_120158’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 263: mkdir: cannot create directory ‘.tmp_120161’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 264: mkdir: cannot create directory ‘.tmp_120164’: Permission denied
```

**`/usr/lib/modules/7.3.1-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux73-nvidia-340xx] 260: mkdir: cannot create directory ‘.tmp_128294’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 261: mkdir: cannot create directory ‘.tmp_128297’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 262: mkdir: cannot create directory ‘.tmp_128300’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 263: mkdir: cannot create directory ‘.tmp_128303’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 264: mkdir: cannot create directory ‘.tmp_128306’: Permission denied
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

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

| Build | Hits | Signature |
|-------|-----:|-----------|
| 340xx/normal/linux-next-nvidia-340xx | 1 | `warning: ignoring old recipe for target 'Module.symvers'` |
| 340xx/normal/linux-next-nvidia-340xx | 1 | `warning: overriding recipe for target 'Module.symvers'` |

## 🚫 Not built (no make.log)

- `340xx / normal / linux71-nvidia-340xx`
- `390xx / normal / linux71-nvidia-390xx`

---
_End of index. Per-build detail files live in the harvest tree._
