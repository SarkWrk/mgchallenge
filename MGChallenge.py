#The following code will be a bad example of an encodedTextFromFileoding/decoding machine

import random # Get a random number for encoding
import os # Used for getting the path for creating EncodedText.txt

hasProgramSucceeded = False
fileDirectory = os.path.dirname(__file__) # Gets file directory

print("Tip: Press ctrl + c to hard-exit this program.")

encodedTextFileName = input("Is there a specific file name you want to use in this program? (leave blank if not)\n")
fileEncoding = input("What is the file encoded in? (ex: UTF-8, UTF-16)\n")

if encodedTextFileName == "":
    encodedTextFileName = "EncodedText.txt"

encodedTextPath = os.path.join(fileDirectory, encodedTextFileName) # Absolute path for encodedTextFileName.txt

def GetEncodeInt() ->int:
    encodeInt = input("\nIs there a specific offset you want to use?\n")

    if encodeInt.isnumeric() == False:
        print("\nThe value you provided was not a number. Will proceed with a randomly chosen number.")
        encodeInt = random.randint(-20, 20)
    else:
        encodeInt = int(encodeInt)
    
    if encodeInt != 0:
        return encodeInt
    else:
        return GetEncodeInt()

def ChangeText(changeBy:int, text:str="") ->str:
    changedText = ""
    failedToConvertCharacter = False

    for character in text:
        print("Character: " + character + " | Ord: " + str(ord(character)) + " | Change: " + str(changeBy))

        try:
            changedText = changedText + chr(ord(character) + changeBy)
        except:
            failedToConvertCharacter = True
            changedText = changedText + character
    
    if failedToConvertCharacter == True:
        print("Some of the text was unable to be converted.")

    return changedText

def WriteFile(text:str="", skip:bool=False) ->bool:
    failedCreation = False
    wroteToFile = False

    if skip == False:
        try:
            with open(encodedTextPath, "x", encoding=fileEncoding) as encodedFile:
                encodedFile.write(text)
                wroteToFile = True
        except:
            print("\nUnable to create file! This is most likely due to a file with this name already created.")

            failedCreation = True

    if failedCreation == True or skip == True:
        shouldOverrideFile = input("\nDo you want to override the information in '" + encodedTextFileName + "'? (y/n)\n")
        if shouldOverrideFile == "yes" or shouldOverrideFile.casefold() == "y":
            print("Overriding contents with encoded text.")

            try:
                with open(encodedTextPath, "w", encoding=fileEncoding) as encodedFile:
                    encodedFile.write(text)
                    wroteToFile = True
            except:
                print("\nCould not override file. Please copy the text if you're saving it instead please.\n")

    return wroteToFile

def CloneFile(text=""):
    clonePath = os.path.join(fileDirectory, encodedTextFileName.split(".")[0] + " - Clone.txt")

    with open(clonePath, "x", encoding=fileEncoding) as clonedFile:
        clonedFile.write(text)

def EncodeFile(separator:str="|+|-"):

    with open(encodedTextPath, "r", encoding=fileEncoding, newline='') as unencodedFile:
        unencodedText = unencodedFile.read()
        

    copyFile = input("Do you want to clone the original file?\n")

    if copyFile.casefold() == "y" or copyFile.casefold() == "yes":
        CloneFile(text=unencodedText)

    encodeInt = GetEncodeInt()

    encodedText = str(encodeInt) + separator + "\n" + ChangeText(encodeInt, unencodedText)

    writeToFile = encodedText

    if WriteFile(writeToFile, True) == False:
        print("\nFinal outcome:\n" + encodedText)

def Main():
    global hasProgramSucceeded

    userInputForDecodeOrEncode = input("Are you decoding a file/text, encoding a file, or encoding text? (d/f/e respectively)\n")
    separator = input("\nWhat do you want to use as a separator between text decoding? (default is |+|-))\n")

    hasProgramSucceeded = True
    decoder = 0

    if separator == "":
        separator = "|+|-"
    if userInputForDecodeOrEncode.casefold() == "text" or userInputForDecodeOrEncode == "e":
        encodeInt = GetEncodeInt()

        text = input("\nWhat is the text you are trying to encode?\n")
        encodedText =  str(encodeInt) + separator + ChangeText(encodeInt, text=text)

        print("\nFinal outcome:\n" + encodedText)

        createFile = input("\nDo you want to create a file with this information? (y/n)\n")

        if createFile.casefold() == "yes" or createFile.casefold() == "y":
            WriteFile(encodedText)

    elif userInputForDecodeOrEncode.casefold() == "decode" or userInputForDecodeOrEncode == "d":
        readFile = False
        try:
            with open(encodedTextPath, "r", encoding=fileEncoding, newline='') as encodedFile:
                text = encodedFile.read()
                readFile = True
        except:
            text = input("\nWhat is the text you want to decode:\n")
            
        if readFile == True:
            confirmCorrectText = input("\nIs \" " + str(text) + " \" what you are trying to decode? (y/n) \n")
            if confirmCorrectText.casefold() == "yes" or confirmCorrectText.casefold() == "y":
                pass
            else:
                text = input("\nWhat is the text you want to decode:\n")

        splitEncodedText = text.split(separator)

        if splitEncodedText[0].isnumeric() == True:
            decoder = int(splitEncodedText[0])

            removeText = text.replace(str(decoder) + separator, "")

            decodedText = ChangeText(-decoder, removeText)

            print("\nThe original text was:\n" + decodedText)

            WriteFile(decodedText, True)
        else:
            print("The seperator you gave does not align with the seperator used to encode.")
            hasProgramSucceeded = False
    
    elif userInputForDecodeOrEncode.casefold() == "file" or userInputForDecodeOrEncode == "f":
        # try:
            EncodeFile(separator=separator)
        # except:
        #     hasProgramSucceeded = False
    
    else:
        hasProgramSucceeded = False

while hasProgramSucceeded == False:
    Main()

import time

print("Programme will close in 30s.")
time.sleep(30)
