#!/usr/bin/env bash
#
# build-official.sh
#
# Called from .github/workflows/build-official.yml as the `builder` user.
#
# $1 = workspace path (where clean-nvidia-container.sh lives)
# $2 = path to file with available kernel prefixes (one per line)
#
# Build order:
#   Simple branches  (390xx, 470xx): makepkg -si works (single DKMS).
#   Complex branches (580xx, current): pkgbase contains BOTH a closed and
#     an open DKMS subpackage, both providing 'NVIDIA-MODULE' and thus
#     conflicting. Strategy: build once with -s, install closed only,
#     build closed modules, cleanup, reinstall userspace (needed by the
#     open DKMS's dependency on nvidia-utils=${pkgver}), install open
#     DKMS only, build open modules, cleanup.
#
set -uo pipefail

WS="${1:?missing workspace arg}"
KERNELS_FILE="${2:?missing kernels file}"

info() { echo "[build-official] $*"; }

# ---------------------------------------------------------------------------
# Helper: build one nvidia kernel module for every available kernel
# ---------------------------------------------------------------------------
build_kernel_modules() {
    local nv_folder="$1"
    while read -r prefix; do
        [ -z "$prefix" ] && continue
        local kdir="/build/official/extra/${prefix}-extramodules/${nv_folder}"
        [ -d "$kdir" ] || continue
        echo "==> ${prefix}-extramodules / ${nv_folder}"
        cd "$kdir"
        makepkg -s --noconfirm --skippgpcheck \
            || echo "    [warn] build failed: $kdir"
    done < "$KERNELS_FILE"
}

# ---------------------------------------------------------------------------
# Pre-install runtime deps that the built packages expect.
# makepkg -si handles this automatically; our manual pacman -U does not.
# inetutils provides the `hostname` binary used by some open kernel
# module Makefiles (utils.mk) during the build.
# ---------------------------------------------------------------------------
info "pre-installing common nvidia runtime deps"
sudo pacman -S --noconfirm --needed \
    libglvnd egl-wayland egl-gbm egl-x11 \
    desktop-file-utils \
    inetutils \
    || info "some deps not available, continuing"

# ---------------------------------------------------------------------------
# Simple branches (single DKMS): 390xx, 470xx
# ---------------------------------------------------------------------------
for utils_name in nvidia-390xx-utils nvidia-470xx-utils; do
    drv="${utils_name#nvidia-}"
    drv="${drv%-utils}"
    utils_dir="/build/official/extra/${utils_name}"
    [ -d "$utils_dir" ] || { info "no ${utils_name} — skipping"; continue; }

    echo "::group::Building ${utils_name}"
    cd "$utils_dir"
    makepkg -si --noconfirm --skippgpcheck \
        || echo "    [warn] utils build/install failed: ${utils_name}"

    build_kernel_modules "nvidia-${drv}"

    echo "==> cleanup after ${drv}"
    sudo bash "${WS}/clean-nvidia-container.sh" "$drv" || true
    echo "::endgroup::"
done

# ---------------------------------------------------------------------------
# Complex branches (closed + open DKMS in one pkgbase): 580xx, current
# ---------------------------------------------------------------------------
build_complex() {
    local utils_name="$1"       # nvidia-580xx-utils
    local closed_folder="$2"    # nvidia-580xx
    local open_folder="$3"      # nvidia-580xx-open
    local clean_driver="$4"     # 580xx  (or "current")
    local base="${utils_name%-utils}"

    local utils_dir="/build/official/extra/${utils_name}"
    [ -d "$utils_dir" ] || { info "no ${utils_name} — skipping"; return 0; }

    # ---- Closed half ------------------------------------------------------
    echo "::group::Building ${utils_name} (closed)"
    cd "$utils_dir"

    makepkg -s --noconfirm --skippgpcheck \
        || echo "    [warn] utils build failed: ${utils_name}"

    # Install closed packages only. Explicit names so the *-open-* ones
    # stay uninstalled.
    sudo pacman -U --noconfirm \
        "${base}-utils-"*.pkg.tar.zst \
        "opencl-${base}-"*.pkg.tar.zst \
        "${base}-dkms-"*.pkg.tar.zst \
        "mhwd-${base}-"*.pkg.tar.zst \
        || echo "    [warn] closed install failed: ${utils_name}"

    build_kernel_modules "$closed_folder"

    echo "==> cleanup after ${clean_driver} (closed)"
    sudo bash "${WS}/clean-nvidia-container.sh" "$clean_driver" || true
    echo "::endgroup::"

    # ---- Open half --------------------------------------------------------
    echo "::group::Building ${utils_name} (open)"
    cd "$utils_dir"

    # The open DKMS depends on the userspace package from the same pkgbase
    # (`nvidia-utils=${pkgver}`). The cleanup after the closed phase
    # removed everything, so reinstall the userspace package from the
    # .pkg.tar.zst files that are still on disk.
    sudo pacman -U --noconfirm \
        "${base}-utils-"*.pkg.tar.zst \
        || echo "    [warn] userspace reinstall failed: ${utils_name}"

    # The open .pkg.tar.zst is still on disk from the earlier build.
    sudo pacman -U --noconfirm \
        "${base}-open-dkms-"*.pkg.tar.zst \
        || echo "    [warn] open install failed: ${utils_name}"

    build_kernel_modules "$open_folder"

    echo "==> cleanup after ${clean_driver} (open)"
    sudo bash "${WS}/clean-nvidia-container.sh" "$clean_driver" || true
    echo "::endgroup::"
}

build_complex nvidia-580xx-utils nvidia-580xx nvidia-580xx-open 580xx
build_complex nvidia-utils      nvidia      nvidia-open      current

info "done"