# Harvest Index — 2026-11-09 23:26:18 

## TL;DR

- **State:** ❗0 failed · 🔍0 suspicious · ⚠0 warnings · ✅9 clean · 🚫13 not-built
- **Action needed:** none — no actionable cross-build warnings

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 22 — ❗0 failed, 🔍0 suspicious, ⚠0 warn, ✅9 clean, 🚫13 not-built
- **Warning signatures:** 0 total — 0 actionable across multiple builds, 0 informational, 0 unique to one build
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
| 1 | 340xx | normal | linux-next-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 2 | 340xx | normal | linux61-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 3 | 340xx | normal | linux612-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 4 | 340xx | normal | linux618-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 5 | 340xx | normal | linux66-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 6 | 340xx | normal | linux71-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 7 | 340xx | normal | linux72-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 8 | 340xx | normal | linux73-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 9 | 340xx | rt | linux61-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 10 | 340xx | rt | linux612-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 11 | 340xx | rt | linux66-rt-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 12 | 390xx | normal | 6.1.192-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164941 |  |
| 13 | 390xx | normal | 6.12.116-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.18.62-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 15 | 390xx | normal | 6.6.162-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.3.3-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 17 | 390xx | normal | 7.4.0-rc2-next-20261109-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 18 | 390xx | normal | linux71-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 19 | 390xx | normal | linux72-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 20 | 390xx | rt | 6.1.190-1-rt70-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
| 21 | 390xx | rt | 6.12.111-1-rt21-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 22 | 390xx | rt | 6.6.159-1-rt82-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

_None._

### ⚙️ Informational (build system / Makefile)

_None._

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

## 🚫 Not built (no make.log)

- `340xx / normal / linux-next-nvidia-340xx`
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
- `390xx / normal / linux72-nvidia-390xx`

---
_End of index. Per-build detail files live in the harvest tree._
