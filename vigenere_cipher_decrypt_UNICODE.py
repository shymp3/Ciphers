#Decrypts 6-digit hex Vigenere ciphertext across the full Unicode range.

# ---sub---
def vigenere_decrypter(ciphertext,key):
    plaintext = []
    key_index = 0
    MAX_UNICODE = 1114112

    for i in range(0, len(ciphertext), 6):
        hex_chunk = ciphertext[i:i+6]
        char_val = int(hex_chunk, 16)
        shift_val = ord(key[key_index % len(key)])

        decrypted_val = (char_val - shift_val) % MAX_UNICODE

        plaintext.append(chr(decrypted_val))
        key_index += 1

    return "".join(plaintext)

# ---main---

if __name__ == '__main__':

    print(" ---Vigenere Decrypter (UNICODE HEX)---")
    secret_message = input("Enter message to decode: ").strip()
    secret_key = input("Enter secret key: ")

    decoded_message = vigenere_decrypter(secret_message, secret_key)

    print("Decoded message:",decoded_message)