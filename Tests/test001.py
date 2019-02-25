# This is a simplified yet functional prototype of cipher algorithm.
# User inserts the message to be encrypted, which is converted to alpha-numeric values and stored as a NumPy Matrix.
# A Key matrix is generated with random numerical values, to the size of the plain text matrix.
# Encryption is one round of multiplication of the key matrix and the plain text matrix.
# Decryption is the one round of division of the encrypted plain text matrix and the key matrix.
# Further work in test002.py will implement rounds and key matrix permutation.
import numpy as np

message = input('Message to encrypt: ')
message.lower()

# alpha-numeric-conversion
message_output = []
for character in message:
    number = ord(character) - 96  # ASCII conversion table (minus 96 from ASCII lower case alphabet, numerical values)
    message_output.append(number)

p_matrix = np.matrix(message_output)

print("The matrix : ", p_matrix)
print("Matrix shape : ", p_matrix.shape)

print("Generating key matrix...")
k = np.random.randn(*p_matrix.shape)
print("Generated key matrix : ", k)

# encrypt
encrypted = np.multiply(k, p_matrix)
print("\nEncrypted: \n", encrypted)

# decrypt
decrypted = np.divide(encrypted, k)
print("\nDecrypted: \n", decrypted)
