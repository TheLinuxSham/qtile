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
# Future Improvements
I use Qtile on two machines. One of them is a Laptop and the other is my Desktop. They both use different sets of FN-Keys. My goal is configure Qtile in a way to recognize the host and automatically set the right keybindings for the FN-Keys.

My Desktop also uses two screens. I would love to start specific apps to defined groups and screens.
