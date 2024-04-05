#!/bin/bash

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# Tyler(UnclassedPenguin) Auto Minecraft Backup 2022
#
# Author: Tyler(UnclassedPenguin)
#    URL: https://unclassed.ca
# GitHub: https://github.com/UnclassedPenguin
#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


SCRIPTNAME="${0##*/}"

warn() {
    printf >&2 "$SCRIPTNAME: $*\n"
}

date=$(date '+%Y-%m-%d')

deleteoldbackups() {
  warn $"Checking for backups older than 7 days to delete..."
  cd ~/backups/minecraft/
  find . -type f -mtime +7 -delete
  warn $"Done..."
}

# Requires exit code 0 or 1 as parameter
startserver() {
  cd ~/minecraft/
  screen -S minecraft -X stuff './start.sh'$'\n'
  warn $"Starting server and exiting..."
  exit $1
}

warn $"Stopping minecraft server..."
screen -S minecraft -X stuff $' stop\n'
sleep 30

# I tend to forget to exit copy mode after looking at the server.
# So this will catch if you didn't exit copy mode in screen.
if [[ $(pgrep bedrock_server) ]]; then
  warn $"Server didn't shutdown..."
  warn $"Attempting to stop minecraft server again..."
  screen -S minecraft -X stuff $' stop\n'
  sleep 30
fi

# If for some reason both attempts to stop the server fail, it will
# exit without backing up. I don't know how reliable backing up a 
# running server is.
if [[ $(pgrep bedrock_server) ]]; then
  warn $"Server still running..."
  warn $"No Backup created, check manually..."
  warn $"Exiting..."
  exit 1
else
  warn $"Server successfully shutdown..."

  warn $"Checking if backup exists..."

  cd ~/backups/minecraft

  if [[ -f $date-minecraft.tar.gz ]]; then
    warn $"Minecraft backup for $date exists already..."
    deleteoldbackups
    startserver 0
  else
    warn $"Backup not found, creating..."
    tar czf $date-minecraft.tar.gz -C ~/minecraft/worlds/ ~/minecraft/server.properties ~/minecraft/allowlist.json . || {
      warn $"Something went wrong with minecraft backup..."
      deleteoldbackups
      startserver 1 
    }
    warn $"Backup of minecraft successful"
    deleteoldbackups
    startserver 0
  fi
fi
