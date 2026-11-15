#Encrypts text into 6-digit hex Vigenere ciphertext across the full Unicode range.

# ---sub---
def vigenere_encrypter(plaintext,key):
    ciphertext_hex = []
    key_index = 0
    MAX_UNICODE = 1114112

    for char in plaintext:
        char_val = ord(char)
        shift_val = ord(key[key_index % len(key)])

        encrypted_val = (char_val + shift_val) % MAX_UNICODE

        ciphertext_hex.append(f'{encrypted_val:06x}')
        key_index += 1

    return "".join(ciphertext_hex)

# ---main---

if __name__ == '__main__':

    print(" ---Vigenere Encoder (UNICODE HEX)---")
    secret_message = input("Enter message to encode: ")
    secret_key = input("Enter secret key: ")

    encoded_message = vigenere_encrypter(secret_message,secret_key)

    print("Encoded message: ")
    print(encoded_message)