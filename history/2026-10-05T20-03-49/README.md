# Harvest Index — 2026-10-05 20:03:49 

## TL;DR

- **State:** ❗2 failed · 🔍0 suspicious · ⚠24 warnings · ✅4 clean · 🚫38 not-built
- **Action needed (108):**
    - 18 builds · 18 hits · `warning: this statement may fall through [-Wimplicit-fallthrough=]`
    - 16 builds · 48 hits · `warning: implicit conversion from 'uvm_fault_access_type_t' to 'uvm_fault_type_t' [-Wenum-conversion]`
    - 16 builds · 16 hits · `warning: implicit conversion from 'enum <anonymous>' to 'uvm_fault_type_t' [-Wenum-conversion]`
    - … and 105 more (see `## 🔁 Cross-build warning signatures`)

## Overview

- **Diag root:** `/build/official/extra`
- **Harvest:**   `/build/harvest-official`
- **Branches:**  390xx, 470xx, 580xx, 580xx-open, nvidia, nvidia-open
- **Builds:** 68 — ❗2 failed, 🔍0 suspicious, ⚠24 warn, ✅4 clean, 🚫38 not-built
- **Warning signatures:** 109 total — 108 actionable across multiple builds, 0 informational, 1 unique to one build
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
| 1 | 390xx | normal | 6.12.109-1-MANJARO | 390.157 | ⚠ warnings | 0 | 77 / 114 | 0 | 94491 |  |
| 2 | 390xx | normal | 6.18.50-1-MANJARO | 390.157 | ⚠ warnings | 0 | 76 / 109 | 0 | 94492 |  |
| 3 | 390xx | normal | 6.6.156-2-MANJARO | 390.157 | ⚠ warnings | 0 | 6 / 12 | 0 | 94474 |  |
| 4 | 390xx | normal | 7.1.13-2-MANJARO | 390.157 | ⚠ warnings | 0 | 76 / 109 | 0 | 94492 |  |
| 5 | 390xx | normal | 7.2.4-1-MANJARO | 390.157 | ⚠ warnings | 0 | 76 / 109 | 0 | 94492 |  |
| 6 | 390xx | normal | 7.3.0-rc2-1-MANJARO | 390.157 | ⚠ warnings | 0 | 76 / 109 | 0 | 94492 |  |
| 7 | 390xx | normal | linux54-nvidia-390xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 8 | 390xx | normal | linux61-nvidia-390xx | - | ❗ failed | 26 | 2 / 8 | 0 | 0 |  |
| 9 | 390xx | rt | 6.12.100-1-rt20-MANJARO | 390.157 | ⚠ warnings | 0 | 76 / 113 | 0 | 94492 |  |
| 10 | 390xx | rt | 6.6.151-1-rt78-MANJARO | 390.157 | ⚠ warnings | 0 | 6 / 12 | 0 | 94474 |  |
| 11 | 390xx | rt | linux61-rt-nvidia-390xx | - | ❗ failed | 26 | 2 / 8 | 0 | 0 |  |
| 12 | 390xx | rt | linux618-rt-nvidia-390xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 13 | 470xx | normal | 6.1.187-2-MANJARO | 470.256.02 | ⚠ warnings | 0 | 6 / 6 | 0 | 157265 |  |
| 14 | 470xx | normal | 6.12.109-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 52 / 60 | 0 | 63696 |  |
| 15 | 470xx | normal | 6.18.50-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 16 | 470xx | normal | 6.6.156-2-MANJARO | 470.256.02 | ⚠ warnings | 0 | 14 / 16 | 0 | 63696 |  |
| 17 | 470xx | normal | 7.1.13-2-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 18 | 470xx | normal | 7.2.4-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 19 | 470xx | normal | 7.3.0-rc2-1-MANJARO | 470.256.02 | ⚠ warnings | 0 | 53 / 61 | 0 | 63696 |  |
| 20 | 470xx | normal | linux54-nvidia-470xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 21 | 470xx | rt | 6.1.182-1-rt67-MANJARO | 470.256.02 | ⚠ warnings | 0 | 6 / 6 | 0 | 157265 |  |
| 22 | 470xx | rt | 6.12.100-1-rt20-MANJARO | 470.256.02 | ⚠ warnings | 0 | 52 / 60 | 0 | 63696 |  |
| 23 | 470xx | rt | 6.6.151-1-rt78-MANJARO | 470.256.02 | ⚠ warnings | 0 | 14 / 16 | 0 | 63696 |  |
| 24 | 470xx | rt | linux618-rt-nvidia-470xx | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 25 | 580xx | normal | 6.1.187-2-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 137982 |  |
| 26 | 580xx | normal | 6.12.109-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 1 / 7 | 0 | 47475 |  |
| 27 | 580xx | normal | 6.18.50-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 2 / 8 | 0 | 47475 |  |
| 28 | 580xx | normal | 6.6.156-2-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 47475 |  |
| 29 | 580xx | normal | 7.1.13-2-MANJARO | 580.178.04 | ⚠ warnings | 0 | 3 / 173 | 0 | 47475 |  |
| 30 | 580xx | normal | 7.2.4-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 3 / 173 | 0 | 47475 |  |
| 31 | 580xx | normal | 7.3.0-rc2-1-MANJARO | 580.178.04 | ⚠ warnings | 0 | 3 / 173 | 0 | 47475 |  |
| 32 | 580xx | rt | 6.1.182-1-rt67-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 137983 |  |
| 33 | 580xx | rt | 6.12.100-1-rt20-MANJARO | 580.178.04 | ⚠ warnings | 0 | 1 / 7 | 0 | 47475 |  |
| 34 | 580xx | rt | 6.6.151-1-rt78-MANJARO | 580.178.04 | ✅ clean | 0 | 0 / 0 | 0 | 47475 |  |
| 35 | 580xx-open | normal | linux61-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 36 | 580xx-open | normal | linux612-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 37 | 580xx-open | normal | linux618-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 38 | 580xx-open | normal | linux66-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 39 | 580xx-open | normal | linux71-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 40 | 580xx-open | normal | linux72-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 41 | 580xx-open | normal | linux73-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 42 | 580xx-open | rt | linux61-rt-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 43 | 580xx-open | rt | linux612-rt-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 44 | 580xx-open | rt | linux66-rt-nvidia-580xx-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 45 | nvidia | normal | linux54-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 46 | nvidia | normal | linux61-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 47 | nvidia | normal | linux612-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 48 | nvidia | normal | linux618-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 49 | nvidia | normal | linux66-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 50 | nvidia | normal | linux71-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 51 | nvidia | normal | linux72-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 52 | nvidia | normal | linux73-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 53 | nvidia | rt | linux61-rt-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 54 | nvidia | rt | linux612-rt-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 55 | nvidia | rt | linux618-rt-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 56 | nvidia | rt | linux66-rt-nvidia | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 57 | nvidia-open | normal | linux54-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 58 | nvidia-open | normal | linux61-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 59 | nvidia-open | normal | linux612-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 60 | nvidia-open | normal | linux618-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 61 | nvidia-open | normal | linux66-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 62 | nvidia-open | normal | linux71-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 63 | nvidia-open | normal | linux72-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 64 | nvidia-open | normal | linux73-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 65 | nvidia-open | rt | linux61-rt-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 66 | nvidia-open | rt | linux612-rt-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 67 | nvidia-open | rt | linux618-rt-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 68 | nvidia-open | rt | linux66-rt-nvidia-open | - | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 390xx / normal / linux61-nvidia-390xx — ?  (26 errors)

