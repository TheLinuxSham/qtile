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
```sudo pacman -S qtile python-psutil lm-sensors```
in your terminal of choice. 

python-psutil and lm-sensors are used to grab information off of hardware 
(see documentation [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#thermalsensor), [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#cpu), and [here](https://docs.qtile.org/en/stable/manual/ref/widgets.html#memory))

Pacman should also install every neccessary dependency automatically.
After that, copy the content of this folder to:

`~/.config/qtile`


Or open a terminal in the downloaded qtile folder and run:
```
mkdir -p ~/.config/qtile
mv * ~/.config/qtile
```

Now log out and start a new session in Qtile or simply press `Mod (usally left Win key) + Ctrl + r` to restart Qtile with the new config.

Consider installing [Dunst](https://wiki.archlinux.org/title/Dunst), a lightweight replacement for the notification-daemons and [Picom](https://wiki.archlinux.org/title/Picom), a standalone window compositor on X11 for a little bit of eye candy.
# Features
I use the same dotfiles for two systems. The code in **config.py** will check for the host systems name and set up Qtile accordingly.


There's two autostart scripts that start host specific apps/settings via the **autostart_module.py** in **autostart_scripts** folder.

Same goes for some key bindings. My systems use different keyboards and I seperated the keys in host individual python files over at **keys** folder.
# Future Improvements
1. I plan on completely extract key related stuff to a seperate file from the config.py and add key chords to them. So I can use the same key combos on any system. Also it would make the config.py more compact.

2. My Desktop uses two screens. I will add group specific app spawning and specific screen spawning in the future.

3. Make the Battery Icons only show up on my Laptop.
