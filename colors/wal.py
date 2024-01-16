"""
Utilizes color schemes created by PyWal from wallpapers.
See this link for more information:
https://github.com/dylanaraps/pywal/wiki/Customization#qtile
"""
from libqtile.lazy import lazy
import os

colors = []

cache_path = f"/home/{os.getlogin()}/.cache/wal/colors"


def load_colors():
    with open(cache_path, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()


load_colors()
