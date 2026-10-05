#!/usr/bin/env bash
#
# clean-nvidia-container.sh
#
# Container-friendly nvidia cleanup. Mirrors the manual workflow:
#   pacman -R  mhwd-nvidia-XXX nvidia-XXX-dkms nvidia-XXX-utils
#              opencl-nvidia-XXX mhwd-db mhwd
#   rm -rf /var/lib/dkms/nvidia/<version>
#
# Uses -Rdd (no dependency cascade) instead of -Rns so unrelated
# packages (dkms, gcc, libdrm, libglvnd, ...) stay installed and
# the next driver branch can reuse them.
#
# Usage:
#   clean-nvidia-container.sh [driver]
#     driver: optional. "340xx", "390xx", "470xx", "580xx", etc.
#             If omitted, cleans all known drivers.
#
set -uo pipefail

DRIVER="${1:-}"

info() { echo "[clean] $*"; }

# Map driver → dkms state version
declare -A DKMS_VER=(
  [340xx]="340.108"
  [390xx]="390.157"
  [470xx]="470.256.02"
  [580xx]="580.65.06"
)

# --- Build pacman pattern ---------------------------------------------------
if [ -n "$DRIVER" ]; then
  pattern="^(nvidia-${DRIVER}.*|opencl-nvidia-${DRIVER}.*|mhwd-nvidia-${DRIVER}.*|lib32-(nvidia|opencl-nvidia)-${DRIVER}.*|linux.*-nvidia-${DRIVER}.*|mhwd-db|mhwd)\$"
else
  pattern="^(nvidia-(340xx|390xx|470xx|580xx).*|opencl-nvidia-(340xx|390xx|470xx|580xx).*|mhwd-nvidia-(340xx|390xx|470xx|580xx).*|lib32-(nvidia|opencl-nvidia)-(340xx|390xx|470xx|580xx).*|linux.*-nvidia-(340xx|390xx|470xx|580xx).*|mhwd-db|mhwd)\$"
fi

# --- 1. pacman packages -----------------------------------------------------
pkgs=$(pacman -Qq 2>/dev/null | grep -E "$pattern" | sort -u || true)
if [ -n "$pkgs" ]; then
  info "uninstalling (no dependency cascade):"
  echo "$pkgs" | sed 's/^/    /'
  # shellcheck disable=SC2086
  pacman -Rdd --noconfirm $pkgs 2>&1 | sed 's/^/    /' || true
else
  info "no matching packages installed"
fi

# --- 2. DKMS module state (per driver) --------------------------------------
if [ -n "$DRIVER" ] && [ -n "${DKMS_VER[$DRIVER]:-}" ]; then
  for d in /var/lib/dkms/nvidia /var/lib/dkms/nvidia-"${DKMS_VER[$DRIVER]}"; do
    [ -e "$d" ] || continue
    info "rm -rf $d"
    rm -rf -- "$d" 2>/dev/null || true
  done
else
  for d in /var/lib/dkms/nvidia*; do
    [ -e "$d" ] || continue
    info "rm -rf $d"
    rm -rf -- "$d" 2>/dev/null || true
  done
fi

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

# --- 4. Filesystem leftovers ------------------------------------------------
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