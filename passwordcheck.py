import hashlib
import requests

class Passwd():
    
    # Get User input

    def getPass(self):
        password = input("Enter your Password: ")
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
        
        for line in hashesOrganized:
            if line[0:35].lower() == lastBits:
                isFound = True
                foundPassword = line
                break

        if isFound == True:
            splitNum = foundPassword.split(':')
            print("Password has been found {} times! -- {}".format(splitNum[1], foundPassword))
        elif isFound == False:
            print("Password was not found. Nice!")

def main():
    passwd = Passwd()
    passwd.checkPassword()

if __name__ == '__main__':
    main()
