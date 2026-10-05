# Harvest Index — 2026-10-04 22:02:21 

## 📊 Changes since 2026-10-04T18-19-46

### ✅ Resolved signatures (0)

_None._

### 🆕 New signatures (0)

_None._

### 🔀 Status changes (0)

_None._


## Overview

- **Diag root:** `/build/diag`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 20 — ❗12 failed, 🔍0 suspicious, ⚠8 warn, ✅0 clean, 🚫0 not-built
- **Warning signatures:** 8 total — 8 across multiple builds, 0 unique to one build
- **Suspicious signatures:** 53  ·  **integrity issues:** 0 builds  ·  **integrity notes:** 0 builds

## Legend

| Symbol | Status | Meaning |
|:------:|--------|---------|
| ❗ | failed     | make.log contains real errors — **blocker** |
| 🔍 | suspicious | no errors, but suspicious lines or integrity issues |
| ⚠  | warnings   | built, no errors, non-noise warnings to review |
| ✅ | clean      | built, no errors, only known noise |
| 🚫 | not-built  | no make.log at all |

Per-build detail lives in the harvest tree, one directory per kernel: `00-header.txt`, `01-errors.txt`, `02-warnings.txt`, `03-noise.txt`, `04-suspicious.txt`, `summary.txt`.

## Status table

| # | Branch | Variant | Kernel | Driver | Status | Err | Clean (uniq/total) | Susp | Noise | Integ |
|---|--------|---------|--------|--------|:------:|----:|-------------------:|-----:|------:|:-----:|
| 1 | 340xx | normal | 6.1.187-2-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 4 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.109-1-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 8 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.50-1-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 5 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.156-2-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 8 | 0 | 1 |  |
| 5 | 340xx | normal | 7.1.13-2-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 5 | 0 | 0 |  |
| 6 | 340xx | normal | linux72-nvidia-340xx | - | ❗ failed | 48 | 2 / 10 | 26 | 0 |  |
| 7 | 340xx | normal | linux73-nvidia-340xx | - | ❗ failed | 47 | 2 / 10 | 27 | 0 |  |
| 8 | 340xx | rt | 6.1.182-1-rt67-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 4 | 0 | 1 |  |
| 9 | 340xx | rt | 6.12.100-1-rt20-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 8 | 0 | 1 |  |
| 10 | 340xx | rt | 6.6.151-1-rt78-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 8 | 0 | 1 |  |
| 11 | 390xx | normal | linux61-nvidia-390xx | - | ❗ failed | 3 | 1 / 1 | 0 | 0 |  |
| 12 | 390xx | normal | linux612-nvidia-390xx | - | ❗ failed | 4 | 1 / 1 | 0 | 0 |  |
| 13 | 390xx | normal | linux618-nvidia-390xx | - | ❗ failed | 5 | 1 / 1 | 0 | 0 |  |
| 14 | 390xx | normal | linux66-nvidia-390xx | - | ❗ failed | 4 | 1 / 1 | 0 | 0 |  |
| 15 | 390xx | normal | linux71-nvidia-390xx | - | ❗ failed | 5 | 1 / 1 | 0 | 0 |  |
| 16 | 390xx | normal | linux72-nvidia-390xx | - | ❗ failed | 5 | 1 / 1 | 0 | 0 |  |
| 17 | 390xx | normal | linux73-nvidia-390xx | - | ❗ failed | 5 | 1 / 1 | 0 | 0 |  |
| 18 | 390xx | rt | linux61-rt-nvidia-390xx | - | ❗ failed | 3 | 1 / 1 | 0 | 0 |  |
| 19 | 390xx | rt | linux612-rt-nvidia-390xx | - | ❗ failed | 4 | 1 / 1 | 0 | 0 |  |
| 20 | 390xx | rt | linux66-rt-nvidia-390xx | - | ❗ failed | 4 | 1 / 1 | 0 | 0 |  |

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 340xx / normal / linux72-nvidia-340xx — ?  (48 errors)

Path: `340xx/normal/linux72-nvidia-340xx`

```
221: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
224: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
231: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
234: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
241: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
244: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
251: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
254: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
264: /usr/lib/modules/7.2.4-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
274: /usr/lib/modules/7.2.4-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
284: /usr/lib/modules/7.2.4-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
294: /usr/lib/modules/7.2.4-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
297: nv-linux.h:324:2: error: #error "NV_PCI_DMA_MAPPING_ERROR() undefined!"
306: nv-linux.h:336:2: error: #error "NV_ACPI_WALK_NAMESPACE_ARGUMENT_COUNT value unrecognized!"
309: nv-linux.h:324:2: error: #error "NV_PCI_DMA_MAPPING_ERROR() undefined!"
```

