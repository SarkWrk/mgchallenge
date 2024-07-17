# Why?
This is code that I created due to something Mgloven said. I don't remember when, but it was in [Ice](https://discord.com/channels/@me/759616929085784065).

# What does the code do?
This code runs a basic Ceaser Chiper ([link to Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)).

# How do I use it?

## Setup
The program is coded in Python. So, if not already installed, download the newest version of Python from the Microsoft Store or [the Python Software Foundation's official site](https://www.python.org/downloads/).
After installing Python, download the code, or create your own Python file with the code.

## Running the code
You can run the code in your favourite IDE of choice, or through the terminal.

When running the code you are given the question `Are you decoding a file/text or encoding text? (d = decode, e = encode)`. You **must** answer using either `d` or `e` (case inspecific).
### Encoding
After responding, if you responded with wanting to encode (if you want to decode, see the next section): the program will ask you for a seperator (used so that the program can later decode the text). When decoding the *same* seperator must be used.
Next, you give the program the text you want to encode.
After the encoding, the program will give you the text it encoded.
When giving the encoded text, the program will ask if you want to save the encoded text to a text file. If answered `y` (case insensitive) to, the program will attempt to create a text file called `EncodedText.txt` to save the text to.
If the creation failed, it's most likely due to the file already existing. The program will ask if you want to override the contents of the file.
### Decoding
After responding, if you responded with wanting to decode: the program will try to find a text file called `EncodedText.txt`. If found, it will ask if that is the text you're looking to decode. If unsuccessful, or the text found is not the text you want to decode, the program will ask for the text you want to decode.
Afterwards, the code will ask you for the seperator used by the program when encoding the text.
Finally, the program will give you the decoded text.
