import sys


def encrypt(message, k):
    message = message.lower()
    encrypted_text = ""
    for char in message:
        if char.islower():
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