### 340xx / normal / linux73-nvidia-340xx — ?  (47 errors)

Path: `340xx/normal/linux73-nvidia-340xx`

```
221: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
224: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
231: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
234: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
241: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
244: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
251: conftest/functions.h:23:2: error: #error acpi_walk_namespace() conftest failed!
254: conftest/functions.h:25:2: error: #error pci_dma_mapping_error() conftest failed!
264: /usr/lib/modules/7.3.0-rc2-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
274: /usr/lib/modules/7.3.0-rc2-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
284: /usr/lib/modules/7.3.0-rc2-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
294: /usr/lib/modules/7.3.0-rc2-1-MANJARO/build/include/linux/sched/topology.h:122:23: error: ‘counted_by’ attribute is not allowed for a non-array field
297: nv-linux.h:324:2: error: #error "NV_PCI_DMA_MAPPING_ERROR() undefined!"
306: nv-linux.h:336:2: error: #error "NV_ACPI_WALK_NAMESPACE_ARGUMENT_COUNT value unrecognized!"
310: nv-linux.h:1881:5: error: too many arguments to function ‘pci_save_state’; expected 1, have 2
```

### 390xx / normal / linux61-nvidia-390xx — ?  (3 errors)

Path: `390xx/normal/linux61-nvidia-390xx`

```
54: make[2]: *** [/build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/Kbuild:224: cc_version_check] Error 1
56: make[1]: *** [Makefile:2028: /build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build] Error 2
57: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux612-nvidia-390xx — ?  (4 errors)

Path: `390xx/normal/linux612-nvidia-390xx`

```
55: make[3]: *** [/build/diag/nvidia-390xx/normal-kernels/linux612-nvidia-390xx/src/nvidia/390.157/build/Kbuild:224: cc_version_check] Error 1
57: make[2]: *** [/usr/lib/modules/6.12.109-1-MANJARO/build/Makefile:1967: /build/diag/nvidia-390xx/normal-kernels/linux612-nvidia-390xx/src/nvidia/390.157/build] Error 2
58: make[1]: *** [Makefile:224: __sub-make] Error 2
60: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux618-nvidia-390xx — ?  (5 errors)

Path: `390xx/normal/linux618-nvidia-390xx`

```
56: make[4]: *** [Kbuild:225: cc_version_check] Error 1
58: make[3]: *** [/usr/lib/modules/6.18.50-1-MANJARO/build/Makefile:2050: .] Error 2
59: make[2]: *** [/usr/lib/modules/6.18.50-1-MANJARO/build/Makefile:248: __sub-make] Error 2
61: make[1]: *** [Makefile:248: __sub-make] Error 2
63: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux66-nvidia-390xx — ?  (4 errors)

Path: `390xx/normal/linux66-nvidia-390xx`

```
55: make[3]: *** [/build/diag/nvidia-390xx/normal-kernels/linux66-nvidia-390xx/src/nvidia/390.157/build/Kbuild:225: cc_version_check] Error 1
57: make[2]: *** [/usr/lib/modules/6.6.156-2-MANJARO/build/Makefile:1933: /build/diag/nvidia-390xx/normal-kernels/linux66-nvidia-390xx/src/nvidia/390.157/build] Error 2
58: make[1]: *** [Makefile:234: __sub-make] Error 2
60: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux71-nvidia-390xx — ?  (5 errors)

Path: `390xx/normal/linux71-nvidia-390xx`

```
56: make[4]: *** [Kbuild:225: cc_version_check] Error 1
58: make[3]: *** [/usr/lib/modules/7.1.13-2-MANJARO/build/Makefile:2165: .] Error 2
59: make[2]: *** [/usr/lib/modules/7.1.13-2-MANJARO/build/Makefile:248: __sub-make] Error 2
61: make[1]: *** [Makefile:248: __sub-make] Error 2
63: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux72-nvidia-390xx — ?  (5 errors)

Path: `390xx/normal/linux72-nvidia-390xx`

```
56: make[4]: *** [Kbuild:225: cc_version_check] Error 1
58: make[3]: *** [/usr/lib/modules/7.2.4-1-MANJARO/build/Makefile:2198: .] Error 2
59: make[2]: *** [/usr/lib/modules/7.2.4-1-MANJARO/build/Makefile:248: __sub-make] Error 2
61: make[1]: *** [Makefile:248: __sub-make] Error 2
63: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux73-nvidia-390xx — ?  (5 errors)

