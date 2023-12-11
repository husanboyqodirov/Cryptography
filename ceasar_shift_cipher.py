# Coded with love by Husanboy Qodirov
# Cryptography & Network Security Lab

# encrypt function takes two arguments: plaintext (string) and shift key (integer)
def encrypt(plaintext, key):
    ciphertext = ""
    # iterate through plaintext
    for char in plaintext:
        # if this character is space, then simply add space
        if (char == " "):
            ciphertext += " "
        # if this character is uppercase
        elif (char.isupper()):
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        # if this caracter is lowercase
        elif (char.islower()):
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        # if this is speacial character, then simply add it
        else:
            ciphertext += char
    return ciphertext

# decrypt function takes two arguments: ciphertext (string) and shift key (integer)
def decrypt(ciphertext, key):
    plaintext = ""
    # iterate through ciphertext
    for char in ciphertext:
        # if this character is space, then simply add space
        if (char == " "):
            plaintext += " "
        # if this character is uppercase
        elif (char.isupper()):
            plaintext += chr((ord(char) - key - 65) % 26 + 65)
        # if this caracter is lowercase
        elif (char.islower()):
            plaintext += chr((ord(char) - key - 97) % 26 + 97)
        # if this is speacial character, then simply add it
        else:
            plaintext += char
    return plaintext

# brute_force function takes one argument: ciphertext, and performs decryption on all possible 25 key values starting from 1 until 25. 
def brute_force(ciphertext):
    for key in range(1, 26):
        plaintext = decrypt(ciphertext, key)
        print('Hacking key %s: %s' % (key, plaintext))

# program entry point, display menu until user chooses to exit
while(True):
    try:
        option = int(input("\nWhat do you want to do?\n1 Encrypt\n2 Decrypt\n3 Brute Force\n4 Exit\n: "))
    # if entered value is not integer
    except ValueError:
        print("Enter only numbers to choose your action.")
        continue

    # encryption
    if (option == 1):
        plaintext = input("\nEnter plaintext: ")
        while(True):
            try:
                key = int(input("Enter shift key: "))
            except ValueError:
                print("Enter only numbers for shift key.")
                continue
            # Accept key value only if it is in range of 1 to 25.
            # Anything under or below this suggested key value causes 
            # similar cipher text for keys used between suggested range
            # or no security at all: for example encrypting plaintext with
            # key 0 or 26 results in no cipher text. Or key over 25 such as
            # 29 results in same cipher text for key 3.
            # So all in all, effective key length is 25.
            if (key < 1 or key > 25):
                print("Shift key should be between 1 to 25")
                continue
            break
        print("Cipher text: " + encrypt(plaintext, key))

    # decryption
    elif (option == 2):
        ciphertext = input("\nEnter cipher text: ")
        while(True):
            try:
                key = int(input("Enter shift key: "))
            except ValueError:
                print("Enter only numbers for shift key.")
                continue
            if (key < 1 or key > 25):
                print("Shift key should be between 1 to 25")
                continue
            break
        print("Plain text: " + decrypt(ciphertext, key))

    # brute-force
    elif (option == 3):
        ciphertext = input("\nEnter cipher text: ")
        brute_force(ciphertext)

    # exit program
    elif (option == 4):
        exit()

    # if entered option number is out of range
    else:
        print("Enter numbers from 1 to 4 to choose your action.")
        continue