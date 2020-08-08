import pyperclip
import json
import time
from pathlib import Path
file = "passwords.txt"
pathFile = Path("passwords.txt")
if pathFile.is_file():
    open(file, "r+")
    passwordsFile = json.load(open(file))
else:
    open(file, "w+")
    passwordsFile = {}

def password_Locker():
    print("Password Locker")
    print("1. Find your Password")
    print("2. Save your Password")
    print("3. Update pass")
    print("4. Exit")

    try:
        optionNumber = int(input("Enter your option number:"))
    except:
        print("Enter the provided Number")
        optionNumber = int(input("Enter your option number:"))
    while optionNumber:
        if optionNumber == 1:
            passFinder()
        elif optionNumber == 2:
            passSave()
        elif optionNumber == 3:
            passUpdate()
        elif optionNumber == 4:
            break
        else:
            print("invalid option")
        optionNumber = int(input("Enter your option number:"))
    print("Now, Exiting")


def passFinder():
    acc = input("Enter your email or platform")

    if acc in passwordsFile.keys():
        passEncrypted = passwordsFile[acc]
        pyperclip.copy(decode(passEncrypted))
        print("Password copied... 60 sec!!!")
        time.sleep(60)
        print("Password Erased from clip board")
    else:
        print("Invalid Account")

def passUpdate():
    acc = input("Enter your email or platform")
    if acc in passwordsFile.keys():
        newpass = input("Enter new password: ")
        passwordsFile[acc] = encode(newpass)
        json.dump(passwordsFile, open(file, "w"))
        print("New Password Saved")

def decode(passEncrypted):
    decodedPass = []
    for i in range(len(passEncrypted)):
        decodePass = chr(ord(passEncrypted[i]) + len(passEncrypted))
        decodedPass.append(decodePass)
    passDecoded = "".join(decodedPass)
    return passDecoded

def passSave():
    acc = input("Enter your email or platform")
    password = input("Enter your password to add")
    passwordsFile[acc] = encode(password)
    json.dump(passwordsFile, open(file, "w"))
    print("Password Saved")
def encode(password):
    encodedPass = []
    for i in range(len(password)):
        encodePass = chr(ord(password[i]) - len(password))
        encodedPass.append(encodePass)
    passEncrypted = "".join(encodedPass)
    return passEncrypted

password_Locker()
