#The following code will be a bad example of an encodedTextFromFileoding/decoding machine

import random # Get a random number for encoding
import os # Used for getting the path for creating EncodedText.txt

hasProgramSucceeded = False
fileDirectory = os.path.dirname(__file__) # Gets file directory
encodedTextPath = os.path.join(fileDirectory, "encodedText.txt") # Absolute path for encodedText.txt

print("Tip: Press ctrl + c to hard-exit this program.")

def main():
    userInputForDecodeOrEncode = input("Are you decoding a file/text or encode text?\n")
    separator = input("\nWhat do you want to use as a seperator between text decoding: (default is |+|-))\n")
    global hasProgramSucceeded
    hasProgramSucceeded = True
    decoder = 0

    if separator == "":
        separator = "|+|-"
    if userInputForDecodeOrEncode.casefold() == "encode" or userInputForDecodeOrEncode == "e":
        print("Alright, encoding!")

        encodeInt = random.randint(1, 100)

        text = input("\nWhat is the text you are trying to encode?\n")
        encodedText = ""

        encodedText = encodedText + str(encodeInt) + separator

        for i in text:
            encodedLetter = chr(ord(i) + encodeInt)
            encodedText = encodedText + encodedLetter
        print("\nFinal outcome:\n" + str(encodedText))

        createFile = input("\nDo you want to create a file with this information? (y/n)\n")

        if createFile.casefold() == "yes" or createFile.casefold() == "y":
            try:
                f = open(encodedTextPath, "x", encoding="utf-16")
                f.write(encodedText)
                f.close()
            except:
                print("\nUnable to create file! This is most likely due to a file with this name already created.")
                shouldOverrideFile = input("\nDo you want to override the information in 'encodedText.txt'? (y/n)\n")
                if shouldOverrideFile == "yes" or shouldOverrideFile.casefold() == "y":
                    print("Overriding contents with encodedTextFromFileoded text.")
                    try:
                        x = open(encodedTextPath, "w", encoding="utf-16")
                        x.write(encodedText)
                        x.close()
                    except:
                        print("\nCould not override file. Please copy the text if you're saving it instead please.\n")
                        print(encodedText)
                        print("\n")
                else:
                    print("Will not override")

        print("Finished!")

    elif userInputForDecodeOrEncode.casefold() == "decode" or userInputForDecodeOrEncode == "d":
        print("Alright, decoding!")

        try:
            encodedTextFromFile = open(encodedTextPath, "r", encodedTextFromFileoding="utf-16")
            text = encodedTextFromFile.read()
            encodedTextFromFile.close()
            confirmCorrectText = input("\nIs \n\" " + str(text) + " \"\n what you are trying to decode? (y/n) \n")
            if confirmCorrectText.casefold() == "yes" or confirmCorrectText.casefold() == "y":
                print("Okay!")
            else:
                text = input("\nWhat is the text you want to decode:\n")
        except:
            print("Can't find file.\n Do you have a text that you can input instead?")
            text = input("\nText:\n")

        splitEncodedText = text.split(separator)

        if splitEncodedText[0].isnumeric() == True:
            decoder = int(splitEncodedText[0])

            removeText = text.replace(str(decoder) + separator, "")

            decodedText = ""

            for i in removeText:
                decodedLetter = chr(ord(i) - decoder)
                decodedText = decodedText + decodedLetter

            print("\nThe text was:\n" + str(decodedText))
        else:
            print("The seperator you gave does not align with the seperator you used to encodedTextFromFileode.")
            hasProgramSucceeded = False

while hasProgramSucceeded == False:
    main()

import time

print("\nYou may exit this program at any time. It will automatically close after 30s.")
time.sleep(30)
