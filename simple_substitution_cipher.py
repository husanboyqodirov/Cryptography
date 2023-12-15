"""
The Simple Substitution Cipher
Coded with love by Husanboy Qodirov
"""

import random

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # Let the user specify if they are encrypting or decrypting:
    while True:  # Keep asking until the user enters e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        print('Please specify the key to use.')
        if myMode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            myKey = generateRandomKey()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if checkKey(response):
                myKey = response
                break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Perform the encryption/decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    # Display the results:
    print('The %sed message is:' % (myMode))
    print(translated)

def checkKey(key):
    """Return True if key is valid. Otherwise return False."""
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print('There is an error in the key or symbol set.')
        return False
    return True

def encryptMessage(message, key):
    """Encrypt the message using the key."""
    return translateMessage(message, key, 'encrypt')

def decryptMessage(message, key):
    """Decrypt the message using the key."""
    return translateMessage(message, key, 'decrypt')

def translateMessage(message, key, mode):
    """Encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # The symbol is not in LETTERS, just add it unchanged.
            translated += symbol

    return translated

def generateRandomKey():
    """Generate and return a random encryption key."""
    key = list(LETTERS)  # Get a list from the LETTERS string.
    random.shuffle(key)  # Randomly shuffle the list.
    return ''.join(key)  # Get a string from the list.

# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()