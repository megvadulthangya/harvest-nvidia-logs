# Harvest Index — 2026-10-23 06:40:45 

## TL;DR

- **State:** ❗0 failed · 🔍0 suspicious · ⚠2 warnings · ✅8 clean · 🚫11 not-built
- **Action needed (1):**
    - 2 builds · 10 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 21 — ❗0 failed, 🔍0 suspicious, ⚠2 warn, ✅8 clean, 🚫11 not-built
- **Warning signatures:** 1 total — 1 actionable across multiple builds, 0 informational, 0 unique to one build
- **Suspicious signatures:** 0  ·  **integrity issues:** 0 builds  ·  **integrity notes:** 0 builds

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
| 1 | 340xx | normal | linux61-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 2 | 340xx | normal | linux612-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 3 | 340xx | normal | linux618-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 4 | 340xx | normal | linux66-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 5 | 340xx | normal | linux71-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 6 | 340xx | normal | linux72-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 7 | 340xx | normal | linux73-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 8 | 340xx | rt | linux61-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 9 | 340xx | rt | linux612-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 10 | 340xx | rt | linux66-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 11 | 390xx | normal | 6.1.189-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 12 | 390xx | normal | 6.12.112-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 13 | 390xx | normal | 6.18.55-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.6.158-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 15 | 390xx | normal | 7.2.9-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.3.0-next-20261022-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 17 | 390xx | normal | 7.3.0-rc6-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 18 | 390xx | normal | linux71-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 19 | 390xx | rt | 6.1.182-1-rt67-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 20 | 390xx | rt | 6.12.100-1-rt20-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 21 | 390xx | rt | 6.6.151-1-rt78-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 2 | 10 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 390xx/rt |

### ⚙️ Informational (build system / Makefile)

_None._

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

## 🚫 Not built (no make.log)

- `340xx / normal / linux61-nvidia-340xx`
- `340xx / normal / linux612-nvidia-340xx`
- `340xx / normal / linux618-nvidia-340xx`
- `340xx / normal / linux66-nvidia-340xx`
- `340xx / normal / linux71-nvidia-340xx`
- `340xx / normal / linux72-nvidia-340xx`
- `340xx / normal / linux73-nvidia-340xx`
- `340xx / rt / linux61-rt-nvidia-340xx`
- `340xx / rt / linux612-rt-nvidia-340xx`
- `340xx / rt / linux66-rt-nvidia-340xx`
- `390xx / normal / linux71-nvidia-390xx`

---
_End of index. Per-build detail files live in the harvest tree._
