# This test implements encryption and key permutation rounds.
# Further work in test003.py will implement user interaction.
import numpy as np


# Pre-defined number of encryption and key permutation rounds.
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


# Decryption rounds based on the pre-defined encryption and key permutations rounds.
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


message = input("\nMessage to encrypt: ")
message.lower()

# plain text alpha-numeric-conversion
message_output = []
for character in message:
    number = ord(character) - 96  # ASCII conversion table (minus 96 from ASCII lower case alphabet, numerical values)
    message_output.append(number)

# plain text numeric-to-alpha-conversion
decoded_message = []
for character in message:
    number = ord(character)
    decoded_message.append(number)

p_matrix = np.matrix(message_output)
print("\nMessage converted to alpha-numeric values : ", p_matrix)
k = np.random.randint(0, 99, p_matrix.shape, dtype=np.int)
print("\nGenerated key matrix : ", k)

encryption_and_permutation()
decryption_and_permutation()