Path: `390xx/normal/linux73-nvidia-390xx`

```
55: make[4]: *** [Kbuild:224: cc_version_check] Error 1
58: make[3]: *** [/usr/lib/modules/7.3.0-rc2-1-MANJARO/build/Makefile:2229: .] Error 2
59: make[2]: *** [/usr/lib/modules/7.3.0-rc2-1-MANJARO/build/Makefile:248: __sub-make] Error 2
61: make[1]: *** [Makefile:248: __sub-make] Error 2
63: make: *** [Makefile:93: modules] Error 2
```

### 390xx / rt / linux61-rt-nvidia-390xx — ?  (3 errors)

Path: `390xx/rt/linux61-rt-nvidia-390xx`

```
54: make[2]: *** [/build/diag/nvidia-390xx/rt-kernels/linux61-rt-nvidia-390xx/src/nvidia/390.157/build/Kbuild:224: cc_version_check] Error 1
56: make[1]: *** [Makefile:2028: /build/diag/nvidia-390xx/rt-kernels/linux61-rt-nvidia-390xx/src/nvidia/390.157/build] Error 2
57: make: *** [Makefile:93: modules] Error 2
```

### 390xx / rt / linux612-rt-nvidia-390xx — ?  (4 errors)

Path: `390xx/rt/linux612-rt-nvidia-390xx`

```
55: make[3]: *** [/build/diag/nvidia-390xx/rt-kernels/linux612-rt-nvidia-390xx/src/nvidia/390.157/build/Kbuild:225: cc_version_check] Error 1
57: make[2]: *** [/usr/lib/modules/6.12.100-1-rt20-MANJARO/build/Makefile:1962: /build/diag/nvidia-390xx/rt-kernels/linux612-rt-nvidia-390xx/src/nvidia/390.157/build] Error 2
58: make[1]: *** [Makefile:224: __sub-make] Error 2
60: make: *** [Makefile:93: modules] Error 2
```

### 390xx / rt / linux66-rt-nvidia-390xx — ?  (4 errors)

Path: `390xx/rt/linux66-rt-nvidia-390xx`

```
55: make[3]: *** [/build/diag/nvidia-390xx/rt-kernels/linux66-rt-nvidia-390xx/src/nvidia/390.157/build/Kbuild:225: cc_version_check] Error 1
57: make[2]: *** [/usr/lib/modules/6.6.151-1-rt78-MANJARO/build/Makefile:1933: /build/diag/nvidia-390xx/rt-kernels/linux66-rt-nvidia-390xx/src/nvidia/390.157/build] Error 2
58: make[1]: *** [Makefile:234: __sub-make] Error 2
60: make: *** [Makefile:93: modules] Error 2
```

## 🔍 Suspicious signatures

