# Harvest Index — 2026-10-09 14:16:00 

## TL;DR

- **State:** ❗2 failed · 🔍0 suspicious · ⚠48 warnings · ✅4 clean · 🚫14 not-built
- **Action needed (137):**
    - 18 builds · 36 hits · `warning: format '%d' expects argument of type 'int', but argument 2 has type 'uvm_processor_id_t' [-Wformat=]`
    - 18 builds · 36 hits · `warning: format '%d' expects argument of type 'int', but argument 3 has type 'uvm_processor_id_t' [-Wformat=]`
    - 18 builds · 18 hits · `warning: variable 'DIDT10Count' set but not used [-Wunused-but-set-variable=]`
    - … and 134 more (see `## 🔁 Cross-build warning signatures`)

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  390xx, 470xx, 580xx, 580xx-open, nvidia, nvidia-open
- **Builds:** 68 — ❗2 failed, 🔍0 suspicious, ⚠48 warn, ✅4 clean, 🚫14 not-built
- **Warning signatures:** 137 total — 137 actionable across multiple builds, 0 informational, 0 unique to one build
- **Suspicious signatures:** 0  ·  **integrity issues:** 0 builds  ·  **integrity notes:** 0 builds

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
| 1 | 390xx | normal | 6.12.112-1-MANJARO | 390.157 | ⚠ warnings | 0 | 75 / 83 | 0 | 94522 |  |
| 2 | 390xx | normal | 6.18.55-1-MANJARO | 390.157 | ⚠ warnings | 0 | 75 / 79 | 0 | 94522 |  |
| 3 | 390xx | normal | 6.6.158-1-MANJARO | 390.157 | ⚠ warnings | 0 | 6 / 12 | 0 | 94474 |  |
| 4 | 390xx | normal | 7.2.9-1-MANJARO | 390.157 | ⚠ warnings | 0 | 75 / 79 | 0 | 94522 |  |
| 5 | 390xx | normal | 7.3.0-rc6-1-MANJARO | 390.157 | ⚠ warnings | 0 | 75 / 79 | 0 | 94522 |  |
| 6 | 390xx | normal | linux54-nvidia-390xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 7 | 390xx | normal | linux61-nvidia-390xx | - | ❗ failed | 26 | 2 / 8 | 0 | 0 |  |
| 8 | 390xx | normal | linux71-nvidia-390xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 9 | 390xx | rt | 6.12.100-1-rt20-MANJARO | 390.157 | ⚠ warnings | 0 | 75 / 83 | 0 | 94522 |  |
| 10 | 390xx | rt | 6.6.151-1-rt78-MANJARO | 390.157 | ⚠ warnings | 0 | 6 / 12 | 0 | 94474 |  |
| 11 | 390xx | rt | linux61-rt-nvidia-390xx | - | ❗ failed | 26 | 2 / 8 | 0 | 0 |  |
| 12 | 390xx | rt | linux618-rt-nvidia-390xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 13 | 470xx | normal | 6.1.189-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 6 / 6 | 0 | 157265 |  |
| 14 | 470xx | normal | 6.12.112-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 52 / 60 | 0 | 63696 |  |
| 15 | 470xx | normal | 6.18.55-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 16 | 470xx | normal | 6.6.158-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 14 / 16 | 0 | 63696 |  |
| 17 | 470xx | normal | 7.2.9-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 18 | 470xx | normal | 7.3.0-rc6-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 19 | 470xx | normal | linux54-nvidia-470xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 20 | 470xx | normal | linux71-nvidia-470xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 21 | 470xx | rt | 6.1.182-1-rt67-MANJARO | 470.256.02 | ⚠ warnings | 0 | 6 / 6 | 0 | 157265 |  |
| 22 | 470xx | rt | 6.12.100-1-rt20-MANJARO | 470.256.02 | ⚠ warnings | 0 | 52 / 60 | 0 | 63696 |  |
| 23 | 470xx | rt | 6.6.151-1-rt78-MANJARO | 470.256.02 | ⚠ warnings | 0 | 14 / 16 | 0 | 63696 |  |
| 24 | 470xx | rt | linux618-rt-nvidia-470xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 25 | 580xx | normal | 6.1.189-1-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 137982 |  |
| 26 | 580xx | normal | 6.12.112-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 1 / 7 | 0 | 47475 |  |
| 27 | 580xx | normal | 6.18.55-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 2 / 8 | 0 | 47475 |  |
| 28 | 580xx | normal | 6.6.158-1-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 47475 |  |
| 29 | 580xx | normal | 7.2.9-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 3 / 173 | 0 | 47475 |  |
| 30 | 580xx | normal | 7.3.0-rc6-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 3 / 173 | 0 | 47475 |  |
| 31 | 580xx | normal | linux71-nvidia-580xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 32 | 580xx | rt | 6.1.182-1-rt67-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 137983 |  |
| 33 | 580xx | rt | 6.12.100-1-rt20-MANJARO | 580.178.04 | ⚠ warnings | 0 | 1 / 7 | 0 | 47475 |  |
| 34 | 580xx | rt | 6.6.151-1-rt78-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 47475 |  |
| 35 | 580xx-open | normal | 6.1.189-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 7 / 400 | 0 | 39133 |  |
| 36 | 580xx-open | normal | 6.12.112-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 29 / 428 | 0 | 13756 |  |
| 37 | 580xx-open | normal | 6.18.55-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 29 / 428 | 0 | 13821 |  |
| 38 | 580xx-open | normal | 6.6.158-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 7 / 400 | 0 | 13404 |  |
| 39 | 580xx-open | normal | 7.2.9-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 30 / 593 | 0 | 13821 |  |
| 40 | 580xx-open | normal | 7.3.0-rc6-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 30 / 593 | 0 | 13821 |  |
| 41 | 580xx-open | normal | linux71-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 42 | 580xx-open | rt | 6.1.182-1-rt67-MANJARO | 580.178.04 | ⚠ warnings | 0 | 7 / 400 | 0 | 39124 |  |
| 43 | 580xx-open | rt | 6.12.100-1-rt20-MANJARO | 580.178.04 | ⚠ warnings | 0 | 29 / 428 | 0 | 13740 |  |
| 44 | 580xx-open | rt | 6.6.151-1-rt78-MANJARO | 580.178.04 | ⚠ warnings | 0 | 7 / 400 | 0 | 9890 |  |
| 45 | nvidia | normal | 6.1.189-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 132258 |  |
| 46 | nvidia | normal | 6.12.112-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 44699 |  |
| 47 | nvidia | normal | 6.18.55-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 3 / 5 | 0 | 44699 |  |
| 48 | nvidia | normal | 6.6.158-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 44699 |  |
| 49 | nvidia | normal | 7.2.9-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 3 / 5 | 0 | 44699 |  |
| 50 | nvidia | normal | 7.3.0-rc6-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 3 / 5 | 0 | 44699 |  |
| 51 | nvidia | normal | linux54-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 52 | nvidia | normal | linux71-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 53 | nvidia | rt | 6.1.182-1-rt67-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 132258 |  |
| 54 | nvidia | rt | 6.12.100-1-rt20-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 44699 |  |
| 55 | nvidia | rt | 6.6.151-1-rt78-MANJARO | 615.78.08 | ⚠ warnings | 0 | 2 / 4 | 0 | 44699 |  |
| 56 | nvidia | rt | linux618-rt-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 57 | nvidia-open | normal | 6.1.189-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 37478 |  |
| 58 | nvidia-open | normal | 6.12.112-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 59 | nvidia-open | normal | 6.18.55-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 60 | nvidia-open | normal | 6.6.158-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 61 | nvidia-open | normal | 7.2.9-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 62 | nvidia-open | normal | 7.3.0-rc6-1-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 63 | nvidia-open | normal | linux54-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 64 | nvidia-open | normal | linux71-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 65 | nvidia-open | rt | 6.1.182-1-rt67-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 37478 |  |
| 66 | nvidia-open | rt | 6.12.100-1-rt20-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 67 | nvidia-open | rt | 6.6.151-1-rt78-MANJARO | 615.78.08 | ⚠ warnings | 0 | 5 / 7 | 0 | 11674 |  |
| 68 | nvidia-open | rt | linux618-rt-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 390xx / normal / linux61-nvidia-390xx — ?  (26 errors)

