from color_palette.catpuccino_latte import catpuccino_latte
from libqtile import bar, widget
from libqtile.config import Screen


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

# EOF
