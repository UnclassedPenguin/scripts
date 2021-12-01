import hashlib
import requests
from time import sleep
from rich.status import Status
from rich.console import Console

console = Console()

class Passwd():
    
    # Get User input

    def getPass(self):
        console.print("[bold blue]Enter your Password: ")
        password = console.input("[bold blue]> ")
        return password

    # Takes the password and hashes it to SHA-1    

    def hashPass(self):
        password = self.getPass()
        hashPass = hashlib.sha1(str(password).encode('utf-8'))
        hashedPass = hashPass.hexdigest() 
        firstFive = hashedPass[0:5]
        lastBits = hashedPass[5:]
        return firstFive, lastBits

    # Strips the first five characters and passes it to the HaveIBeenPwned API

    def apiRequest(self):
        splitHash = self.hashPass()
        firstFive = splitHash[0]
        lastBits = splitHash[1]
        url = "https://api.pwnedpasswords.com/range/{}".format(firstFive)
        response = requests.get(url)
        dataReturned = response.text
        return lastBits, dataReturned

    # Compares the rest of the hash against the returned data to see if it was found

    def checkPassword(self):
        isFound = False 
        dataReturned = self.apiRequest()
        lastBits = dataReturned[0]
        hashes = dataReturned[1]
        hashesOrganized = hashes.split()       
        
        with Status("[blue]Checking Passwords...") as status:
            status.update(spinner="aesthetic")
            sleep(3)
            for line in hashesOrganized:
                if line[0:35].lower() == lastBits:
                    isFound = True
                    foundPassword = line
                    break

        if isFound == True:
            splitNum = foundPassword.split(':')
            commaNum = '{:,}'.format(int(splitNum[1]))    
            print("\n")
            console.print("[bold blue]Password has been found [bold red]{}[/] times! [bold white]-- {}".format(commaNum, foundPassword))
        elif isFound == False:
            print("\n")
            console.print("[bold blue]Password was not found. Nice!")

def main():
    try:
        run = True
        while run == True: 
            passwd = Passwd()
            passwd.checkPassword()
            print("\n")
            runInput = console.input("[bold blue]Would you like to check another password? ([bold red]Y[/] or [bold red]n[/]) ")
            print("\n")
            
            if runInput.lower() == 'y' or runInput.lower() == 'yes':
                run = True
            elif runInput.lower() == 'n' or runInput.lower() == 'no':
                run = False
                console.print("[bold blue]Thanks for using [bold purple]UnclassedPenguin[/] Password Checker!")
                print("\n")
    except KeyboardInterrupt:
        print("\n")
        console.print("[bold blue]Thanks for using [bold purple]UnclassedPenguin[/] Password Checker!")
        print("\n")
    except: 
        print("\n")
        console.print("[bold blue]Something went [bold red]wrong[/]...")
        print("\n")
        
if __name__ == '__main__':
    main()
