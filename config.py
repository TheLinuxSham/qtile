# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from color_palette import catpuccino_latte
from autostart_script.autostart_module import autostart_once
from keys.lenovo import lenovo_keys
from keys.desktop import desktop_keys
import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
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
    Key([mod],
        "p",
        lazy.spawn("sh -c ~/.config/rofi/scripts/power"),
        desc="Rofi Script Powermenu"),
    Key([],
        "XF86Favorites",
        lazy.spawn("sh -c ~/.config/rofi/scripts/themes"),
        desc="Theme_switcher"),

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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Thunar File Manager"),
    Key([mod], "h", lazy.spawn("roficlip"), desc="clipboard"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Firefox Web Browser"),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),
]

groups = [
    Group("1 "), Group("2 "), Group("3 󰅨"), Group("4 "),
    Group("5 󱥁"), Group("6 󰙯"), Group("7 󱜌"), Group("8 󱣴")
    ]
group_keys = ["1", "2", "3", "4", "5", "6", "7", "8"]

for i in range(len(groups)):
    group_key = group_keys[i]
    group_name = groups[i].name
    keys.append(Key([mod], group_key, lazy.group[group_name].toscreen()))
    keys.append(Key([mod, "control"], group_key,
                lazy.window.togroup(group_name, switch_group=False)))
    keys.append(Key([mod, "shift"], group_key, lazy.window.togroup(group_name,
                switch_group=True)))

layouts = [
    layout.Columns(
        margin=14,
        border_focus=catpuccino_latte[19],
        border_on_single=True,
        border_normal=catpuccino_latte[15],
        border_width=3
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=15,
    padding=10,
    foreground=catpuccino_latte[14]
)
extension_defaults = widget_defaults.copy()

if os.uname()[1].lower() == "desktop":
    keys = keys + desktop_keys
    autostart_once("~/.config/qtile/autostart_script/autostart_desktop.sh")
if os.uname()[1].lower() == "thinkpad":
    keys = keys + lenovo_keys
    autostart_once("~/.config/qtile/autostart_script/autostart_lenovo.sh")
else:
    pass


def set_spacer():
    return widget.Spacer(length=8)


def set_battery(battery_id: int):
    return widget.Battery(
                    background=catpuccino_latte[10],
                    battery=battery_id,
                    format="{char} {percent:2.0%}",
                    full_char="󰂄",
                    discharge_char="󰂂",
                    charge_char="󱐋",
                    unknown_char="",
                    low_foreground="#ff0000",
                    low_percentage=0.25,
                    update_interval=120
                )


screens = [
    Screen(
        top=bar.Bar(
            [
                set_spacer(),
                widget.GroupBox(
                    padding_x=0,
                    # margin_x=-10,
                    # sets color for groups with active apps
                    active=catpuccino_latte[25],
                    # sets color for inactive groups
                    inactive=catpuccino_latte[14],
                    # sets font color for selected group
                    # block_highlight_text_color=catpuccino_latte[25],
                    highlight_method="line",
                    background=catpuccino_latte[6],
                    rounded=True,
                    # set color for line highlight exclusively
                    highlight_color=catpuccino_latte[6],
                    # sets highlight color for selected group
                    this_current_screen_border=catpuccino_latte[12],
                    ),
                set_spacer(),
                widget.CurrentLayout(
                    fmt=" {}",
                    background=catpuccino_latte[8]
                ),
                widget.Prompt(),
                set_spacer(),
                widget.WindowName(
                    fontsize=14,
                    foreground=catpuccino_latte[25]
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", catpuccino_latte[20]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                set_spacer(),
                widget.Volume(
                    emoji=True,
                    emoji_list=["󰸈", "󰖀", "", "󰕾"],
                    fmt="{}",
                    fontsize=25,
                    background=catpuccino_latte[12],
                    # padding=3
                ),
                widget.Spacer(length=-5),
                widget.Volume(
                    background=catpuccino_latte[12],
                ),
                set_spacer(),
                # set_battery(0),
                # widget.Spacer(length=-10),
                # set_battery(1),
                # set_spacer(),
                widget.CPU(
                    background=catpuccino_latte[3],
                    format="CPU {freq_current}GHz"
                ),
                widget.Spacer(length=-10),
                widget.ThermalSensor(
                    background=catpuccino_latte[3],
                    tag_sensor="Tctl"
                ),
                set_spacer(),
                widget.Memory(
                    background=catpuccino_latte[9],
                    format="󰍛 {MemUsed:.00f}/{MemTotal:.00f}{mm}",
                    update_interval=5.0,
                    measure_mem="M"
                ),
                set_spacer(),
                widget.Clock(
                    background=catpuccino_latte[5],
                    format="󰃮 %a %d.%m.%Y  %I:%M %p",
                    ),
            ],
            28,  # bar thinkness
            background=catpuccino_latte[14],
            # margin = [4,10,4,10], # set up for floating bar
            border_width=[4, 10, 4, 10],  # Draw top and bottom borders
            border_color=catpuccino_latte[14]
            # ["ff00ff", "ff00ff", "ff00ff", "ff00ff"] for different
            # colors each side
        ),
        # You can uncomment this variable if you see
        # that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve
        # performance, however your system might still be struggling

        # This variable is set to None (no cap) by default, but you can set it
        # to 60 to indicate that you limit it to 60 events per second

        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()
            ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of
        # an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# EOF
