## Password Check
Multiple versions of the same program for fun :)  

1. [Password Check](#PasswordCheck)
2. [Password Check Basic](#PasswordCheckBasic)
4. [Password Check File](#PasswordCheckFile)
3. [Password Check Private](#PasswordCheckPrivate)
5. [Password Check Rich](#PasswordCheckRich)

## PasswordCheck

This is my own version of a password checker which uses the HaveIBeenPwned API and checks if your password has been found in any online breaches that they have collected.  

It uses Threading to show a spinner while it is looking up the password.  

For more information [read this blog post](https://unclassed.ca/2021/simple-password-check/) or [watch this video](https://www.youtube.com/watch?v=hhUb5iknVJs).

Usage:

- Save file.
- Execute with python3

```
$ python3 passwordcheck.py
```

It will ask for your password, type it in and it will check. Will either output that it found it or it didn't.

**Be careful using any program like this that you find on the internet. I am not collecting anything, you can read the code, but people with bad intent could. Make sure you understand what this program is doing.**

## PasswordCheckBasic  

Pretty much the same as password check, but even more basic. Uses the least requirements. Nothing fancy at all.   

## PasswordCheckFile
Pretty much the same as password check, but you have to pass it a text file with a list of words in it, and it will go through the list line by line and check each password. At the end it will print them out from most to least used, and also give you the Most used password and the least used password from your list. It checks the list based on new lines, so create a file called pass.txt and fill it like:  
  
word1  
word2  
word3  
password  
thing  
another  
one    

then execute it like:  

```
$ python3 passwordcheckfile.py pass.txt
```

## PasswordCheckPrivate

Pretty much the same as password check, but it uses stdiomask module (a requirement) to mask the input of your password to asterisks. Slightly more private maybe, but the same functionality. Oddly enough, you can't exit the program with ctrl-c when it is prompting for a password so I made it quit on entering the password 'exit'.  

## PasswordCheckRich

This is the same as Password check but just made to look a little bit different using the [rich](https://github.com/willmcgugan/rich) python module. I was just messing around with it. 


