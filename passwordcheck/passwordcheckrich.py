import hashlib
import requests
from rich.status import Status
from rich.console import Console


console = Console()
    
# Get User input

def getPass():
    console.print("[bold blue]Enter your Password: ")
    password = console.input("[bold blue]> ")
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
    with Status("[blue]Checking Passwords...") as status:
        status.update(spinner="aesthetic")
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
        console.print("[bold blue]Password 'exit' has been found [bold red]{}[/] times!".format(commaNum))
        print("\n")
        console.print("[bold white]{}".format(foundPassword))
        print("\n")
        console.print("[bold blue]Thanks for using [bold purple]UnclassedPenguin[/] Password Checker!")
        exit()
    else: 
        if isFound == True:
            splitNum = foundPassword.split(':')
            commaNum = '{:,}'.format(int(splitNum[1]))    
            print("\n")
            console.print("[bold blue]Password '[red bold]{}[/]' has been found [bold red]{}[/] times!".format(password, commaNum))
            print("\n")
            console.print("[bold white]{}".format(foundPassword))
        elif isFound == False:
            print("\n")
            console.print("[bold blue]Password was not found. Nice!")

def main():
    try:
        console.print("[bold blue]Ctrl-c to [bold red]quit[/] or enter 'exit'[/]")
        console.print("[bold white]----------------------------------------------[/]")
        run = True
        while run == True: 
            checkPassword()
            console.print("[bold white]----------------------------------------------[/]")
    except KeyboardInterrupt:
        print("\n")
        console.print("[bold blue]Thanks for using [bold purple]UnclassedPenguin[/] Password Checker!")
        print("\n")
        
if __name__ == '__main__':
    main()
