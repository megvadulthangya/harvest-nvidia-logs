# Harvest Index — 2026-11-22 11:32:45 

## TL;DR

- **State:** ❗3 failed · 🔍0 suspicious · ⚠8 warnings · ✅9 clean · 🚫0 not-built
- **⚠ Integrity issues:** 1 build(s) affected — see `## 🧱 Integrity issues` below
- **Action needed (1):**
    - 2 builds · 8 hits · `warning: Please avoid flushing system-wide workqueues. [-Wattribute-warning]`
- **Informational:** 4 build-system signature(s) — no driver fix needed

## Overview

- **Diag root:** `/build/sources`
- **Harvest:**   `/build/harvest`
- **Branches:**  340xx, 390xx
- **Builds:** 20 — ❗3 failed, 🔍0 suspicious, ⚠8 warn, ✅9 clean, 🚫0 not-built
- **Warning signatures:** 5 total — 1 actionable across multiple builds, 4 informational, 0 unique to one build
- **Suspicious signatures:** 3  ·  **integrity issues:** 1 builds  ·  **integrity notes:** 0 builds

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

For non-clean builds (warnings, suspicious, failures), the raw `make.log` is archived in the same directory as `make.log.zst` (or `.gz` / plain).

## Status table

| # | Branch | Variant | Kernel | Driver | Status | Err | Clean (uniq/total) | Susp | Noise | Integ |
|---|--------|---------|--------|--------|:------:|----:|-------------------:|-----:|------:|:-----:|
| 1 | 340xx | normal | 6.1.192-2-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 2 | 340xx | normal | 6.12.117-1-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 3 | 340xx | normal | 6.18.63-3-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 0 |  |
| 4 | 340xx | normal | 6.6.162-2-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 5 | 340xx | normal | 7.3.4-3-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 0 |  |
| 6 | 340xx | normal | linux-next-nvidia-340xx | — | ❗ failed | 42 | 0 / 0 | 3 | 0 |  |
| 7 | 340xx | normal | linux74-nvidia-340xx | — | ❗ failed | 11 | 0 / 0 | 3 | 0 | ! |
| 8 | 340xx | rt | 6.1.190-2-rt70-MANJARO | 340.108 | ⚠ warnings | 0 | 3 / 6 | 0 | 1 |  |
| 9 | 340xx | rt | 6.12.116-1-rt22-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 10 | 340xx | rt | 6.6.159-2-rt82-MANJARO | 340.108 | ⚠ warnings | 0 | 2 / 2 | 0 | 1 |  |
| 11 | 390xx | normal | 6.1.192-2-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164941 |  |
| 12 | 390xx | normal | 6.12.117-1-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 13 | 390xx | normal | 6.18.63-3-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 14 | 390xx | normal | 6.6.162-2-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 15 | 390xx | normal | 7.3.4-3-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 16 | 390xx | normal | 7.4.0-rc2-3-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 17 | 390xx | normal | linux-next-nvidia-390xx | — | ❗ failed | 40 | 0 / 0 | 0 | 0 |  |
| 18 | 390xx | rt | 6.1.190-2-rt70-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 164941 |  |
| 19 | 390xx | rt | 6.12.116-1-rt22-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |
| 20 | 390xx | rt | 6.6.159-2-rt82-MANJARO | 390.157 | ✅ clean | 0 | 0 / 0 | 0 | 94474 |  |

## 🧱 Integrity issues

Structural problems detected between the **log** and the **build tree** — these likely indicate a silent failure.

### 340xx / normal / linux74-nvidia-340xx

Path: `340xx/normal/linux74-nvidia-340xx`  ·  modules on disk: 0 [—]  ·  log LD [M]: ['nvidia']

- log claims to link modules ['nvidia'] but no matching .ko/.ko.zst found on disk

## ❗ Failures — fix these first

Full error list in each build's `01-errors.txt`. Excerpt below.

### 340xx / normal / linux-next-nvidia-340xx — ?  (42 errors)

Path: `340xx/normal/linux-next-nvidia-340xx`

```
237: nv-linux.h:1975:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
246: nv-linux.h:2082:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
256: nv-linux.h:2082:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
270: nv-linux.h:1975:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
279: nv-linux.h:2082:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
289: nv-linux.h:2082:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
300: nv-linux.h:1975:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
309: nv-linux.h:2082:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
319: nv-linux.h:2082:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
330: nv-linux.h:1975:29: error: ‘nv_proc_ops_t’ {aka ‘struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
336: nv-procfs.c:415:28: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
340: nv-procfs.c:415:28: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
345: nv-linux.h:1976:29: error: ‘nv_proc_ops_t’ {aka ‘struct proc_ops’} has no member named ‘proc_write’; did you mean ‘proc_write_buf’?
351: nv-procfs.c:416:28: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
355: nv-procfs.c:416:28: error: initialization of ‘int (*)(struct inode *, struct file *)’ from incompatible pointer type ‘ssize_t (*)(struct file *, const char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, const char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
```

### 340xx / normal / linux74-nvidia-340xx — ?  (11 errors)

Path: `340xx/normal/linux74-nvidia-340xx`

