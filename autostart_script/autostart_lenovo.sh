#!/bin/bash

# Starts Polkit Manager for Apps that need sudo privileges
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Start picom for composing effects
picom &

# Apply wallpaper using nitrogen
nitrogen --restore &

# Start Dunst Notification Daemon
$HOME/.config/dunst/launchdunst.sh &

# Set Bluelight Protection
redshift -P -O 4500 &

# Start Clipton Clipboard Manager
systemctl --user restart clipton &
