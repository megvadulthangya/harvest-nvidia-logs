#!/usr/bin/env bash
#
# clean-nvidia-container.sh
#
# Container-friendly nvidia cleanup.
# Removes ONLY the nvidia packages and their kernel module artifacts.
# Never touches unrelated packages (dkms, gcc, libdrm, libglvnd, ...).
#
# Usage:
#   clean-nvidia-container.sh [driver]
#     driver: optional. "340xx", "390xx", etc. If omitted, cleans all.
#
set -uo pipefail

DRIVER="${1:-}"

info() { echo "[clean] $*"; }

# Build the pacman grep pattern.
if [ -n "$DRIVER" ]; then
  pattern="^(nvidia-${DRIVER}.*|opencl-nvidia-${DRIVER}.*|mhwd-nvidia-${DRIVER}.*|lib32-(nvidia|opencl-nvidia)-${DRIVER}.*|linux.*-nvidia-${DRIVER}.*)\$"
else
  pattern="^(nvidia-(340xx|390xx|470xx|580xx).*|opencl-nvidia-(340xx|390xx|470xx|580xx).*|mhwd-nvidia-(340xx|390xx|470xx|580xx).*|lib32-(nvidia|opencl-nvidia)-(340xx|390xx|470xx|580xx).*|linux.*-nvidia-(340xx|390xx|470xx|580xx).*)\$"
fi

# --- 1. pacman packages — ONLY the nvidia ones, no dependency cascade ------
pkgs=$(pacman -Qq 2>/dev/null | grep -E "$pattern" | sort -u || true)
if [ -n "$pkgs" ]; then
  info "uninstalling nvidia packages (no dependency cascade):"
  echo "$pkgs" | sed 's/^/    /'
  # -Rdd: remove exactly these packages, ignore dependency checks.
  # The package's own .INSTALL hooks still run (dkms cleanup, etc.).
  # shellcheck disable=SC2086
  pacman -Rdd --noconfirm $pkgs 2>&1 | sed 's/^/    /' || true
else
  info "no matching nvidia packages installed"
fi

# --- 2. DKMS modules --------------------------------------------------------
if command -v dkms >/dev/null 2>&1; then
  dkms status 2>/dev/null \
    | awk -F'[/,]' '/nvidia/{print $1"/"$2}' \
    | sort -u \
    | while read -r v; do
        [ -z "$v" ] && continue
        info "dkms remove $v"
        dkms remove "$v" --all 2>&1 | sed 's/^/    /' || true
      done
fi

# --- 3. Filesystem leftovers (nvidia only) ---------------------------------
for p in \
  /usr/src/nvidia-* \
  /var/lib/dkms/nvidia* \
  /usr/share/vulkan/icd.d/nvidia_icd.json \
  /usr/share/glvnd/egl_vendor.d/10_nvidia.json \
  /etc/ld.so.conf.d/nvidia*.conf \
  /etc/modprobe.d/nvidia*.conf \
  /etc/modprobe.d/blacklist-nvidia*.conf \
  /etc/modules-load.d/nvidia*.conf \
  /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf \
  /etc/mhwd.d/nvidia*.conf \
  ; do
  if compgen -G "$p" >/dev/null 2>&1; then
    info "rm -rf $p"
    # shellcheck disable=SC2086
    rm -rf -- $p 2>/dev/null || true
  fi
done

# --- 4. Library leftovers ---------------------------------------------------
find /usr/lib /usr/lib32 -maxdepth 2 \( \
  -name 'libnvidia*' -o \
  -name 'libcuda*' -o \
  -name 'libGLX_nvidia*' -o \
  -name 'libEGL_nvidia*' -o \
  -name 'libnvcuvid*' \
  \) -delete 2>/dev/null || true

info "done"