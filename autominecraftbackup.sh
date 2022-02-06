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
screen -S minecraft -X stuff 'stop'$'\n'
sleep 30
warn $"Done..."

warn $"Checking if backup exists..."
cd ~/backups/minecraft
if [[ -f $date-minecraft.tar.gz ]]; then
  warn $"Minecraft backup for $date exists already..."
  deleteoldbackups
  startserver 0
else
  warn $"Backup not found, creating..."
  tar czf $date-minecraft.tar.gz -C ~/minecraft/worlds/ ~/minecraft/server.properties ~/minecraft/whitelist.json . || {
    warn $"Something went wrong with minecraft backup..."
    deleteoldbackups
    startserver 1 
  }
  warn $"Backup of minecraft succesful"
  deleteoldbackups
  startserver 0
fi

