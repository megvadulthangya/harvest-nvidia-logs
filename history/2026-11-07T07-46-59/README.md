# Harvest Index — 2026-11-07 07:46:59 

## TL;DR

- **State:** ❗0 failed · 🔍0 suspicious · ⚠10 warnings · ✅0 clean · 🚫12 not-built
- **Action needed (1):**
    - 8 builds · 32 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
- **Informational:** 4 build-system signature(s) — no driver fix needed

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 22 — ❗0 failed, 🔍0 suspicious, ⚠10 warn, ✅0 clean, 🚫12 not-built
- **Warning signatures:** 5 total — 1 actionable across multiple builds, 4 informational, 0 unique to one build
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
| 1 | 340xx | normal | 6.1.191-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.115-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.60-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.161-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 5 | 340xx | normal | 7.2.14-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 0 |  |
| 6 | 340xx | normal | 7.3.1-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 0 |  |
| 7 | 340xx | normal | 7.4.0-rc1-next-20261105-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 0 |  |
| 8 | 340xx | normal | linux71-nvidia-340xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 9 | 340xx | rt | 6.1.190-1-rt70-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 10 | 340xx | rt | 6.12.111-1-rt21-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 11 | 340xx | rt | 6.6.159-1-rt82-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 12 | 390xx | normal | linux-next-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 13 | 390xx | normal | linux61-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 14 | 390xx | normal | linux612-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 15 | 390xx | normal | linux618-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 16 | 390xx | normal | linux66-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 17 | 390xx | normal | linux71-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 18 | 390xx | normal | linux72-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 19 | 390xx | normal | linux73-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 20 | 390xx | rt | linux61-rt-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 21 | 390xx | rt | linux612-rt-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |
| 22 | 390xx | rt | linux66-rt-nvidia-390xx | — | 🚫 not-built | 0 | 0 / 0 | 0 | 0 |  |

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 8 | 32 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt |

### ⚙️ Informational (build system / Makefile)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 6 | 6 | `warning: ignoring old recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 2 | 6 | 6 | `warning: overriding recipe for target '<path>'` | 340xx/normal, 340xx/rt |
| 3 | 4 | 4 | `warning: ignoring old recipe for target 'Module.symvers'` | 340xx/normal |
| 4 | 4 | 4 | `warning: overriding recipe for target 'Module.symvers'` | 340xx/normal |

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

## 🚫 Not built (no make.log)

- `340xx / normal / linux71-nvidia-340xx`
- `390xx / normal / linux-next-nvidia-390xx`
- `390xx / normal / linux61-nvidia-390xx`
- `390xx / normal / linux612-nvidia-390xx`
- `390xx / normal / linux618-nvidia-390xx`
- `390xx / normal / linux66-nvidia-390xx`
- `390xx / normal / linux71-nvidia-390xx`
- `390xx / normal / linux72-nvidia-390xx`
- `390xx / normal / linux73-nvidia-390xx`
- `390xx / rt / linux61-rt-nvidia-390xx`
- `390xx / rt / linux612-rt-nvidia-390xx`
- `390xx / rt / linux66-rt-nvidia-390xx`

---
_End of index. Per-build detail files live in the harvest tree._
