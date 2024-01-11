from libqtile import hook
import os
import subprocess


@hook.subscribe.startup_once
def autostart_once(script_path: id):
    home = os.path.expanduser(script_path)
    subprocess.call([home])

# EOF
