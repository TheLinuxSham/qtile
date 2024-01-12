from settings_config.group_config import groups, group_keys
from settings_config.layout_config import layouts
from settings_config.mouse_config import mouse
from settings_config.screen_config import screens
from keys.desktop import desktop_keys
from keys.lenovo import lenovo_keys
from keys.qtile_keys import keys


def get_groups():
    return groups


def get_group_keys():
    return group_keys


def get_layout():
    return layouts


def get_mouse():
    return mouse


def get_bar():
    return screens


def get_keys():
    return keys


def get_desktop():
    return keys + desktop_keys


def get_lenovo():
    return keys + lenovo_keys
