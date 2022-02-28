# Scripts
A random collection of useful scripts

1. [easyssh](#easyssh)
2. [UbuntuSplashColor.py](#UbuntuSplashColor)
3. [Password Check](#PasswordCheck)
4. [Rich Password Check](#RichPasswordCheck)
5. [Auto Minecraft Backup](#AutoMinecraftBackup)
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

## PasswordCheck

This is my own version of a password checker which uses the HaveIBeenPwned API and checks if your password has been found in any online breaches that they have collected. For more information [read this blog post](https://unclassed.ca/2021/simple-password-check/) or [watch this video](https://www.youtube.com/watch?v=hhUb5iknVJs).

Usage:

- Save file.
- Execute with python3

```
$ python3 passwordcheck.py
```

It will ask for your password, type it in and it will check. Will either output that it found it or it didn't.

**Be careful using any program like this that you find on the internet. I am not collecting anything, you can read the code, but people with bad intent could. Make sure you understand what this program is doing.**

## RichPasswordCheck

This is the same as Password check but just made to look a little bit different using the [rich](https://github.com/willmcgugan/rich) python module. I was just messing around with it. 

## AutoMinecraftBackup  

This is a script I use on my minecraft server to automatically back up. have it run daily with cron. 
