#The following code will be a bad example of an encoding/decoding machine
import random
import time

hasdecoderfailed = True

print("Tip: Press ctrl + c to hard-exit this program.")

def main():
    userInputforDorE = input("Are you decoding a file/text or encoding text?\n")
    sepperator = input("\nWhat do you want to use as a seperator between text decoding: (default is |+|-))\n")
    global hasdecoderfailed
    hasdecoderfailed = False
    decoder = 0

    if sepperator == "":
        sepperator = "|+|-"
    if userInputforDorE.casefold() == "encode" or userInputforDorE == "e":
        print("Alright, encoding!")
        time.sleep(1)

        encint = random.randint(1, 100)

        text = input("\nWhat is the text you are trying to encode?\n")
        encodedtext = ""

        encodedtext = encodedtext + str(encint) + sepperator

        for i in text:
            enclet = chr(ord(i) + encint)
            encodedtext = encodedtext + enclet
        print("\nFinal outcome:\n" + str(encodedtext))

        createfile = input("\nDo you want to create a file with this information? (y/n)\n")

        if createfile.casefold() == "yes" or createfile.casefold() == "y":
            try:
                f = open("EncodedText.txt", "x")
                x = open("EncodedText.txt", "w")
                x.write(encodedtext)
                x.close()
                f.close()
            except:
                print("\nUnable to create file! This is most likely due to a file with this name already created.")
                shouldoverride = input("\nDo you want to override the information in 'EncodedText.txt'? (y/n)\n")
                if shouldoverride == "yes" or shouldoverride.casefold() == "y":
                    print("Overriding contents with encoded text.")
                    try:
                        x = open("EncodedText.txt", "w")
                        x.write(encodedtext)
                        x.close()
                    except:
                        print("\nCould not override file. Please copy the text if you're saving it instead please.\n")
                        print(encodedtext)
                        print("\n")
                else:
                    print("Will not override")

        print("Finished!")

    elif userInputforDorE.casefold() == "decode" or userInputforDorE == "d":
        print("Alright, decoding!")
        time.sleep(1)

        try:
            Enc = open("EncodedText.txt", "r")
            text = Enc.read()
            Enc.close()
            confirm = input("\nIs \n\" " + str(text) + " \"\n what you are trying to decode? (y/n) \n")
            if confirm.casefold() == "yes" or confirm.casefold() == "y":
                print("Okay!")
            else:
                text = input("\nWhat is the text you want to decode:\n")
        except:
            print("Can't find file.\n Do you have a text that you can input instead?")
            text = input("\nText:\n")

        splittext = text.split(sepperator)

        if splittext[0].isnumeric() == True:
            decoder = int(splittext[0])
        else:
            print("The seperator you gave does not align with the seperator you used to encode.")
            print("This program is going to restart in 3s")
            time.sleep(3)

        if hasdecoderfailed == False:
            removedtext = text.replace(str(decoder) + sepperator, "")

            dectext = ""

            for i in removedtext:
                declet = chr(ord(i) - decoder)
                dectext = dectext + declet

            print("\nThe text was:\n" + str(dectext))
        else:
            hasdecoderfailed = True
    else:
        print("Not a valid input")

while hasdecoderfailed == True:
    main()

print("\nYou may exit this program at any time. It will automatically close after 30s.")
time.sleep(30)
