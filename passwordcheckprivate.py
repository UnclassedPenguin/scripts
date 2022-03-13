#!/usr/bin/env python3
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# Tyler(UnclassedPenguin) Password Check Private 2022
#
# Author: Tyler(UnclassedPenguin)
#    URL: https://unclassed.ca
# GitHub: https://github.com/UnclassedPenguin
#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import hashlib
import requests
import stdiomask

    
# Get User input

def getPass():
    while True:
        password = stdiomask.getpass(prompt="Enter your password: ") 
        if password.strip() != '':
            break
        else:
            print("Please input a password.")
            print("\n")

    return password

# Takes the password and hashes it to SHA-1    

def hashPass():
    password = getPass()
    hashPass = hashlib.sha1(str(password).encode('utf-8'))
    hashedPass = hashPass.hexdigest() 
    firstFive = hashedPass[0:5]
    lastBits = hashedPass[5:]
    return firstFive, lastBits, password

# Strips the first five characters and passes it to the HaveIBeenPwned API

def apiRequest():
    splitHash = hashPass()
    firstFive = splitHash[0]
    lastBits = splitHash[1]
    password = splitHash[2]
    url = "https://api.pwnedpasswords.com/range/{}".format(firstFive)
    response = requests.get(url)
    dataReturned = response.text
    return lastBits, dataReturned, password

# Compares the rest of the hash against the returned data to see if it was found

def checkPassword():
    isFound = False 
    dataReturned = apiRequest()
    lastBits = dataReturned[0]
    hashes = dataReturned[1]
    password = dataReturned[2]
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
            print("Password has been found {} times!".format(commaNum))
            print("\n")
            print(foundPassword)
        elif isFound == False:
            print("\n")
            print("Password was not found. Nice!")



def main():
    try:
        print("Enter password 'exit' to quit")
        print("----------------------------------------------")
        run = True
        while run == True: 
            checkPassword()
            print("----------------------------------------------")

    except KeyboardInterrupt:
        print("\n")
        print("Thanks for using UnclassedPenguin Password Checker!")
        print("\n")


if __name__ == '__main__':
    main()
