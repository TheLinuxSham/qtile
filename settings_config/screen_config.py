from colors.wal import colors, load_colors
from libqtile import bar, widget
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration


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
                    background=colors[0],
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
                # widget.Spacer(arrow_right),
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
                    fontsize=14,
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
                    background=colors[4],
                ),
                widget.Spacer(length=-6),
                widget.Volume(
                    background=colors[4],
                    **arrow_right
                ),
                # set_spacer(),
                # set_battery(0),
                # widget.Spacer(length=-10),
                # set_battery(1),
                # set_spacer(),
                widget.CPU(
                    background=colors[5],
                    format="CPU {freq_current}GHz",
                ),
                widget.Spacer(length=-10),
                widget.ThermalSensor(
                    background=colors[5],
                    tag_sensor="Tctl",
                    **arrow_right
                ),
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
