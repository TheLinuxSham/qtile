from libqtile.config import Key, Match
from libqtile.lazy import lazy
import os
from keys.qtile_keys import mod
from autostart_script.autostart_module import autostart_once
from settings_thunnel import get_groups, get_group_keys, get_layout, get_mouse, get_bar, get_keys, get_desktop, get_lenovo
from libqtile import layout

widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=15,
    padding=10,
    foreground="#4c4f69"
)

extension_defaults = widget_defaults.copy()

screens = get_bar()
layouts = get_layout()
mouse = get_mouse()
groups = get_groups()
group_keys = get_group_keys()


# Sets up settings specific to host system name
if os.uname()[1].lower() == "desktop":
    keys = get_desktop()
    autostart_once("~/.config/qtile/autostart_script/autostart_desktop.sh")
if os.uname()[1].lower() == "thinkpad":
    keys = get_lenovo()
    autostart_once("~/.config/qtile/autostart_script/autostart_lenovo.sh")
else:
    get_keys()


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


# EOF
