# Keybindings for my desktop pc
from libqtile.config import Key
from libqtile.lazy import lazy

desktop_keys = [
    Key([],
        "Menu",
        lazy.spawn("flameshot gui"),
        desc="Starts Screenshot App Flameshot"),
]

# EOF
