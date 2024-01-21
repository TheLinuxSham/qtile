# Keybinds for any system I use
from libqtile.config import Key
from libqtile.lazy import lazy
import os

user = os.getlogin()

mod = "mod4"  # left win (super) key

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # UNIVERSAL SET OF FN-KEYS
    Key([],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume 0 +5%"),
        desc="Volume Up By 5%"),
    Key([],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume 0 -5%"),
        desc="Volume Down By 5%"),
    Key([],
        "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"),
        desc="Volume (Un)Mute"),
    Key([],
        "XF86AudioMicMute",
        lazy.spawn("amixer set Capture toggle"),
        desc="Microphone (Un)Mute"),

    # APP KEYS
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Thunar File Manager"),
    Key([mod], "h", lazy.spawn("roficlip"), desc="clipboard"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Firefox Web Browser"),
    Key([mod], "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "o",
        lazy.spawn("rofi -modi emoji -show emoji"),
        desc="Spawn a emoji-picker using rofi"),
    Key([mod], "backspace",
        lazy.spawn("clipton"),
        desc="Spawn a clipbaord manager using rofi"),
    Key([mod],
        "p",
        lazy.spawn(f"rofi -show power-menu -modi power-menu:/home/{user}/.config/rofi/rofi-power-menu"),
        desc="Rofi Script Powermenu"),
    Key([mod, "control"], "next", lazy.spawn("redshift -x"),
        desc="Redshift Disable Bluelight Filter"),
    Key([mod], "next", lazy.spawn("redshift -P -O 4500"),
        desc="Redshift Enable Bluelight Weak"),
    Key([mod], "prior", lazy.spawn("redshift -P -O 2750"),
        desc="Redshift Enable Bluelight Strong"),
]
