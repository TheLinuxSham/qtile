# grabbed from https://github.com/qtile/qtile-examples/blob/master/oboingo/keys.py

# Depending on how many screens I have, state which group goes on which screen
# Just a static list, nothing fancy
# key_for_group is the key/group
# screen_number is which screen it should go on
if num_screens[hostname] == 4:
    key_for_group = ["1", "2", "3", "4", "5", "6", "7", "8"]
    screen_number = [0, 0, 0, 0, 0, 0, 1, 1]
else:
    key_for_group = ["1", "2", "3", "4", "5", "6", "7", "8"]
    screen_number = [0, 0, 0, 0, 0, 0 ,0 ,0]
# Loop over the groups, and setup keys for each group to move groups to screens
# and move focus to screens/groups
for index, i in enumerate(groups):
    home.addchildren(
        # mod1 + number of group (starting with 1) = switch to group
        KeyNode([mod4], key_for_group[index], [], lazy.group[i.name].toscreen(screen_number[index]), lazy.to_screen(screen_number[index])),

        # mod1 + shift + number of group (starting with 1) = switch to & move focused window to group
        KeyNode([mod4, "shift"], key_for_group[index], [], lazy.window.togroup(i.name)),
    )
