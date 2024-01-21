# About

These are the Dotfiles for my personal Qtile Setup. [Qtile](https://qtile.org/) is a tiling window manager for Linux that's written and configured solely in Python.  

It's my first time using a tiling window manager, but I have some experience with Python. 
So I wanted to give it a shot and further hone my programming skills to see what I can come up with.

Since I'm new to this, I tried to hack on various dotfiles before, but none of them would work for me out of the box. 
The configs had either weird dependencies as packages, assets, no/bad documentation on what to do, or outdated code. Eventually I quit trying to fix them.

So I came up with another plan: Configure Qtile in a way that will be somewhat pleasing with as little dependencies as possible.
For that I hacked on the default Qtile config and was very cautios about adding extra stuff.

With that out of the way... Feel free to use it or let it inspire you!

I use Arch, btw.

# Setup

Download this repo and extract it. You might want to check the autostart_desktop.sh as it contains commands to set up my screen resolutions/roations, wallpaper and composing effects at log in. 
You might alter/delete the code to your needs. My dotfiles run perfectly with an empty script file.


For an Arch Distribution install

```sudo pacman -S qtile python-psutil lm-sensors rofi python-pywal dunst picom redshift```

and also

```yay -S otf-geist-mono-nerd```


in your terminal of choice. 


Pacman should also install every neccessary dependency automatically.
After that, copy the content of this folder to:

`~/.config/qtile`


Or open a terminal in the downloaded qtile folder and run:
```
mkdir -p ~/.config/qtile
mv * ~/.config/qtile
```

Now log out and start a new session in Qtile or simply press `Mod (usally left Win key/Super key) + Ctrl + r` to restart Qtile with the new config.

See Dependencies & Packages Overview for more information on how all is used or what the intention was.
# Features
I use the same dotfiles for two systems. The code in **config.py** will check for the host systems name and set up Qtile accordingly.


There's two autostart scripts that start host specific apps/settings via the **autostart_module.py** in **autostart_scripts** folder.

Same goes for some key bindings. My systems use different keyboards and I seperated the keys in host individual python files over at **keys** folder.

# Dependencies & Packages Overview
## Qtile
Qtile, of course, is used to run Qtile... you now?

python-psutil and lm-sensors are used to grab information off of hardware 
(see documentation [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#thermalsensor), [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#cpu), and [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#memory))

## Nitrogen
[Nitrogen](https://wiki.archlinux.org/title/Nitrogen) sets my wallpaper. I then use it on each login session to restore my settings. See ./autostart_script for scripts.

Alternative: [feh](https://wiki.archlinux.org/title/Feh)

## PyWal
I use [PyWal](https://github.com/dylanaraps/pywal) to generate color schemes from my set wallpaper automatically. This color scheme is safed in a cache file and can be used by Qtile, Visual Studio Code, Alacritty, Neo Vim and so on. See ./colors/wal.py. 

You COULD also use PyWal to set your wallpaper, instead of nitrogen. But only if you use one screen.

For more customization see [here](https://github.com/dylanaraps/pywal/wiki/Customization#rofi).

## Rofi (optional)
I use [Rofi](https://wiki.archlinux.org/title/Rofi) to search and launch my Apps. 

I also integrated a [powermenu script](https://github.com/jluttine/rofi-power-menu) for quick access through Rofi. The script is executed via Qtile-Key-Command with a specified path to the dotfiles of rofi. It isn't added to $PATH itself. See ./keys/qtile_keys.py.

Alternative: [dmenu](https://wiki.archlinux.org/title/Dmenu)

## Redshift (optional)
[Redshift](https://wiki.archlinux.org/title/Redshift) sets up a bluelight filter for me via Qtile-Key-Command. Its has a combo for strong, weak and disabled mode. See ./keys/qtile_keys.py.

## Dunst (optional)
Qtile does not need [Dunst](https://wiki.archlinux.org/title/Dunst) to be able to run. But you won't see any notifications on your system without Dunst. 

Color scheme is also used from PyWal. I modified the default dunstrc to my liking and added the colors I want PyWal to set. I copied the dunstrc to ~/.config/wal/templates. Also the documentation for [templates](https://github.com/dylanaraps/pywal/wiki/User-Template-Files) may be of interest. Then I created a script to restart Dunst every time I set a new scheme with PyWal and created a symlink between the template dunstrc and the dunstrc in my .config.

## Picom (optional)
I can set up shadows and round edges for windows with [Picom](https://wiki.archlinux.org/title/Picom). Qtile does not need this package to be able to run and there are a lot of alternatives. Picom is for X11.


# Future Improvements

1. Add Key Chords to launch most used apps independent of host system.

2. Let Qtile spawn specific apps to set groups.

3. Make the Battery Icons only show up on my Laptop.