Lines that are **not** errors and **not** warnings, but contain keywords that often indicate real problems (missing files, permissions, OOM, crashes, missing deps).

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 1 | 1 | `/usr/lib/modules/7.2.4-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory` | 340xx/normal |
| 2 | 1 | 1 | `/usr/lib/modules/7.3.0-rc2-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |
| 3 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80649’: Permission denied` | 340xx/normal |
| 4 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80652’: Permission denied` | 340xx/normal |
| 5 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80655’: Permission denied` | 340xx/normal |
| 6 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80658’: Permission denied` | 340xx/normal |
| 7 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80661’: Permission denied` | 340xx/normal |
| 8 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80664’: Permission denied` | 340xx/normal |
| 9 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80667’: Permission denied` | 340xx/normal |
| 10 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80670’: Permission denied` | 340xx/normal |
| 11 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80673’: Permission denied` | 340xx/normal |
| 12 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80676’: Permission denied` | 340xx/normal |
| 13 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80679’: Permission denied` | 340xx/normal |
| 14 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80682’: Permission denied` | 340xx/normal |
| 15 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80685’: Permission denied` | 340xx/normal |
| 16 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80688’: Permission denied` | 340xx/normal |
| 17 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80691’: Permission denied` | 340xx/normal |
| 18 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80694’: Permission denied` | 340xx/normal |
| 19 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80697’: Permission denied` | 340xx/normal |
| 20 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80700’: Permission denied` | 340xx/normal |
| 21 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80703’: Permission denied` | 340xx/normal |
| 22 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80706’: Permission denied` | 340xx/normal |
| 23 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80709’: Permission denied` | 340xx/normal |
| 24 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80712’: Permission denied` | 340xx/normal |
| 25 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80715’: Permission denied` | 340xx/normal |
| 26 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80718’: Permission denied` | 340xx/normal |
| 27 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_80721’: Permission denied` | 340xx/normal |
| 28 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88366’: Permission denied` | 340xx/normal |
| 29 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88369’: Permission denied` | 340xx/normal |
| 30 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88372’: Permission denied` | 340xx/normal |
| 31 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88375’: Permission denied` | 340xx/normal |
| 32 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88378’: Permission denied` | 340xx/normal |
| 33 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88381’: Permission denied` | 340xx/normal |
| 34 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88384’: Permission denied` | 340xx/normal |
| 35 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88387’: Permission denied` | 340xx/normal |
| 36 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88390’: Permission denied` | 340xx/normal |
| 37 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88393’: Permission denied` | 340xx/normal |
| 38 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88396’: Permission denied` | 340xx/normal |
| 39 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88399’: Permission denied` | 340xx/normal |
| 40 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88402’: Permission denied` | 340xx/normal |
| 41 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88405’: Permission denied` | 340xx/normal |
| 42 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88408’: Permission denied` | 340xx/normal |
| 43 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88411’: Permission denied` | 340xx/normal |
| 44 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88414’: Permission denied` | 340xx/normal |
| 45 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88417’: Permission denied` | 340xx/normal |
| 46 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88420’: Permission denied` | 340xx/normal |
| 47 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88423’: Permission denied` | 340xx/normal |
| 48 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88426’: Permission denied` | 340xx/normal |
| 49 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88429’: Permission denied` | 340xx/normal |
| 50 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88432’: Permission denied` | 340xx/normal |
| 51 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88435’: Permission denied` | 340xx/normal |
| 52 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88438’: Permission denied` | 340xx/normal |
| 53 | 1 | 1 | `mkdir: cannot create directory ‘.tmp_88441’: Permission denied` | 340xx/normal |

<details><summary>Context excerpts (first few hits per signature)</summary>

**`/usr/lib/modules/7.2.4-1-MANJARO/build/scripts/Makefile.build:37: Makefile: No such file or directory`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`/usr/lib/modules/7.3.0-rc2-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux73-nvidia-340xx] 474: mkdir: cannot create directory ‘.tmp_88366’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 475: mkdir: cannot create directory ‘.tmp_88369’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 476: mkdir: cannot create directory ‘.tmp_88372’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 477: mkdir: cannot create directory ‘.tmp_88375’: Permission denied
[340xx/normal/linux73-nvidia-340xx] 478: mkdir: cannot create directory ‘.tmp_88378’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80649’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80652’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80655’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80658’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80661’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80664’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80667’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

**`mkdir: cannot create directory ‘.tmp_80670’: Permission denied`**

```
[340xx/normal/linux72-nvidia-340xx] 488: mkdir: cannot create directory ‘.tmp_80649’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 489: mkdir: cannot create directory ‘.tmp_80652’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 490: mkdir: cannot create directory ‘.tmp_80655’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 491: mkdir: cannot create directory ‘.tmp_80658’: Permission denied
[340xx/normal/linux72-nvidia-340xx] 492: mkdir: cannot create directory ‘.tmp_80661’: Permission denied
```

</details>

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 20 | 30 | `warning: the compiler differs from the one used to build the kernel` | 340xx/normal, 340xx/rt, 390xx/normal, 390xx/rt |
| 2 | 6 | 6 | `warning: ignoring old recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 3 | 6 | 6 | `warning: overriding recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 4 | 4 | 16 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt |
| 5 | 2 | 16 | `warning: ‘NV_ACPI_WALK_NAMESPACE_ARGUMENT_COUNT’ is not defined, evaluates to ‘0’ [-Wundef]` | 340xx/normal |
| 6 | 2 | 2 | `warning: ignoring old recipe for target 'Module.symvers'` | 340xx/normal |
| 7 | 2 | 2 | `warning: ignoring return value of ‘refcount_sub_and_test’ declared with attribute ‘warn_unused_result’ [-Wunused-result]` | 340xx/normal |
| 8 | 2 | 2 | `warning: overriding recipe for target 'Module.symvers'` | 340xx/normal |

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

---
_End of index. Per-build detail files live in the harvest tree._
