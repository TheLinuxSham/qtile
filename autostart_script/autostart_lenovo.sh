#!/bin/bash

# Set config for screens
# xrandr --output DisplayPort-1 --mode 1920x1080 &

# Start picom for composing effects
picom &

# Apply wallpaper using nitrogen
nitrogen --restore &