Path: `390xx/normal/linux61-nvidia-390xx`

```
196: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
200: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
207: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
214: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
220: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
224: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
230: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
249: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
267: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
272: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
278: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
297: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
317: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of 'vm_flags_set' follows non-static declaration
324: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2031:20: error: static declaration of 'vm_flags_clear' follows non-static declaration
331: /build/official/extra/linux61-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of 'vm_flags_set' follows non-static declaration
```

### 390xx / rt / linux61-rt-nvidia-390xx — ?  (26 errors)

Path: `390xx/rt/linux61-rt-nvidia-390xx`

```
193: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
200: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
207: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
212: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
218: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
238: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:337:5: error: implicit declaration of function 'vm_flags_set'; did you mean 'nv_vm_flags_set'? [-Wimplicit-function-declaration]
243: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
248: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
256: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
259: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
291: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-mm.h:348:5: error: implicit declaration of function 'vm_flags_clear'; did you mean 'nv_vm_flags_clear'? [-Wimplicit-function-declaration]
297: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-timer.h:70:19: error: static declaration of 'timer_delete_sync' follows non-static declaration
317: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of 'vm_flags_set' follows non-static declaration
324: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2031:20: error: static declaration of 'vm_flags_clear' follows non-static declaration
331: /build/official/extra/linux61-rt-extramodules/nvidia-390xx/src/nvidia/390.157/build/common/inc/nv-linux.h:2026:20: error: static declaration of 'vm_flags_set' follows non-static declaration
```

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 18 | 18 | `warning: this statement may fall through [-Wimplicit-fallthrough=]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 2 | 16 | 48 | `warning: implicit conversion from 'uvm_fault_access_type_t' to 'uvm_fault_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 3 | 16 | 16 | `warning: implicit conversion from 'enum <anonymous>' to 'uvm_fault_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 4 | 16 | 16 | `warning: implicit conversion from 'uvm_fault_type_t' to 'uvm_fault_access_type_t' [-Wenum-conversion]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 5 | 12 | 60 | `warning: 'static' is not at beginning of declaration [-Wold-style-declaration]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 6 | 12 | 12 | `warning: no previous prototype for 'exercise_error_forwarding_va' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 7 | 12 | 12 | `warning: no previous prototype for 'nv_destroy_ibmnpu_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 8 | 12 | 12 | `warning: no previous prototype for 'nv_init_ibmnpu_devices' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 9 | 12 | 12 | `warning: no previous prototype for 'nv_init_ibmnpu_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 10 | 12 | 12 | `warning: no previous prototype for 'nv_load_dma_map_scatterlist' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 11 | 12 | 12 | `warning: no previous prototype for 'nvidia_exit_module' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 12 | 12 | 12 | `warning: no previous prototype for 'nvidia_init_module' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 13 | 12 | 12 | `warning: no previous prototype for 'nvkms_close_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 14 | 12 | 12 | `warning: no previous prototype for 'nvkms_ioctl_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 15 | 12 | 12 | `warning: no previous prototype for 'nvkms_open_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 16 | 12 | 12 | `warning: no previous prototype for 'nvlink_core_exit' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 17 | 12 | 12 | `warning: no previous prototype for 'nvlink_core_init' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 18 | 12 | 12 | `warning: no previous prototype for 'on_nvq_assert' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 19 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_disable_prefetch_faults_unsupported' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 20 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_enable_prefetch_faults_unsupported' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 21 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_mmu_mode_kepler' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 22 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_mmu_mode_pascal' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 23 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_disable_prefetch_faults' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 24 | 12 | 12 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_enable_prefetch_faults' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 25 | 12 | 12 | `warning: no previous prototype for 'uvm_tools_exit' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 26 | 12 | 12 | `warning: no previous prototype for 'uvm_tools_init' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt, 470xx/normal, 470xx/rt |
| 27 | 10 | 10 | `warning: 'IMPORT_SGT_STUBS_NEEDED' redefined` | 470xx/normal, 470xx/rt |
| 28 | 10 | 10 | `warning: unused variable 'nv_drm_plane_state' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 29 | 10 | 10 | `warning: unused variable 'primary_plane' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 30 | 10 | 10 | `warning: unused variable 'ret' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 31 | 10 | 10 | `warning: unused variable 'status' [-Wunused-variable]` | 470xx/normal, 470xx/rt |
| 32 | 8 | 24 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 390xx/normal, 390xx/rt |
| 33 | 8 | 8 | `warning: implicit conversion from 'UvmGpuCachingType' to 'UvmRmGpuCachingType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 34 | 8 | 8 | `warning: implicit conversion from 'UvmGpuCompressionType' to 'UvmRmGpuCompressionType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 35 | 8 | 8 | `warning: implicit conversion from 'UvmGpuFormatElementBits' to 'UvmRmGpuFormatElementBits' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 36 | 8 | 8 | `warning: implicit conversion from 'UvmGpuFormatType' to 'UvmRmGpuFormatType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 37 | 8 | 8 | `warning: implicit conversion from 'UvmGpuMappingType' to 'UvmRmGpuMappingType' [-Wenum-conversion]` | 470xx/normal, 470xx/rt |
| 38 | 8 | 8 | `warning: unused variable 'device' [-Wunused-variable]` | 390xx/normal, 390xx/rt |
| 39 | 6 | 180 | `warning: objtool: <func>+0xADDR: indirect jump found in MITIGATION_RETPOLINE build` | 390xx/normal, 390xx/rt |
| 40 | 6 | 42 | `warning: this use of 'defined' may not be portable [-Wexpansion-to-defined]` | 580xx/normal, 580xx/rt |
| 41 | 6 | 6 | `warning: no previous prototype for '_raw_q_flush' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 42 | 6 | 6 | `warning: no previous prototype for 'block_map' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 43 | 6 | 6 | `warning: no previous prototype for 'cpu_addr_from_fake' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 44 | 6 | 6 | `warning: no previous prototype for 'fake_membar' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 45 | 6 | 6 | `warning: no previous prototype for 'fake_noop' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 46 | 6 | 6 | `warning: no previous prototype for 'fake_wait_for_idle' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 47 | 6 | 6 | `warning: no previous prototype for 'get_page_sizes' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 48 | 6 | 6 | `warning: no previous prototype for 'map_rm_pt_range' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 49 | 6 | 6 | `warning: no previous prototype for 'nv_cap_procfs_init' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 50 | 6 | 6 | `warning: no previous prototype for 'nv_dma_unmap_sgt' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 51 | 6 | 6 | `warning: no previous prototype for 'nv_firmware_path' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 52 | 6 | 6 | `warning: no previous prototype for 'nv_get_ibmnpu_chip_id' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 53 | 6 | 6 | `warning: no previous prototype for 'nv_get_num_dpaux_instances' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 54 | 6 | 6 | `warning: no previous prototype for 'nv_ibmnpu_cache_flush_numa_region' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 55 | 6 | 6 | `warning: no previous prototype for 'nv_pci_register_driver' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 56 | 6 | 6 | `warning: no previous prototype for 'nv_unregister_ibmnpu_devices' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 57 | 6 | 6 | `warning: no previous prototype for 'nvswitch_exit' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 58 | 6 | 6 | `warning: no previous prototype for 'nvswitch_init' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 59 | 6 | 6 | `warning: no previous prototype for 'os_mem_copy_custom' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 60 | 6 | 6 | `warning: no previous prototype for 'parse_fault_entry_common' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 61 | 6 | 6 | `warning: no previous prototype for 'random_channel_type' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 62 | 6 | 6 | `warning: no previous prototype for 'random_gpu' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 63 | 6 | 6 | `warning: no previous prototype for 'range_group_range_iter_advance' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 64 | 6 | 6 | `warning: no previous prototype for 'stress_test_all_gpus_in_va' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 65 | 6 | 6 | `warning: no previous prototype for 'test_memset_rm_mem' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 66 | 6 | 6 | `warning: no previous prototype for 'test_ordering' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 67 | 6 | 6 | `warning: no previous prototype for 'test_page_tree_alloc_table' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 68 | 6 | 6 | `warning: no previous prototype for 'test_push_interleaving' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 69 | 6 | 6 | `warning: no previous prototype for 'test_tracker_add_tracker' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 70 | 6 | 6 | `warning: no previous prototype for 'test_tracker_overwrite' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 71 | 6 | 6 | `warning: no previous prototype for 'test_tracking' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 72 | 6 | 6 | `warning: no previous prototype for 'timestamp_on_complete' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 73 | 6 | 6 | `warning: no previous prototype for 'try_get_ptes' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 74 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_check_channel_va_space' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 75 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_flush_deferred_work' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 76 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_get_page_thrashing_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 77 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_get_prefetch_faults_reenable_lapse' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 78 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_range_group_range_count' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 79 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_range_group_range_info' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 80 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_set_page_prefetch_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 81 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_set_page_thrashing_policy' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 82 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_set_prefetch_faults_reenable_lapse' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 83 | 6 | 6 | `warning: no previous prototype for 'uvm8_test_set_prefetch_filtering' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 84 | 6 | 6 | `warning: no previous prototype for 'uvm_api_disable_peer_access' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 85 | 6 | 6 | `warning: no previous prototype for 'uvm_api_enable_peer_access' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 86 | 6 | 6 | `warning: no previous prototype for 'uvm_channel_manager_print_pending_pushes' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 87 | 6 | 6 | `warning: no previous prototype for 'uvm_gpu_get_by_uuid_and_swizz_id_locked' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 88 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_client_id_to_utlb_id_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 89 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_kepler_mmu_engine_id_to_type_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 90 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_pascal_fault_buffer_parse_non_replayable_entry_unsupported' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 91 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_pascal_mmu_client_id_to_utlb_id' [-Wmissing-prototypes]` | 470xx/normal, 470xx/rt |
| 92 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_clear_valid' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 93 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_is_valid' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 94 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_entry_size' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 95 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_access_counter_buffer_parse_entry' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 96 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_disable_access_counter_notifications' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 97 | 6 | 6 | `warning: no previous prototype for 'uvm_hal_volta_enable_access_counter_notifications' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 98 | 6 | 6 | `warning: no previous prototype for 'uvm_pushbuffer_get_size' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 99 | 6 | 6 | `warning: no previous prototype for 'uvm_pushbuffer_update_progress' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 100 | 6 | 6 | `warning: no previous prototype for 'uvm_range_group_range_next' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 101 | 6 | 6 | `warning: no previous prototype for 'uvm_range_group_range_prev' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 102 | 6 | 6 | `warning: no previous prototype for 'uvm_va_range_remove_gpu_va_space_managed' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 103 | 6 | 6 | `warning: no previous prototype for 'va_block_set_read_duplication_locked' [-Wmissing-prototypes]` | 390xx/normal, 390xx/rt |
| 104 | 4 | 4 | `warning: conflicting types for 'nv_encode_caching' due to enum/integer mismatch; have 'int(pgprot_t *, NvU32,  nv_memory_type_t)' {aka 'int(struct pgprot *, unsigned int,  nv_memory_type_t)'} [-Wenum-int-mismatch]` | 470xx/normal |
| 105 | 4 | 4 | `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]` | 580xx/normal |
| 106 | 3 | 495 | `warning: unused variable 'chip' [-Wunused-variable]` | 580xx/normal |
| 107 | 2 | 8 | `warning: conflicting types for 'vm_flags_clear'; have 'void(struct vm_area_struct *, vm_flags_t)' {aka 'void(struct vm_area_struct *, long unsigned int)'}` | 390xx/normal, 390xx/rt |
| 108 | 2 | 8 | `warning: conflicting types for 'vm_flags_set'; have 'void(struct vm_area_struct *, vm_flags_t)' {aka 'void(struct vm_area_struct *, long unsigned int)'}` | 390xx/normal, 390xx/rt |

### ⚙️ Informational (build system / Makefile)

_None._

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

| Build | Hits | Signature |
|-------|-----:|-----------|
| 390xx/normal/6.12.109-1-MANJARO | 1 | `warning: objtool: .rodata+0x  LD [M]  /build/official/extra/linux612-extramodules/nvidia-390xx/src/nvidia/390.157/build/nvidia-drm.o` |

## 🚫 Not built (no make.log)

- `nvidia / normal / linux54-nvidia`
- `390xx / normal / linux54-nvidia-390xx`
- `470xx / normal / linux54-nvidia-470xx`
- `nvidia-open / normal / linux54-nvidia-open`
- `nvidia / normal / linux61-nvidia`
- `580xx-open / normal / linux61-nvidia-580xx-open`
- `nvidia-open / normal / linux61-nvidia-open`
- `nvidia / rt / linux61-rt-nvidia`
- `580xx-open / rt / linux61-rt-nvidia-580xx-open`
- `nvidia-open / rt / linux61-rt-nvidia-open`
- `nvidia / normal / linux612-nvidia`
- `580xx-open / normal / linux612-nvidia-580xx-open`
- `nvidia-open / normal / linux612-nvidia-open`
- `nvidia / rt / linux612-rt-nvidia`
- `580xx-open / rt / linux612-rt-nvidia-580xx-open`
- `nvidia-open / rt / linux612-rt-nvidia-open`
- `nvidia / normal / linux618-nvidia`
- `580xx-open / normal / linux618-nvidia-580xx-open`
- `nvidia-open / normal / linux618-nvidia-open`
- `nvidia / rt / linux618-rt-nvidia`
- `390xx / rt / linux618-rt-nvidia-390xx`
- `470xx / rt / linux618-rt-nvidia-470xx`
- `nvidia-open / rt / linux618-rt-nvidia-open`
- `nvidia / normal / linux66-nvidia`
- `580xx-open / normal / linux66-nvidia-580xx-open`
- `nvidia-open / normal / linux66-nvidia-open`
- `nvidia / rt / linux66-rt-nvidia`
- `580xx-open / rt / linux66-rt-nvidia-580xx-open`
- `nvidia-open / rt / linux66-rt-nvidia-open`
- `nvidia / normal / linux71-nvidia`
- `580xx-open / normal / linux71-nvidia-580xx-open`
- `nvidia-open / normal / linux71-nvidia-open`
- `nvidia / normal / linux72-nvidia`
- `580xx-open / normal / linux72-nvidia-580xx-open`
- `nvidia-open / normal / linux72-nvidia-open`
- `nvidia / normal / linux73-nvidia`
- `580xx-open / normal / linux73-nvidia-580xx-open`
- `nvidia-open / normal / linux73-nvidia-open`

---
_End of index. Per-build detail files live in the harvest tree._
