#script for decrypting a caesar cipher
import matplotlib.pyplot as plt

#english letter percentages for predictions
ENGLISH_FREQUENCIES = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.130,
    'F': 0.022, 'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002,
    'K': 0.008, 'L': 0.040, 'M': 0.024, 'N': 0.067, 'O': 0.075,
    'P': 0.019, 'Q': 0.001, 'R': 0.060, 'S': 0.063, 'T': 0.091,
    'U': 0.028, 'V': 0.010, 'W': 0.024, 'X': 0.001, 'Y': 0.020, 'Z': 0.001
}

#Decrypter (clock maths) SUB.
def decrypt_caesar(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext.upper():
        if char.isalpha():
            letter_num = ord(char) - ord('A')
            shifted_num = (letter_num - key) % 26
            decrypted_text += chr(shifted_num + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

#Cost function (parabola) SUB
def calculate_cost(text):
    total_letters = sum(1 for char in text if char.isalpha())
    if total_letters == 0:
        return float('inf')

    cost_score = 0.0
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = text.count(letter)
        guess_percentage = count / total_letters
        difference = guess_percentage - ENGLISH_FREQUENCIES[letter]
        cost_score += difference **2
    return cost_score

#cracker loop and plotter SUB.
def crack_and_plot_cipher(secretmessage):
    tested_keys = []
    calculated_costs = []

    best_key = -1
    lowest_cost = float('inf')
    best_decryption = ""
    for test_key in range(26):
        current_guess = decrypt_caesar(secretmessage, test_key)
        current_cost = calculate_cost(current_guess)

        tested_keys.append(test_key)
        calculated_costs.append(current_cost)

        print(f"  -> Testing Key {test_key:2d} | Error Cost Score: {current_cost:.5f}")

        if current_cost < lowest_cost:
            lowest_cost = current_cost
            best_key = test_key
            best_decryption = current_guess


    print("\nScan Complete")
    print(f"Found lowest point on the curve at Key: {best_key}")
    print(f"Decrypted Message: {best_decryption}")


    plt.plot(tested_keys, calculated_costs, color='royalblue', marker='o')

    plt.plot(best_key, lowest_cost, color='limegreen', marker='o', markersize=10)

    plt.grid(True)
    plt.show()

intercepted_data = "Gfjk"
crack_and_plot_cipher(intercepted_data)
