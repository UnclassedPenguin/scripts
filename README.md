# Scripts
A random collection of useful scripts

1. [easyssh](#easyssh)
2. [UbuntuSplashColor.py](#UbuntuSplashColor)
3. [Auto Minecraft Backup](#AutoMinecraftBackup)
4. [Timer](#Timer)
5. [Binary Clock](#BinaryClock)
## easyssh

- Clone the repository, or download just easyssh  

- Place it in a folder that is in your path  

- Open the file and edit username, ip, port, and the name of your server.

```
user="yourusername"
server=192.168.1.1
servername="yourServerName"
port=12345
```
- Give the script executable permission  
`$ chmod +x easyssh`

- Execute!

## UbuntuSplashColor

**This was written for ubuntu 18.04. Doesn't seem the files exist in 20.04. So basically useless now, but I'll leave it for now.**
**Use at your own risk. This is an old program, not maintained, might be smart to check that the files it is going to edit are actually on your system**

This is a program that changes the color of the ubuntu splash screens as you boot up your computer running ubuntu.
I have an article [here](https://unclassed.ca/2019/change-ubuntu-color-manually/) that explains how to manually do these changes. This is just an automation of that process.


- Save file.
- Execute file with sudo privilege using python3.

```
$ sudo python3 UbuntuSplashColor.py
```

Script will edit:
  1. '/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.grub'
  2. '/usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.script'
  3. '/usr/share/gnome-shell/theme/ubuntu.css'

Backups of all files will be saved in same directory with .old extension.
If you have any issues just delete the new files and rename the files with .old to original name.

## AutoMinecraftBackup  

This is a script I use on my minecraft server to automatically back up. have it run daily with cron. 

## Timer

I wanted a simple timer, so I wrote this one in python. All it does is count up in seconds. I've added some arguments to it...Might add some more.

## BinaryClock

I wanted to try writing a binary clock in python, this is what I came up with. I'm sure there is a more efficient way to do it.... Let me know!
