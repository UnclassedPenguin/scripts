#!/usr/bin/env python3
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# Tyler(UnclassedPenguin) Password Check 2022
#
# Author: Tyler(UnclassedPenguin)
#    URL: https://unclassed.ca
# GitHub: https://github.com/UnclassedPenguin
#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import hashlib
import requests
import sys, time, threading
from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'Contacting HaveIBeenPwned API...'+char)
        time.sleep(.1)
        sys.stdout.flush() 
    
# Get User input

def getPass():
    while True:
        password = input("Enter your Password: ")
        if password.strip() != '':
            break
        else:
            print("Please input a password.")
    return password

# Takes the password and hashes it to SHA-1    

def hashPass(password):
    hashPass = hashlib.sha1(str(password).encode('utf-8'))
    hashedPass = hashPass.hexdigest() 
    firstFive = hashedPass[0:5]
    lastBits = hashedPass[5:]
    return firstFive, lastBits, password

# Strips the first five characters and passes it to the HaveIBeenPwned API

def apiRequest(firstFive, lastBits, password):
    url = "https://api.pwnedpasswords.com/range/{}".format(firstFive)
    response = requests.get(url)
    dataReturned = response.text
    return lastBits, dataReturned, password

# Compares the rest of the hash against the returned data to see if it was found

def checkPassword(lastBits, hashes, password):
    isFound = False 
    hashesOrganized = hashes.split()       
    
    for line in hashesOrganized:
        if line[0:35].lower() == lastBits:
            isFound = True
            foundPassword = line
            break

    if password == "exit":
        splitNum = foundPassword.split(':')
        commaNum = '{:,}'.format(int(splitNum[1]))
        print("\n")
        print("Password 'exit' has been found {} times!".format(commaNum))
        print("\n")
        print(foundPassword)
        print("\n")
        print("Thanks for using UnclassedPenguin Password Checker!")
        exit()

    else:
        if isFound == True:
            splitNum = foundPassword.split(':')
            commaNum = '{:,}'.format(int(splitNum[1]))
            print("\n")
            print("Password '{}' has been found {} times!".format(password,commaNum))
            print("\n")
            print(foundPassword)
        elif isFound == False:
            print("\n")
            print("Password was not found. Nice!")

def main():
    try:
        print("Ctrl-c to quit or enter 'exit'")
        print("----------------------------------------------")
        run = True
        while run == True: 
            password = getPass()
            hashpass = hashPass(password)
            apirequest = ThreadWithReturnValue(target=apiRequest, args=(hashpass[0], hashpass[1], hashpass[2]))
            apirequest.start()
            while apirequest.is_alive():
                animated_loading()
            returnvalue = apirequest.join()
            checkPassword(returnvalue[0], returnvalue[1], returnvalue[2])


            print("----------------------------------------------")

    except KeyboardInterrupt:
        print("\n")
        print("Thanks for using UnclassedPenguin Password Checker!")
        print("\n")


if __name__ == '__main__':
    main()
