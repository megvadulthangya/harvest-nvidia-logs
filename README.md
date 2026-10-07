# Harvest Index — 2026-10-07 07:58:57 

## TL;DR

- **State:** ❗0 failed · 🔍0 suspicious · ⚠18 warnings · ✅2 clean · 🚫0 not-built
- **Action needed (2):**
    - 8 builds · 36 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
    - 8 builds · 8 hits · `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]`
- **Informational:** 4 build-system signature(s) — no driver fix needed
- **Since last run (`2026-10-05T14-31-39`):** ✅0 resolved · 🆕0 new · 🔀0 status changes

## 📊 Changes since 2026-10-05T14-31-39

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
- **Builds:** 20 — ❗0 failed, 🔍0 suspicious, ⚠18 warn, ✅2 clean, 🚫0 not-built
- **Warning signatures:** 6 total — 2 actionable across multiple builds, 4 informational, 0 unique to one build
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
| 11 | 390xx | normal | 6.1.187-2-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164942 |  |
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

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 8 | 36 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt, 390xx/normal, 390xx/rt |
| 2 | 8 | 8 | `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]` | 340xx/normal, 390xx/normal |

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

---
_End of index. Per-build detail files live in the harvest tree._
