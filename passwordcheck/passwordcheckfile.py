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
import os, sys, time, threading
import operator
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
        sys.stdout.write('\r'+'Checking password...'+char)
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

def checkPassword(lastBits, hashes, password, passwordDict):
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
            print(" {}: {}".format(password,commaNum))
            passwordDict[password] = splitNum[1]
        elif isFound == False:
            print(" {}: Not Found. Nice!".format(password))
    return passwordDict

def getFile():
    fileName = sys.argv[1]
    if os.path.exists(fileName):
        fileExist = True
    else: 
        fileExist = False
    return os.path.basename(fileName), fileExist

def parseFile(fileName, fileExist):
    if fileExist == True:
        lines = []
        with open(fileName) as File:
            for line in File:
                lines.append(line.rstrip())
        return lines
    else:
        print("File doesn't seem to exist...")

def getNumbers(lines):
    passwordDict = {}
    for line in lines:
        hashpass = hashPass(line)
        apirequest = ThreadWithReturnValue(target=apiRequest, args=(hashpass[0], hashpass[1], hashpass[2]))
        apirequest.start()
        while apirequest.is_alive():
            animated_loading()
        returnvalue = apirequest.join()
        passwordDict = checkPassword(returnvalue[0], returnvalue[1], returnvalue[2], passwordDict)
    return passwordDict

def sortDict(passwordDict):
    # change to ints instaed of string
    dict_with_ints = dict((k,int(v)) for k,v in passwordDict.items())
    sortedDict = {k: v for k, v in sorted(dict_with_ints.items(), key=lambda item: item[1], reverse=True)}
    return sortedDict

def printDict(sortedDict):
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("\n")
    print("Most Popular")
    for password, value in sortedDict.items():
        print("{}: {}".format(password, value))
    print("Least Popular")
    print("\n")
    print("------------------------------------------------")
    print("------------------------------------------------")
    first_item = list(sortedDict.items())[0]
    first_item_comma = '{:,}'.format(int(first_item[1]))
    last_item = list(sortedDict.items())[-1]
    last_item_comma = '{:,}'.format(int(last_item[1]))
    print("The password in your list that was used the MOST was: {}".format(first_item[0]))
    print("It was used {} times!".format(first_item_comma))    
    print("------------------------------------------------")
    print("The password in your list that was used the LEAST was: {}".format(last_item[0]))
    print("It was used {} times!".format(last_item_comma))    
    print("------------------------------------------------")


def main():

    try:
        getfile = getFile()
        filename = getfile[0]
        fileexist = getfile[1]
        lines = parseFile(filename, fileexist)
        passwordDict = getNumbers(lines)
        sortedDict = sortDict(passwordDict)
        printDict(sortedDict)

    except KeyboardInterrupt:
        print("\n")
        print("Thanks for using UnclassedPenguin Password Checker!")
        print("\n")


if __name__ == '__main__':
    main()