```
267: make[4]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/scripts/Makefile.modpost:147: Module.symvers] Error 1
268: make[3]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:2194: modpost] Error 2
269: make[2]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:248: __sub-make] Error 2
271: make[1]: *** [Makefile:248: __sub-make] Error 2
273: make: *** [Makefile:224: nvidia.ko] Error 2
293: make[5]: *** No rule to make target 'Makefile'.  Stop.
294: make[4]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:2244: .] Error 2
295: make[3]: *** [/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/Makefile:248: __sub-make] Error 2
297: make[2]: *** [Makefile:248: __sub-make] Error 2
299: make[1]: *** [Makefile:224: nvidia.ko] Error 2
301: make: *** [Makefile:226: ../Module.symvers] Error 2
```

### 390xx / normal / linux-next-nvidia-390xx — ?  (40 errors)

Path: `390xx/normal/linux-next-nvidia-390xx`

```
549: ././common/inc/nv-procfs.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
558: ././common/inc/nv-procfs.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
568: ././common/inc/nv-procfs.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
582: ././common/inc/nv-procfs.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
591: ././common/inc/nv-procfs.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
601: ././common/inc/nv-procfs.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
612: ././common/inc/nv-procfs.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘const struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
621: ././common/inc/nv-procfs.h:144:32: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
631: ././common/inc/nv-procfs.h:144:32: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
642: ././common/inc/nv-procfs.h:37:29: error: ‘nv_proc_ops_t’ {aka ‘struct proc_ops’} has no member named ‘proc_read’; did you mean ‘proc_mmap’?
648: nvidia/nv-procfs.c:420:28: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
652: nvidia/nv-procfs.c:420:28: error: initialization of ‘loff_t (*)(struct file *, loff_t,  int)’ {aka ‘long long int (*)(struct file *, long long int,  int)’} from incompatible pointer type ‘ssize_t (*)(struct file *, char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
657: ././common/inc/nv-procfs.h:38:29: error: ‘nv_proc_ops_t’ {aka ‘struct proc_ops’} has no member named ‘proc_write’; did you mean ‘proc_write_buf’?
663: nvidia/nv-procfs.c:421:28: error: positional initialization of field in ‘struct’ declared with ‘designated_init’ attribute [-Werror=designated-init]
667: nvidia/nv-procfs.c:421:28: error: initialization of ‘int (*)(struct inode *, struct file *)’ from incompatible pointer type ‘ssize_t (*)(struct file *, const char *, size_t,  loff_t *)’ {aka ‘long int (*)(struct file *, const char *, long unsigned int,  long long int *)’} [-Wincompatible-pointer-types]
```

## 🔍 Suspicious signatures

Lines that are **not** errors and **not** warnings, but contain keywords that often indicate real problems (missing files, permissions, OOM, crashes, missing deps).

| # | Builds | Hits | Signature | Branches |
|---|-------:|-----:|-----------|----------|
| 1 | 2 | 4 | `mkdir: cannot create directory '.tmp_NNN': Permission denied` | 340xx/normal |
| 2 | 1 | 1 | `/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |
| 3 | 1 | 1 | `/usr/lib/modules/7.4.0-rc3-next-20261119-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory` | 340xx/normal |

<details><summary>Context excerpts (first few hits per signature)</summary>

**`mkdir: cannot create directory '.tmp_NNN': Permission denied`**

```
[340xx/normal/linux-next-nvidia-340xx] 512: mkdir: cannot create directory ‘.tmp_25225’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 513: mkdir: cannot create directory ‘.tmp_25228’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 516: /usr/lib/modules/7.4.0-rc3-next-20261119-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
[340xx/normal/linux74-nvidia-340xx] 289: mkdir: cannot create directory ‘.tmp_131885’: Permission denied
[340xx/normal/linux74-nvidia-340xx] 290: mkdir: cannot create directory ‘.tmp_131888’: Permission denied
```

**`/usr/lib/modules/7.4.0-rc2-3-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux74-nvidia-340xx] 289: mkdir: cannot create directory ‘.tmp_131885’: Permission denied
[340xx/normal/linux74-nvidia-340xx] 290: mkdir: cannot create directory ‘.tmp_131888’: Permission denied
[340xx/normal/linux74-nvidia-340xx] 292: /usr/lib/modules/7.4.0-rc2-3-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
```

**`/usr/lib/modules/7.4.0-rc3-next-20261119-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory`**

```
[340xx/normal/linux-next-nvidia-340xx] 512: mkdir: cannot create directory ‘.tmp_25225’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 513: mkdir: cannot create directory ‘.tmp_25228’: Permission denied
[340xx/normal/linux-next-nvidia-340xx] 516: /usr/lib/modules/7.4.0-rc3-next-20261119-1-MANJARO/build/scripts/Makefile.build:38: Makefile: No such file or directory
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
| 3 | 2 | 2 | `warning: ignoring old recipe for target 'Module.symvers'` | 340xx/normal |
| 4 | 2 | 2 | `warning: overriding recipe for target 'Module.symvers'` | 340xx/normal |

## 🧩 Unique to one build

Warnings in exactly **one** build. Usually kernel- or config-specific.

_No unique-to-one-build warnings._

---
_End of index. Per-build detail files live in the harvest tree._
