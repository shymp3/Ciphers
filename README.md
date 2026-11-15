# ***Python Ciphers & Cryptanalysis***

A collection of Python encryption, decryption, and automated codebreaking tools built using modular arithmetic and statistical frequency analysis.

## *Projects* 
 
### 1. Automated Caesar Cipher Codebreaker (`caesar_codebreaker.py`)
* **Frequency Analysis:** Compares decrypted letter distributions against standard English letter frequencies using a cost function to find the most likely shift automatically.
* **Data Visualisation:** Uses `matplotlib` to plot the error cost across all 26 possible keys and highlight the optimal key in green.

### 2. Unicode Hex Vigenère Cipher (`vigenere_cipher_encrypt_UNICODE.py`) and (`vigenere_cipher_decrypt_UNICODE.py`)
* **Full Unicode Support:** Encrypts and decrypts standard text, symbols, and special characters across the full Unicode range (`0` to `1,114,111`) using modular arithmetic.
* **6-Digit Hexadecimal Output:** Converts encrypted code points into fixed-width 6-character hex strings so ciphertext can be copied and pasted across terminals without encoding corruption.
* **Passphrase Keys:** Accepts any text passphrase as a repeating modular shift key.
