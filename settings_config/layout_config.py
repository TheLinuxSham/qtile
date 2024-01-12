from libqtile import layout
from color_palette.catpuccino_latte import catpuccino_latte

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

# EOF
