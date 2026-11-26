# Harvest Index — 2026-11-26 22:33:52 

## TL;DR

- **State:** ❗4 failed · 🔍0 suspicious · ⚠18 warnings · ✅8 clean · 🚫0 not-built
- **Action needed (4):**
    - 14 builds · 62 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
    - 10 builds · 10 hits · `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]`
    - 3 builds · 3 hits · `warning: '__fbdev_warning' defined but not used [-Wunused-variable]`
    - … and 1 more (see `## 🔁 Cross-build warning signatures`)
- **Informational:** 4 build-system signature(s) — no driver fix needed

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx, 470xx
- **Builds:** 30 — ❗4 failed, 🔍0 suspicious, ⚠18 warn, ✅8 clean, 🚫0 not-built
- **Warning signatures:** 8 total — 4 actionable across multiple builds, 4 informational, 0 unique to one build
- **Suspicious signatures:** 2  ·  **integrity issues:** 0 builds  ·  **integrity notes:** 0 builds

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
| 1 | 340xx | normal | 6.1.192-2-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.117-1-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.63-3-MANJARO | 340.108 | ⚠ warnings | 0 | 4 / 7 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.162-2-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 5 | 340xx | normal | 7.3.4-3-MANJARO | 340.108 | ⚠ warnings | 0 | 6 / 9 | 0 | 0 |  |
| 6 | 340xx | normal | 7.4.0-rc2-3-MANJARO | 340.108 | ⚠ warnings | 0 | 6 / 9 | 0 | 0 |  |
| 7 | 340xx | normal | linux-next-nvidia-340xx | — | ❗ failed | 12 | 2 / 2 | 3 | 0 |  |
| 8 | 340xx | rt | 6.1.190-2-rt70-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 9 | 340xx | rt | 6.12.116-1-rt22-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 10 | 340xx | rt | 6.6.159-2-rt82-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 11 | 390xx | normal | 6.1.192-2-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164941 |  |
| 12 | 390xx | normal | 6.12.117-1-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 13 | 390xx | normal | 6.18.63-3-MANJARO | 390.157 | ⚠ warnings | 0 | 2 / 6 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.6.162-2-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 15 | 390xx | normal | 7.3.4-3-MANJARO | 390.157 | ⚠ warnings | 0 | 2 / 6 | 0 | 94474 |  |
| 16 | 390xx | normal | linux-next-nvidia-390xx | — | ❗ failed | 6 | 0 / 0 | 0 | 0 |  |
| 17 | 390xx | normal | linux74-nvidia-390xx | — | ❗ failed | 9 | 2 / 5 | 0 | 0 |  |
| 18 | 390xx | rt | 6.1.190-2-rt70-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164941 |  |
| 19 | 390xx | rt | 6.12.116-1-rt22-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 20 | 390xx | rt | 6.6.159-2-rt82-MANJARO | 390.157 | ⚠ warnings | 0 | 1 / 5 | 0 | 94474 |  |
| 21 | 470xx | normal | 6.1.192-2-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 157265 |  |
| 22 | 470xx | normal | 6.12.117-1-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 63696 |  |
| 23 | 470xx | normal | 6.18.63-3-MANJARO | 470.256.02 | ⚠ warnings | 0 | 1 / 1 | 0 | 63696 |  |
| 24 | 470xx | normal | 6.6.162-2-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 63696 |  |
| 25 | 470xx | normal | 7.3.4-3-MANJARO | 470.256.02 | ⚠ warnings | 0 | 1 / 1 | 0 | 63696 |  |
| 26 | 470xx | normal | 7.3.4-3-MANJARO | 470.256.02 | ⚠ warnings | 0 | 1 / 1 | 0 | 63696 |  |
| 27 | 470xx | normal | linux-next-nvidia-470xx | — | ❗ failed | 71 | 1 / 1 | 0 | 0 |  |
| 28 | 470xx | rt | 6.1.190-2-rt70-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 157265 |  |
| 29 | 470xx | rt | 6.12.116-1-rt22-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 63696 |  |
| 30 | 470xx | rt | 6.6.159-2-rt82-MANJARO | 470.256.02 | ✅ clean | 0 | 0 / 0 | 0 | 63696 |  |

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 340xx / normal / linux-next-nvidia-340xx — ?  (12 errors)

Path: `340xx/normal/linux-next-nvidia-340xx`

```
216: nv.c:935:9: error: implicit declaration of function ‘rdmsr’; did you mean ‘rdmsrq’? [-Wimplicit-function-declaration]
227: make[4]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:321: nv.o] Error 1
229: make[3]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:2252: .] Error 2
230: make[2]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:248: __sub-make] Error 2
232: make[1]: *** [Makefile:248: __sub-make] Error 2
234: make: *** [Makefile:225: nvidia.ko] Error 2
255: make[5]: *** No rule to make target 'Makefile'.  Stop.
256: make[4]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:2252: .] Error 2
257: make[3]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:248: __sub-make] Error 2
259: make[2]: *** [Makefile:248: __sub-make] Error 2
261: make[1]: *** [Makefile:225: nvidia.ko] Error 2
263: make: *** [Makefile:226: ../Module.symvers] Error 2
```

