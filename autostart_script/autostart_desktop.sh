#!/bin/bash

# Starts Polkit Manager for Apps that need sudo privileges
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Set config for screens
# xrandr --output DisplayPort-1 --mode 1920x1080 --rate 60 --output DisplayPort-2 --mode 1920x1080 --rotate left &
xrandr --output HDMI-A-0 --auto --primary --output DisplayPort-0 --auto --rotate left --right-of HDMI-A-0 &

# Start picom for composing effects
picom &

# Apply wallpaper using nitrogen
nitrogen --restore &

# Start corectrl for adjusting CPU and GPU handling
corectrl --minimize-systray &

# Start Dunst Notification Daemon
${HOME}/.config/dunst/launchdunst.sh &

# Set Bluelight Protection
redshift -P -O 4500 &

# Start Clipton Clipboard Manager
systemctl --user restart clipton &

