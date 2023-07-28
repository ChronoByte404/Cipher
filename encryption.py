def create_cipher_key():
    key = {
        'a': '@', 'b': '!', 'c': '#', 'd': '$', 'e': '%', 'f': '&', 'g': '*',
        'h': '(', 'i': ')', 'j': '+', 'k': '-', 'l': '/', 'm': '=', 'n': '?',
        'o': '[', 'p': ']', 'q': '{', 'r': '}', 's': '<', 't': '>', 'u': '|',
        'v': '^', 'w': ':', 'x': ';', 'y': '"', 'z': "'"
    }
    return key

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char in key:
            encrypted_message += key[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    reverse_key = {value: key for key, value in key.items()}
    decrypted_message = ""
    for char in encrypted_message:
        if char in reverse_key:
            decrypted_message += reverse_key[char]
        else:
            decrypted_message += char
    return decrypted_message

cipher_key = create_cipher_key()
plaintext = input("You: ")
encrypted_text = encrypt(plaintext, cipher_key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, cipher_key)
print("Decrypted:", decrypted_text)
