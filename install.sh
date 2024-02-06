#! usr/bin/bash

# installs packages
pacman -Sy qtile python-psutil lm-sensors rofi python-pywal dunst picom redshift
yay -S qtile-extras otf-geist-mono-nerd

# gives privileges for automatic dunst restart after wal set colors
chmod +x ./dotfiles/dunst/launchdunst.sh

#deletes stuff
rm -rfv ./work_in_progress

# moves dotfiles
mkdir -p {$HOME}/.config/qtile
mkdir -p {$HOME}/Pictures/Wallpaper
mv -fv ./autostart_script/ ./colors/ ./keys/ ./config.py {$HOME}/.config/qtile/
mv -fv ./dotfiles/* {$HOME}/.config
mv -v ./wallpaper/endeavour-astronaut.jpg {$HOME]/Pictures/Wallpeper}

# sets wallpaper and color scheme
feh --bg-scale {$HOME}/Pictures/Wallpaper/endeavour-astronaut.jpg
wal -i {$HOME}/Pictures/Wallpaper/endeavour-astronaut.jpg -n -o {$HOME}/.config/dunst/launchdunst.sh

# restart qtile
qtile cmd-obj -o cmd -f reload_config