#!/bin/bash

# Set config for screens
xrandr --output DisplayPort-1 --mode 1920x1080 --rate 60 --output DisplayPort-2 --mode 1920x1080 --rotate left &

# Start picom for composing effects
picom &

# Apply wallpaper using nitrogen
nitrogen --restore &

# Start corectrl for adjusting CPU and GPU handling
corectrl --minimize-systray &