Path: `390xx/normal/linux61-nvidia-390xx`

```
193: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
198: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
204: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
224: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
231: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
238: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
243: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
249: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
267: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
273: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
291: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
297: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
317: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of ‘vm_flags_set’ follows non-static declaration
324: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2031:20: error: static declaration of ‘vm_flags_clear’ follows non-static declaration
332: make[2]: *** [scripts/Makefile.build:250: /build/sources/PKGBUILDs/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/nvidia/nv-gpu-numa.o] Error 1
```

### 390xx / rt / linux61-rt-nvidia-390xx — ?  (26 errors)

Path: `390xx/rt/linux61-rt-nvidia-390xx`

```
193: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
198: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
204: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
224: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
231: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
238: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function ‘vm_flags_set’; did you mean ‘nv_vm_flags_set’? [-Wimplicit-function-declaration]
243: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
249: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
267: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
273: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
291: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function ‘vm_flags_clear’; did you mean ‘nv_vm_flags_clear’? [-Wimplicit-function-declaration]
297: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of ‘timer_delete_sync’ follows non-static declaration
317: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of ‘vm_flags_set’ follows non-static declaration
324: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2031:20: error: static declaration of ‘vm_flags_clear’ follows non-static declaration
328: make[2]: *** [scripts/Makefile.build:250: /build/sources/PKGBUILDs/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/nvidia/nv-frontend.o] Error 1
```

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 18 | 36 | `warning: format '%d' expects argument of type 'int', but argument 2 has type 'uvm_processor_id_t' [-Wformat=]` | nvidia-open/normal, nvidia-open/rt, nvidia/normal, nvidia/rt |
| 2 | 18 | 36 | `warning: format '%d' expects argument of type 'int', but argument 3 has type 'uvm_processor_id_t' [-Wformat=]` | nvidia-open/normal, nvidia-open/rt, nvidia/normal, nvidia/rt |
| 3 | 18 | 18 | `warning: variable 'DIDT10Count' set but not used [-Wunused-but-set-variable=]` | 580xx-open/normal, 580xx-open/rt, nvidia-open/normal, nvidia-open/rt |
| 4 | 18 | 18 | `warning: variable 'extDTDCount' set but not used [-Wunused-but-set-variable=]` | 580xx-open/normal, 580xx-open/rt, nvidia-open/normal, nvidia-open/rt |
| 5 | 18 | 18 | `warning: variable 'i' set but not used [-Wunused-but-set-variable=]` | 580xx-open/normal, 580xx-open/rt, nvidia-open/normal, nvidia-open/rt |
| 6 | 16 | 16 | `warning: this statement may fall through [-Wimplicit-fallthrough=]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 7 | 14 | 42 | `warning: implicit conversion from 'uvm_fault_access_type_t' to 'uvm_fault_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 8 | 14 | 14 | `warning: implicit conversion from 'enum <anonymous>' to 'uvm_fault_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 9 | 14 | 14 | `warning: implicit conversion from 'uvm_fault_type_t' to 'uvm_fault_access_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 10 | 10 | 70 | `warning: this use of 'defined' may not be portable [-Wexpansion-to-defined]` | 580xx-open/normal, 580xx-open/rt, 580xx/normal, 580xx/rt |
| 11 | 10 | 50 | `warning: 'static' is not at beginning of declaration [-Wold-style-declaration]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 12 | 10 | 10 | `warning: no previous prototype for 'exercise_error_forwarding_va' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 13 | 10 | 10 | `warning: no previous prototype for 'nv_destroy_ibmnpu_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 14 | 10 | 10 | `warning: no previous prototype for 'nv_init_ibmnpu_devices' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 15 | 10 | 10 | `warning: no previous prototype for 'nv_init_ibmnpu_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 16 | 10 | 10 | `warning: no previous prototype for 'nv_load_dma_map_scatterlist' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 17 | 10 | 10 | `warning: no previous prototype for 'nvidia_exit_module' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 18 | 10 | 10 | `warning: no previous prototype for 'nvidia_init_module' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 19 | 10 | 10 | `warning: no previous prototype for 'nvkms_close_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 20 | 10 | 10 | `warning: no previous prototype for 'nvkms_ioctl_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 21 | 10 | 10 | `warning: no previous prototype for 'nvkms_open_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 22 | 10 | 10 | `warning: no previous prototype for 'nvlink_core_exit' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 23 | 10 | 10 | `warning: no previous prototype for 'nvlink_core_init' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 24 | 10 | 10 | `warning: no previous prototype for 'on_nvq_assert' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 25 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_disable_prefetch_faults_unsupported' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 26 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_enable_prefetch_faults_unsupported' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 27 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_mmu_mode_kepler' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 28 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_mmu_mode_pascal' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 29 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_disable_prefetch_faults' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 30 | 10 | 10 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_enable_prefetch_faults' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 31 | 10 | 10 | `warning: no previous prototype for 'uvm_tools_exit' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 32 | 10 | 10 | `warning: no previous prototype for 'uvm_tools_init' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 33 | 9 | 3510 | `warning: variable 'aggregate_mask' set but not used [-Wunused-but-set-variable=]` | 580xx-open/normal, 580xx-open/rt |
| 34 | 9 | 27 | `warning: 'virtual bool DisplayPort::EvoMainLink::setFlushMode()' was hidden [-Woverloaded-virtual=]` | 580xx-open/normal, 580xx-open/rt |
| 35 | 9 | 27 | `warning: 'virtual void DisplayPort::EvoMainLink::clearFlushMode(unsigned int, bool)' was hidden [-Woverloaded-virtual=]` | 580xx-open/normal, 580xx-open/rt |
| 36 | 9 | 9 | `warning: 'IMPORT_SGT_STUBS_NEEDED' redefined` | 470xx/normal, 470xx/rt |
| 37 | 9 | 9 | `warning: unused variable 'nv_drm_plane_state' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 38 | 9 | 9 | `warning: unused variable 'primary_plane' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 39 | 9 | 9 | `warning: unused variable 'ret' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 40 | 9 | 9 | `warning: unused variable 'size' [-Wunused-variable]` | 580xx-open/normal, 580xx-open/rt |
| 41 | 9 | 9 | `warning: unused variable 'status' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 42 | 7 | 23 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 390xx/normal, 390xx/rt |
| 43 | 7 | 7 | `warning: implicit conversion from 'UvmGpuCachingType' to 'UvmRmGpuCachingType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 44 | 7 | 7 | `warning: implicit conversion from 'UvmGpuCompressionType' to 'UvmRmGpuCompressionType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 45 | 7 | 7 | `warning: implicit conversion from 'UvmGpuFormatElementBits' to 'UvmRmGpuFormatElementBits' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 46 | 7 | 7 | `warning: implicit conversion from 'UvmGpuFormatType' to 'UvmRmGpuFormatType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 47 | 7 | 7 | `warning: implicit conversion from 'UvmGpuMappingType' to 'UvmRmGpuMappingType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 48 | 7 | 7 | `warning: unused variable 'device' [-Wunused-variable]` | 390xx/normal, 390xx/rt |
| 49 | 6 | 6 | `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]` | 580xx/normal, nvidia/normal |
| 50 | 5 | 5 | `warning: no previous prototype for '_raw_q_flush' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 51 | 5 | 5 | `warning: no previous prototype for 'block_map' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 52 | 5 | 5 | `warning: no previous prototype for 'cpu_addr_from_fake' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 53 | 5 | 5 | `warning: no previous prototype for 'fake_membar' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 54 | 5 | 5 | `warning: no previous prototype for 'fake_noop' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 55 | 5 | 5 | `warning: no previous prototype for 'fake_wait_for_idle' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 56 | 5 | 5 | `warning: no previous prototype for 'get_page_sizes' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 57 | 5 | 5 | `warning: no previous prototype for 'libspdm_check_crypto_backend' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 58 | 5 | 5 | `warning: no previous prototype for 'libspdm_decode_base64' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 59 | 5 | 5 | `warning: no previous prototype for 'libspdm_ec_check_key' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 60 | 5 | 5 | `warning: no previous prototype for 'libspdm_ec_get_pub_key' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 61 | 5 | 5 | `warning: no previous prototype for 'libspdm_ec_set_pub_key' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 62 | 5 | 5 | `warning: no previous prototype for 'libspdm_encode_base64' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 63 | 5 | 5 | `warning: no previous prototype for 'libspdm_gen_x509_csr' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 64 | 5 | 5 | `warning: no previous prototype for 'libspdm_hkdf_sha256_extract_and_expand' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 65 | 5 | 5 | `warning: no previous prototype for 'libspdm_hkdf_sha384_extract_and_expand' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 66 | 5 | 5 | `warning: no previous prototype for 'libspdm_hkdf_sha512_extract_and_expand' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 67 | 5 | 5 | `warning: no previous prototype for 'libspdm_random_seed' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 68 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_construct_certificate' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 69 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_construct_certificate_stack' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 70 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_free' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 71 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_common_name' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 72 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_issuer_common_name' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 73 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_issuer_orgnization_name' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 74 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_organization_name' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 75 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_signature_algorithm' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 76 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_get_tbs_cert' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 77 | 5 | 5 | `warning: no previous prototype for 'libspdm_x509_stack_free' [-Wmissing-prototypes]` | 580xx-open/normal, 580xx-open/rt |
| 78 | 5 | 5 | `warning: no previous prototype for 'map_rm_pt_range' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 79 | 5 | 5 | `warning: no previous prototype for 'nv_cap_procfs_init' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 80 | 5 | 5 | `warning: no previous prototype for 'nv_dma_unmap_sgt' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 81 | 5 | 5 | `warning: no previous prototype for 'nv_firmware_path' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 82 | 5 | 5 | `warning: no previous prototype for 'nv_get_ibmnpu_chip_id' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 83 | 5 | 5 | `warning: no previous prototype for 'nv_get_num_dpaux_instances' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 84 | 5 | 5 | `warning: no previous prototype for 'nv_ibmnpu_cache_flush_numa_region' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 85 | 5 | 5 | `warning: no previous prototype for 'nv_pci_register_driver' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 86 | 5 | 5 | `warning: no previous prototype for 'nv_unregister_ibmnpu_devices' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 87 | 5 | 5 | `warning: no previous prototype for 'nvswitch_exit' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 88 | 5 | 5 | `warning: no previous prototype for 'nvswitch_init' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 89 | 5 | 5 | `warning: no previous prototype for 'os_mem_copy_custom' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 90 | 5 | 5 | `warning: no previous prototype for 'parse_fault_entry_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 91 | 5 | 5 | `warning: no previous prototype for 'random_channel_type' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 92 | 5 | 5 | `warning: no previous prototype for 'random_gpu' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 93 | 5 | 5 | `warning: no previous prototype for 'range_group_range_iter_advance' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 94 | 5 | 5 | `warning: no previous prototype for 'stress_test_all_gpus_in_va' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 95 | 5 | 5 | `warning: no previous prototype for 'test_memset_rm_mem' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 96 | 5 | 5 | `warning: no previous prototype for 'test_ordering' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 97 | 5 | 5 | `warning: no previous prototype for 'test_page_tree_alloc_table' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 98 | 5 | 5 | `warning: no previous prototype for 'test_push_interleaving' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 99 | 5 | 5 | `warning: no previous prototype for 'test_tracker_add_tracker' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 100 | 5 | 5 | `warning: no previous prototype for 'test_tracker_overwrite' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 101 | 5 | 5 | `warning: no previous prototype for 'test_tracking' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 102 | 5 | 5 | `warning: no previous prototype for 'timestamp_on_complete' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 103 | 5 | 5 | `warning: no previous prototype for 'try_get_ptes' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 104 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_check_channel_va_space' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 105 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_flush_deferred_work' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 106 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_get_page_thrashing_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 107 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_get_prefetch_faults_reenable_lapse' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 108 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_range_group_range_count' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 109 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_range_group_range_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 110 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_set_page_prefetch_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 111 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_set_page_thrashing_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 112 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_set_prefetch_faults_reenable_lapse' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 113 | 5 | 5 | `warning: no previous prototype for 'uvm8_test_set_prefetch_filtering' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 114 | 5 | 5 | `warning: no previous prototype for 'uvm_api_disable_peer_access' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 115 | 5 | 5 | `warning: no previous prototype for 'uvm_api_enable_peer_access' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 116 | 5 | 5 | `warning: no previous prototype for 'uvm_channel_manager_print_pending_pushes' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 117 | 5 | 5 | `warning: no previous prototype for 'uvm_gpu_get_by_uuid_and_swizz_id_locked' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 118 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_client_id_to_utlb_id_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 119 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_engine_id_to_type_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 120 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_pascal_fault_buffer_parse_non_replayable_entry_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 121 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_client_id_to_utlb_id' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 122 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_clear_valid' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 123 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_is_valid' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 124 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_size' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 125 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_parse_entry' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 126 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_disable_access_counter_notifications' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 127 | 5 | 5 | `warning: no previous prototype for 'uvm_hal_volta_enable_access_counter_notifications' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 128 | 5 | 5 | `warning: no previous prototype for 'uvm_pushbuffer_get_size' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 129 | 5 | 5 | `warning: no previous prototype for 'uvm_pushbuffer_update_progress' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 130 | 5 | 5 | `warning: no previous prototype for 'uvm_range_group_range_next' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 131 | 5 | 5 | `warning: no previous prototype for 'uvm_range_group_range_prev' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 132 | 5 | 5 | `warning: no previous prototype for 'uvm_va_range_remove_gpu_va_space_managed' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 133 | 5 | 5 | `warning: no previous prototype for 'va_block_set_read_duplication_locked' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 134 | 4 | 660 | `warning: unused variable 'chip' [-Wunused-variable]` | 580xx-open/normal, 580xx/normal |
| 135 | 3 | 3 | `warning: conflicting types for 'nv_encode_caching' due to enum/integer mismatch; have 'int(pgprot_t *, NvU32,  nv_memory_type_t)' {aka 'int(struct pgprot *, unsigned int,  nv_memory_type_t)'} [-Wenum-int-mismatch]` | 470xx/normal |
| 136 | 2 | 8 | `warning: conflicting types for 'vm_flags_clear'; have 'void(struct vm_area_struct *, vm_flags_t)' {aka 'void(struct vm_area_struct *, long unsigned int)'}` | 390xx/normal, 390xx/rt |
| 137 | 2 | 8 | `warning: conflicting types for 'vm_flags_set'; have 'void(struct vm_area_struct *, vm_flags_t)' {aka 'void(struct vm_area_struct *, long unsigned int)'}` | 390xx/normal, 390xx/rt |

