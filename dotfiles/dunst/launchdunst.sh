#!/bin/sh

# =================================================
# Symlink config files so programs can be started
# without referencing the cache directly
# =================================================

# mkdir -p  "${HOME}/.config/dunst"
ln -sf    "${HOME}/.cache/wal/dunstrc"    "${HOME}/.config/dunst/dunstrc"

# ===================
# ====== dunst ======
# ===================

# Restart dunst with the new color scheme
pkill dunst
dunst &