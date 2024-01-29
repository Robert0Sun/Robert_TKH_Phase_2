import sys


def encrypt(message, k):
#we're going to convert any captialized letter into lowercase
    message = message.lower()
    encrypted_text = ""
    # #we're going to be looping through all the characters in the text we want to encrypt

    for char in message:
        if char.islower():
            #97 is the ASCII value of 'A'
            #26 is the how many letters in the alphabet, to ensure that we are going to be in the range of the alphabet
            #this code is for any lowercase letter that is going to be shifted
            #k is the value of how many shifts its going to take to change the letter, with the addition to shift to the right
            encrypted_text += chr((ord(char) + k - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

original_message = "The Goose Does Not Lay Eggs On Wednesday"
encrypted_message = encrypt(original_message, 5)
print(encrypted_message)


def decrypt(message, k):
    message = message.lower()
    encrypted_text = ""
    for char in message:
        if char.islower():
             #97 is the ASCII value of 'A'
            #26 is the how many letters in the alphabet, to ensure that we are going to be in the range of the alphabet
            #this code is for any lowercase letter that is going to be shifted
            #k is the value of how many shifts its going to take to change the letter, with the subtraction to shift to the left
            encrypted_text += chr((ord(char) - k - 97) % 26 + 97)
        else:
            encrypted_text += char    
    return encrypted_text


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)