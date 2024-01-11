from libqtile import hook
import os
import subprocess


@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser(
        '~/.config/qtile/autostart_script/autostart_desktop.sh')
    subprocess.call([home])

# EOF
