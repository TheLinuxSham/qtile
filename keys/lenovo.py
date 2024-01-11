# Keybindings for my lenovo laptop
from libqtile.config import Key
from libqtile.lazy import lazy

lenovo_keys = [
    Key([],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="Brightness Up"),
    Key([],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="Brightness Down"),
    Key([], "print", lazy.spawn("flameshot gui"),
        desc="Starts Screenshot App Flameshot"),

    Key([], "XF86Tools", lazy.spawn("code"), desc="Launch Visual Studio Code"),
]

# EOF
