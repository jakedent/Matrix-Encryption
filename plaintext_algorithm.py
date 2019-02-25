#!/usr/bin/env python3
# This test implements encryption and key permutation rounds and user interaction.
# Further work in test004.py will implement file encryption.
import numpy as np


# User input function, takes input and converts to alpha-numeric values.
def user_input_handler():
    global message, message_output, decoded_message
    message = input("[START] Insert message to be encrypted :   ")
    message.lower()
    # plain text alpha-numeric-conversion
    print("\n[Step 1] Converted message to alpha-numeric values.")
    message_output = []
    for character in message:
        number = ord(
            character) - 96  # ASCII conversion table
        message_output.append(number)

    # plain text numeric-to-alpha-conversion
    decoded_message = []
    for character in message:
        number = ord(character)
        decoded_message.append(number)


# Key generation and plaintext matrix generation.
def key_gen_p():
    global k, p_matrix
    p_matrix = np.matrix(message_output) # Generate plaintext matrix
    print("\n[Step 2] Created matrix for message.")
    print("\n[Step 3] Displaying converted message matrix : ", p_matrix)
    k = np.random.randint(0, 99, p_matrix.shape, dtype=np.int) # Generate key matrix based on plaintext shape
    print("\n[Step 4] Generated key matrix : ", k, "\n\nReady to start encryption!")


# encryption rounds and key permutation
def encryption_and_permutation():
    global key_1, key_2, key_3, e_round_zero, e_round_one, e_round_two, e_round_three
    # Start (Round 0)
    e_round_zero = np.multiply(k, p_matrix)  # Multiply the key k, with the plain text matrix p_matrix.
    print("\n[Step 5] Encryption round 0 : ", e_round_zero)

    # Round one
    key_1 = np.roll(k, 1)
    print("\n[Step 6] Key Permutation 1 : ", key_1)
    e_round_one = np.multiply(key_1, e_round_zero)
    print("\n[Step 7] Encryption round 1 : ", e_round_one)

    # Round two
    key_2 = np.roll(key_1, 2)
    print("\n[Step 8] Key Permutation 2 : ", key_2)
    e_round_two = np.multiply(key_2, e_round_one)
    print("\n[Step 9] Encryption round 2 : ", e_round_two)

    # Round three
    key_3 = np.roll(key_2, 3)
    print("\n[Step 10] Key Permutation 3 : ", key_3)
    e_round_three = np.multiply(key_3, e_round_two)
    print("\n[Step 11] Encryption round 3 : ", e_round_three)
    print("\n[Step 12] Encryption complete after four rounds (R0-R3).", "\n\nEncrypted message :    ", e_round_three)


# Decryption rounds...
def decryption_and_permutation():
    print("\nReady to start decryption!")
    # Start at round 3
    d_round_zero = np.divide(e_round_three, key_3)
    print("\n[Step 13] Decryption round 1 (K3) : ", d_round_zero)
    d_round_one = np.divide(e_round_two, key_2)
    print("\n[Step 14] Decryption round 2 (K2) : ", d_round_one)
    d_round_two = np.divide(e_round_one, key_1)
    print("\n[Step 15] Decryption round 3 (K1) : ", d_round_two)
    d_round_three = np.divide(e_round_zero, k)
    print("\n[Step 16] Decryption round 4 (K) : ", d_round_three)

    print("\n[FINISHED] Decoded message : ", ''.join(map(chr, decoded_message)))


if __name__ == '__main__':
    user_input_handler()
    key_gen_p()
    encryption_and_permutation()
    decryption_and_permutation()
