
import numpy as np

# Logistic Map
def logistic_map(x, r):
    return r * x * (1 - x)


# Divide the state space into intervals
def get_interval(x, num_chars):
    index = int(x * num_chars)
    return min(index, num_chars - 1)


# Encryption
def encrypt(message, x0, r, num_chars=26):
    x = x0
    ciphertext = []

    for char in message.upper():
        if char == " ":
            ciphertext.append(0)
            continue

        target_interval = ord(char) - ord("A")

        count = 0
        max_iterations = 100000

        while count < max_iterations:
            x = logistic_map(x, r)
            count += 1

            if get_interval(x, num_chars) == target_interval:
                ciphertext.append(count)
                break

        if count == max_iterations:
            raise ValueError("Target interval not reached.")

    return ciphertext, x


# Decryption
def decrypt(ciphertext, x0, r, num_chars=26):
    x = x0
    plaintext = ""

    for count in ciphertext:
        if count == 0:
            plaintext += " "
            continue

        for _ in range(count):
            x = logistic_map(x, r)

        index = get_interval(x, num_chars)
        plaintext += chr(index + ord("A"))

    return plaintext


# Demonstration
if __name__ == "__main__":
    message = "HELLO WORLD"

    r = 4.0
    x0 = 0.123456789
    num_chars = 26

    encrypted, final_state = encrypt(message, x0, r, num_chars)
    decrypted = decrypt(encrypted, x0, r, num_chars)

    print("Original Message:", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
    print("Successful Recovery:", message == decrypted)
