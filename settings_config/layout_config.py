from libqtile import layout
from colors.wal import colors, load_colors


load_colors()


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