### 390xx / normal / linux-next-nvidia-390xx — ?  (6 errors)

Path: `390xx/normal/linux-next-nvidia-390xx`

```
533: nvidia/nv.c:1054:9: error: implicit declaration of function ‘rdmsr’; did you mean ‘rdmsrq’? [-Wimplicit-function-declaration]
537: make[4]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:321: nvidia/nv.o] Error 1
539: make[3]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:2252: .] Error 2
540: make[2]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/Makefile:248: __sub-make] Error 2
542: make[1]: *** [Makefile:248: __sub-make] Error 2
544: make: *** [Makefile:93: modules] Error 2
```

### 390xx / normal / linux74-nvidia-390xx — ?  (9 errors)

Path: `390xx/normal/linux74-nvidia-390xx`

```
735: nvidia-drm/nvidia-drm-crtc.c:181:6: error: ‘const struct drm_plane_funcs’ has no member named ‘reset’
739: nvidia-drm/nvidia-drm-crtc.c:181:31: error: ‘drm_atomic_helper_plane_reset’ undeclared here (not in a function); did you mean ‘drm_atomic_helper_page_flip’?
743: nvidia-drm/nvidia-drm-crtc.c:294:6: error: ‘struct drm_crtc_funcs’ has no member named ‘reset’
746: nvidia-drm/nvidia-drm-crtc.c:294:31: error: ‘drm_atomic_helper_crtc_reset’ undeclared here (not in a function); did you mean ‘drm_atomic_helper_check_modeset’?
750: make[4]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/scripts/Makefile.build:290: nvidia-drm/nvidia-drm-crtc.o] Error 1
752: make[3]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:2244: .] Error 2
753: make[2]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:248: __sub-make] Error 2
755: make[1]: *** [Makefile:248: __sub-make] Error 2
757: make: *** [Makefile:93: modules] Error 2
```

### 470xx / normal / linux-next-nvidia-470xx — ?  (71 errors)

Path: `470xx/normal/linux-next-nvidia-470xx`

```
669: nvidia/nv-pat.c:37:43: error: implicit declaration of function ‘rdmsr’; did you mean ‘rdmsrq’? [-Wimplicit-function-declaration]
675: make[4]: *** [/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:321: nvidia/nv-pat.o] Error 1
679: ././common/inc/nv-procfs-utils.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
691: ././common/inc/nv-procfs-utils.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
707: ././common/inc/nv-procfs-utils.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
728: ././common/inc/nv-procfs-utils.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
740: ././common/inc/nv-procfs-utils.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
756: ././common/inc/nv-procfs-utils.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
773: ././common/inc/nv-procfs-utils.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
785: ././common/inc/nv-procfs-utils.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
801: ././common/inc/nv-procfs-utils.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
818: ././common/inc/nv-procfs-utils.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
830: ././common/inc/nv-procfs-utils.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
846: ././common/inc/nv-procfs-utils.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
863: ././common/inc/nv-procfs-utils.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
```

## 🔍 Suspicious signatures

Lines that are **not** errors and **not** warnings, but contain keywords that often indicate real problems (missing files, permissions, OOM, crashes, missing deps).

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 1 | 2 | `mkdir: cannot create directory '.tmp_NNN': Permission denied` | 340xx/normal |
| 2 | 1 | 1 | `/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |

<details><summary>Context excerpts (first few hits per signature)</summary>

**`mkdir: cannot create directory '.tmp_NNN': Permission denied`**

```
[340xx/normal/linux-next-nvidia-340xx] 250: mkdir: cannot create directory ‘.tmp_20605’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 251: mkdir: cannot create directory ‘.tmp_20608’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 254: /usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
```

**`/usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux-next-nvidia-340xx] 250: mkdir: cannot create directory ‘.tmp_20605’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 251: mkdir: cannot create directory ‘.tmp_20608’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 254: /usr/lib/modules/7.4.0-rc4-next-20261124-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
```

</details>

## 🔁 Cross-build warning signatures

Warnings appearing in **more than one build**. Fixing the top signature fixes the most builds at once.

### 🎯 Actionable (driver source)

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 14 | 62 | `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]` | 340xx/normal, 340xx/rt, 390xx/normal, 390xx/rt |
| 2 | 10 | 10 | `warning: ignoring return value of 'refcount_sub_and_test' declared with attribute 'warn_unused_result' [-Wunused-result]` | 340xx/normal, 390xx/normal, 470xx/normal |
| 3 | 3 | 3 | `warning: '__fbdev_warning' defined but not used [-Wunused-variable]` | 340xx/normal |
| 4 | 3 | 3 | `warning: 'nv_fbdev_failure_detected' defined but not used [-Wunused-variable]` | 340xx/normal |

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

---
_End of index. Per-build detail files live in the harvest tree._
