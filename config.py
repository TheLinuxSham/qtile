from libqtile.config import Key, Match, Group, Click, Drag, Screen
from libqtile.lazy import lazy
import os
from keys.qtile_keys import mod
from autostart_script.autostart_module import autostart_once
from libqtile import layout, bar, widget
from colors.wal import colors, load_colors
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from keys.desktop import desktop_keys
from keys.lenovo import lenovo_keys
from keys.qtile_keys import keys


def get_keys():
    return keys


def get_desktop():
    return keys + desktop_keys


def get_lenovo():
    return keys + lenovo_keys


# Sets up settings specific to host system name
if os.uname()[1].lower() == "desktop":
    keys = get_desktop()
    autostart_once("~/.config/qtile/autostart_script/autostart_desktop.sh")
if os.uname()[1].lower() == "thinkpad":
    keys = get_lenovo()
    autostart_once("~/.config/qtile/autostart_script/autostart_lenovo.sh")
else:
    get_keys()


load_colors()


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


widget_defaults = dict(
    font="GeistMono Nerd Font Bold",
    fontsize=17,
    padding=10,
    foreground="#222222"
)


extension_defaults = widget_defaults.copy()


# GROUPS
groups = [
    Group("1"), Group("2"), Group("3"), Group("4"),
    Group("5"), Group("6"), Group("7"), Group("8")
    ]

group_keys = ["1", "2", "3", "4", "5", "6", "7", "8"]


# LAYOUTS
layouts = [
    layout.Columns(
        margin=14,
        border_focus=colors[7],
        border_on_single=True,
        border_normal=colors[3],
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


for i in range(len(groups)):
    push_to_screen = [0, 0, 0, 0, 0, 0, 1, 1]
    group_key = group_keys[i]
    group_name = groups[i].name

    # just switch to group without dragging app
    keys.append(
        Key([mod],
            group_key,
            lazy.group[group_name].toscreen(push_to_screen[i]),
            lazy.to_screen(push_to_screen[i]))
            ),

    # drag app to different group without switching to it
    keys.append(Key([mod, "control"], group_key,
                lazy.window.togroup(group_name, switch_group=False))),

    # switch to different group with app
    keys.append(Key([mod, "shift"], group_key, lazy.window.togroup(group_name,
                switch_group=True)))


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


# WM for java apps
wmname = "LG3D"


arrow_right = {
    "decorations": [
        PowerLineDecoration(path="arrow_right"),
    ]
}

arrow_left = {
    "decorations": [
        PowerLineDecoration(path="arrow_left"),
    ]
}

rounded_right = {
    "decorations": [
        PowerLineDecoration(path="rounded_right"),
    ]
}

rounded_left = {
    "decorations": [
        PowerLineDecoration(path="rounded_left"),
    ]
}


load_colors()


def set_spacer():
    return widget.Spacer(length=8)


def set_battery(battery_id: int):
    return widget.Battery(
                    background=colors[5],
                    battery=battery_id,
                    format="{char} {percent:2.0%}",
                    full_char="󰂄",
                    discharge_char="󰂂",
                    charge_char="󱐋",
                    unknown_char="",
                    low_foreground="#ff0000",
                    low_percentage=0.25,
                    update_interval=120,
                    **arrow_right
                )


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=8,
                    background=colors[0]
                ),
                widget.GroupBox(
                    padding_x=0,
                    # margin_x=-10,
                    # sets color for group(text) with active apps
                    active=colors[8],
                    # sets color for inactive groups
                    inactive=colors[6],
                    highlight_method="line",
                    background=colors[0],
                    rounded=True,
                    # sets color for highlight(block) exclusively
                    highlight_color=colors[1],
                    # sets highlight (underline) color for selected group
                    this_current_screen_border=colors[8],
                    **arrow_left
                    ),
                widget.Prompt(),
                set_spacer(),
                widget.WindowName(
                    # fontsize=14,
                    foreground=colors[8]
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", colors[6]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                set_spacer(),
                widget.Spacer(
                    length=8,
                    **arrow_right
                ),
                widget.Volume(
                    emoji=True,
                    emoji_list=["󰸈", "󰖀", "", "󰕾"],
                    fmt="{}",
                    fontsize=25,
                    background=colors[3],
                ),
                widget.Spacer(length=-6),
                widget.Volume(
                    background=colors[3],
                    **arrow_right
                ),
                widget.CPU(
                    background=colors[4],
                    format="CPU {freq_current}GHz",
                ),
                widget.Spacer(length=-10),
                widget.ThermalSensor(
                    background=colors[4],
                    tag_sensor="CPU", # Tctl
                    **arrow_right
                ),
                # widget.ThermalSensor(
                #     fmt="GPU {}",
                #     background=colors[5],
                #     tag_sensor="edge",
                #     **arrow_right
                # ),
                # set_spacer(),
                set_battery(0),
                widget.Spacer(length=-15),
                set_battery(1),
                # set_spacer(),
                widget.Memory(
                    background=colors[6],
                    format="󰍛 {MemUsed:.00f}/{MemTotal:.00f}{mm}",
                    update_interval=5.0,
                    measure_mem="M",
                    **arrow_right
                ),
                widget.Clock(
                    background=colors[7],
                    format="󰃮 %a %d.%m.%Y  %I:%M %p",
                    # **rounded_left
                    ),
            ],
            28,  # bar thinkness
            background="#FF00FF05",
            margin=[10, 15, -5, 15],  # set up for floating bar
            # border_width=[4, 10, 4, 0],  # Draw top and bottom borders
            # border_color=colors[0]
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