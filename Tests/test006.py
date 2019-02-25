#!/usr/bin/env python3
# This test implements encryption and key permutation rounds and user interaction.
# Further work in test004.py will implement file encryption.
import time
import numpy as np
from test005 import run_file_algorithm, run_file_decryption


def encryption_and_permutation():
    global key_1, key_2, key_3, e_round_zero, e_round_one, e_round_two, e_round_three
    # Start (Round 0)
    e_round_zero = np.multiply(k, p_matrix)  # Multiply the key k, with the plain text matrix p_matrix.
    print("\nInitial encryption (K - R0) : ", e_round_zero)

    # Round one
    key_1 = np.roll(k, 1)
    print("\nKey Permutation 1 (K1) : ", key_1)
    e_round_one = np.multiply(key_1, e_round_zero)
    print("\nEncryption round 1 (R1) : ", e_round_one)

    # Round two
    key_2 = np.roll(key_1, 2)
    print("\nKey Permutation 2 (K2) : ", key_2)
    e_round_two = np.multiply(key_2, e_round_one)
    print("\nEncryption round 2 (R2) : ", e_round_two)

    # Round three
    key_3 = np.roll(key_2, 3)
    print("\nKey Permutation 3 (K3) : ", key_3)
    e_round_three = np.multiply(key_3, e_round_two)
    print("\nEncryption round 3 (R3) : ", e_round_three)

    print("\nFour rounds of encryption (R0-R3) : ", e_round_three)


def decryption_and_permutation():
    # Start at round 3
    d_round_zero = np.divide(e_round_three, key_3)
    print("\nDecryption round 1 (K3) : ", d_round_zero)
    d_round_one = np.divide(e_round_two, key_2)
    print("\nDecryption round 2 (K2) : ", d_round_one)
    d_round_two = np.divide(e_round_one, key_1)
    print("\nDecryption round 3 (K1) : ", d_round_two)
    d_round_three = np.divide(e_round_zero, k)
    print("\nDecryption round 4 (K) : ", d_round_three)

    print("\nDecoded message : ", ''.join(map(chr, decoded_message)))


print("\nGroup 9 cipher software - the GUI took too long. Apologies.")

while True:    # infinite loop
    n = input("\nDo you want to encrypt a file or a secret message? : ")
    n.lower()
    if n == "q" or n == "quit":
        print("\nGoodbye.")
        break  # stops the loop
    elif n == 'f' or n == "file":
        print("\nLoading file encryption algorithm...")
        run_file_algorithm()
        print("\nEncrypted file saved to cipher package directory.")
        print("\nDecrypting file...")
        time.sleep(2)
        run_file_decryption()
        print("\nFile successfully decrypted and saved to cipher package directory.", "\nReturning to main menu...")
    elif n == "sm" or n == "secret message" or n == "message" or n == "m" or n == "secret" or n == "s":
        print("\nLoading plain text encryption algorithm")
        message = input("\nMessage to encrypt: ")
        message.lower()

        # plain text alpha-numeric-conversion
        message_output = []
        for character in message:
            number = ord(
                character) - 96  # ASCII conversion table (minus 96 from ASCII lower case alphabet, numerical values)
            message_output.append(number)

        # plain text numeric-to-alpha-conversion
        decoded_message = []
        for character in message:
            number = ord(character)
            decoded_message.append(number)

        p_matrix = np.matrix(message_output)
        print("\nMessage converted to alpha-numeric values : ", p_matrix)
        k = np.random.randint(0, 99, p_matrix.shape, dtype=np.int)
        print("\nGenerated key matrix : ", k, "\nReady to encrypt...")
        encryption_and_permutation()
        print("\nReady to decrypt : ", e_round_three)
        run_decryption = input("\nYes or No : ")
        run_decryption.lower()
        if run_decryption == "n" or run_decryption == "no":
            print("\nClearing data... Goodbye.")
            break
        elif run_decryption == "y" or run_decryption == "yes":
            decryption_and_permutation()
            print("\nAll processes successful... Goodbye.")
            break
        else:
            print("\nSorry, invalid input.")
            continue
    else:
        print("\nSorry, please enter a valid option : ", "\n\nOptions: f (file) m (message) q (quit)")
        continue