### ⚙️ Informational (build system / Makefile)

_None._

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

## 🚫 Not built (no make.log)

- `nvidia / normal / linux54-nvidia`
- `390xx / normal / linux54-nvidia-390xx`
- `470xx / normal / linux54-nvidia-470xx`
- `nvidia-open / normal / linux54-nvidia-open`
- `nvidia / rt / linux618-rt-nvidia`
- `390xx / rt / linux618-rt-nvidia-390xx`
- `470xx / rt / linux618-rt-nvidia-470xx`
- `nvidia-open / rt / linux618-rt-nvidia-open`
- `nvidia / normal / linux71-nvidia`
- `390xx / normal / linux71-nvidia-390xx`
- `470xx / normal / linux71-nvidia-470xx`
- `580xx / normal / linux71-nvidia-580xx`
- `580xx-open / normal / linux71-nvidia-580xx-open`
- `nvidia-open / normal / linux71-nvidia-open`

---
_End of index. Per-build detail files live in the harvest tree._

## ⚠ EOL / Out-of-sync packages

| Package | Repo version | Manjaro version | Status |
|---------|--------------|-----------------|--------|
| `nvidia-utils` | 615.78.08-1 | 615.71.09-2 | stale |
| `linux54` | — | — | not-in-manjaro |
| `linux618-rt` | — | — | not-in-manjaro |
| `linux71` | — | — | not-in-manjaro |

