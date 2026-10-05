# Harvest Index — 2026-10-05 12:30:02 

## 📊 Changes since 2026-10-05T10-04-53

### ✅ Resolved signatures (1)

- `warning: objtool: _nv001  LD [M]  /build/diag/nvidia-390xx/normal-kernels/linux66-nvidia-390xx/src/nvidia/390.157/build/nvidia-drm.o`

### 🆕 New signatures (1)

- `warning: objtool: _nv002ld -m elf_x86_64 -z noexecstack --no-warn-rwx-segments -r -o /build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/nvidia-modeset/nv-modeset-interface.o /build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/nvidia-modeset/nvidia-modeset-linux.o`

### 🔀 Status changes (0)

_None._

### ➕ New builds (20)

- `340xx/normal/linux61-nvidia-340xx`
- `340xx/normal/linux612-nvidia-340xx`
- `340xx/normal/linux618-nvidia-340xx`
- `340xx/normal/linux66-nvidia-340xx`
- `340xx/normal/linux71-nvidia-340xx`
- `340xx/normal/linux72-nvidia-340xx`
- `340xx/normal/linux73-nvidia-340xx`
- `340xx/rt/linux61-rt-nvidia-340xx`
- `340xx/rt/linux612-rt-nvidia-340xx`
- `340xx/rt/linux66-rt-nvidia-340xx`
- `390xx/normal/linux61-nvidia-390xx`
- `390xx/normal/linux612-nvidia-390xx`
- `390xx/normal/linux618-nvidia-390xx`
- `390xx/normal/linux66-nvidia-390xx`
- `390xx/normal/linux71-nvidia-390xx`
- `390xx/normal/linux72-nvidia-390xx`
- `390xx/normal/linux73-nvidia-390xx`
- `390xx/rt/linux61-rt-nvidia-390xx`
- `390xx/rt/linux612-rt-nvidia-390xx`
- `390xx/rt/linux66-rt-nvidia-390xx`

### ➖ Removed builds (20)

- `340xx/normal/6.1.187-2-MANJARO`
- `340xx/normal/6.12.109-1-MANJARO`
- `340xx/normal/6.18.50-1-MANJARO`
- `340xx/normal/6.6.156-2-MANJARO`
- `340xx/normal/7.1.13-2-MANJARO`
- `340xx/normal/7.2.4-1-MANJARO`
- `340xx/normal/7.3.0-rc2-1-MANJARO`
- `340xx/rt/6.1.182-1-rt67-MANJARO`
- `340xx/rt/6.12.100-1-rt20-MANJARO`
- `340xx/rt/6.6.151-1-rt78-MANJARO`
- `390xx/normal/6.1.187-2-MANJARO`
- `390xx/normal/6.12.109-1-MANJARO`
- `390xx/normal/6.18.50-1-MANJARO`
- `390xx/normal/6.6.156-2-MANJARO`
- `390xx/normal/7.1.13-2-MANJARO`
- `390xx/normal/7.2.4-1-MANJARO`
- `390xx/normal/7.3.0-rc2-1-MANJARO`
- `390xx/rt/6.1.182-1-rt67-MANJARO`
- `390xx/rt/6.12.100-1-rt20-MANJARO`
- `390xx/rt/6.6.151-1-rt78-MANJARO`


## Overview

- **Diag root:** `/build/diag`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 20 — ❗0 failed, 🔍0 suspicious, ⚠19 warn, ✅1 clean, 🚫0 not-built
- **Warning signatures:** 7 total — 6 across multiple builds, 1 unique to one build
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
| 1 | 340xx | normal | 6.1.187-2-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.109-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.50-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 3 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.156-2-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 5 | 340xx | normal | 7.1.13-2-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 3 | 0 | 0 |  |
| 6 | 340xx | normal | 7.2.4-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 3 | 0 | 0 |  |
| 7 | 340xx | normal | 7.3.0-rc2-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 3 | 0 | 0 |  |
| 8 | 340xx | rt | 6.1.182-1-rt67-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 9 | 340xx | rt | 6.12.100-1-rt20-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 10 | 340xx | rt | 6.6.151-1-rt78-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 11 | 390xx | normal | 6.1.187-2-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 1 | 0 | 164941 |  |
| 12 | 390xx | normal | 6.12.109-1-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 13 | 390xx | normal | 6.18.50-1-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 1 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.6.156-2-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 15 | 390xx | normal | 7.1.13-2-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 1 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.2.4-1-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 1 | 0 | 94474 |  |
| 17 | 390xx | normal | 7.3.0-rc2-1-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 1 | 0 | 94474 |  |
| 18 | 390xx | rt | 6.1.182-1-rt67-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 19 | 390xx | rt | 6.12.100-1-rt20-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 20 | 390xx | rt | 6.6.151-1-rt78-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 8 | 36 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt, 390xx/normal, 390xx/rt |
| 2 | 8 | 8 | `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]` | 340xx/normal, 390xx/normal |
| 3 | 6 | 6 | `warning: ignoring old recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 4 | 6 | 6 | `warning: overriding recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 5 | 4 | 4 | `warning: ignoring old recipe for target 'Module.symvers'` | 340xx/normal |
| 6 | 4 | 4 | `warning: overriding recipe for target 'Module.symvers'` | 340xx/normal |

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

| Build | Hits | Signature |
|-------|-----:|-----------|
| 390xx/normal/6.1.187-2-MANJARO | 1 | `warning: objtool: _nv002ld -m elf_x86_64 -z noexecstack --no-warn-rwx-segments -r -o /build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/nvidia-modeset/nv-modeset-interface.o /build/diag/nvidia-390xx/normal-kernels/linux61-nvidia-390xx/src/nvidia/390.157/build/nvidia-modeset/nvidia-modeset-linux.o` |

---
_End of index. Per-build detail files live in the harvest tree._
