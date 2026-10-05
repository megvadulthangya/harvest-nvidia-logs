#!/usr/bin/env bash
#
# clean-nvidia-container.sh
#
# Container-friendly nvidia cleanup.
# Removes ONLY the nvidia packages and their kernel module artifacts.
# Never touches unrelated packages (dkms, gcc, libdrm, libglvnd, ...).
#
# Supports:
#   - legacy branches:  340xx, 390xx, 470xx, 580xx, 580xx-open
#   - current branch:   current  (nvidia-utils, nvidia-open-dkms, ...)
#
# Usage:
#   clean-nvidia-container.sh [driver]
#     driver: "340xx" | "390xx" | "470xx" | "580xx" | "current"
#             If omitted, cleans all known branches.
#
set -uo pipefail

DRIVER="${1:-}"

info() { echo "[clean] $*"; }

# --- Build pacman pattern ---------------------------------------------------
if [ -n "$DRIVER" ]; then
  if [ "$DRIVER" = "current" ]; then
    # Current branch: package names have no version suffix.
    # Matches nvidia, nvidia-open, nvidia-utils, nvidia-dkms,
    # nvidia-open-dkms, opencl-nvidia, lib32-nvidia-utils, ...
    pattern="^(nvidia|nvidia-open|nvidia-utils|nvidia-dkms|nvidia-open-dkms|opencl-nvidia|lib32-nvidia-utils|lib32-opencl-nvidia|lib32-nvidia|mhwd-nvidia|mhwd-db|mhwd)\$"
  else
    # Legacy branch. The trailing .* also covers -open variants, so
    # nvidia-580xx.* matches nvidia-580xx-open-dkms as well.
    pattern="^(nvidia-${DRIVER}.*|opencl-nvidia-${DRIVER}.*|mhwd-nvidia-${DRIVER}.*|lib32-(nvidia|opencl-nvidia)-${DRIVER}.*|linux.*-nvidia-${DRIVER}.*|mhwd-db|mhwd)\$"
  fi
else
  pattern="^(nvidia|nvidia-open|nvidia-utils|nvidia-dkms|nvidia-open-dkms|opencl-nvidia|lib32-nvidia-utils|lib32-opencl-nvidia|lib32-nvidia|mhwd-nvidia|nvidia-(340xx|390xx|470xx|580xx|580xx-open).*|opencl-nvidia-(340xx|390xx|470xx|580xx|580xx-open).*|mhwd-nvidia-(340xx|390xx|470xx|580xx|580xx-open).*|lib32-(nvidia|opencl-nvidia)-(340xx|390xx|470xx|580xx|580xx-open).*|linux.*-nvidia-(340xx|390xx|470xx|580xx|580xx-open).*|mhwd-db|mhwd)\$"
fi

# --- 1. pacman packages -----------------------------------------------------
pkgs=$(pacman -Qq 2>/dev/null | grep -E "$pattern" | sort -u || true)
if [ -n "$pkgs" ]; then
  info "uninstalling (no dependency cascade):"
  echo "$pkgs" | sed 's/^/    /'
  # -Rdd: remove exactly these packages, ignore dependency checks.
  # shellcheck disable=SC2086
  pacman -Rdd --noconfirm $pkgs 2>&1 | sed 's/^/    /' || true
else
  info "no matching packages installed"
fi

# --- 2. DKMS state (all versions, closed + open) ----------------------------
for d in /var/lib/dkms/nvidia /var/lib/dkms/nvidia-open; do
  [ -e "$d" ] || continue
  info "rm -rf $d"
  rm -rf -- "$d" 2>/dev/null || true
done

# --- 3. DKMS registry -------------------------------------------------------
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

# --- 4. Filesystem leftovers (nvidia only) ---------------------------------
for p in \
  /usr/src/nvidia-* \
  /usr/share/vulkan/icd.d/nvidia_icd.json \
  /usr/share/glvnd/egl_vendor.d/10_nvidia.json \
  /etc/ld.so.conf.d/nvidia*.conf \
  /etc/ld.so.conf.d/00-nvidia.conf \
  /etc/modprobe.d/nvidia*.conf \
  /etc/modprobe.d/blacklist-nvidia*.conf \
  /etc/modules-load.d/nvidia*.conf \
  /etc/X11/xorg.conf.d/10-nvidia-drm-outputclass.conf \
  /etc/X11/xorg.conf.d/20-nvidia-*.conf \
  /etc/mhwd.d/nvidia*.conf \
  /var/lib/mhwd/ids/pci/nvidia-*.ids \
  ; do
  if compgen -G "$p" >/dev/null 2>&1; then
    info "rm -rf $p"
    # shellcheck disable=SC2086
    rm -rf -- $p 2>/dev/null || true
  fi
done

# --- 5. Library leftovers ---------------------------------------------------
find /usr/lib /usr/lib32 -maxdepth 2 \( \
  -name 'libnvidia*' -o \
  -name 'libcuda*' -o \
  -name 'libGLX_nvidia*' -o \
  -name 'libEGL_nvidia*' -o \
  -name 'libnvcuvid*' \
  \) -delete 2>/dev/null || true

info "done"