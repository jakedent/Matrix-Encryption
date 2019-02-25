# File encryption only (monolithic).
# This test implements file encryption encryption and decryption.
# Files are encrypted with one round of encryption with the same algorithm as the secret message cipher.
# Further work on this function would implement encryption rounds with key permutation.
# Test 005 implements this algorithm as a function to be called from user interaction.
import binascii
import numpy as np
import pathlib
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# File to be encrypted
filename = filedialog.askopenfilename()
# filename = 'test.png'
file_type = pathlib.Path(filename).suffix  # File type

# Open file and read as binary
with open(filename, 'rb') as f:
    content = f.read()
file_to_hex = binascii.hexlify(content)  # Convert entire file to hexadecimal

# Show user file hex file conversion
print("\nConverted file to hexadecimal.", file_to_hex.decode("utf-8"))  # Decode byte string
# Get first 64 bits of file
first_64_bits = file_to_hex[:16]
# Show user first 64-bits of file
print("\nCollected first 64-bits of file :    ", first_64_bits.decode("utf-8"))

# Split 64-bit segment into two 32-bit segments
print("\nSplitting 64-bits into two 32-bit segments...")
split_64 = first_64_bits.decode("utf-8")
splits = 8
two_bytes = [split_64[i:i + splits] for i in range(0, len(split_64), splits)]
print("\nSplit complete :     ", two_bytes)

# Convert hex to base16 for simple arithmetic
bytes_b16 = [int(x, 16) for x in two_bytes]
print("\nConverted hex to base 16 :    ", bytes_b16)

# Create matrix of two bytes (32-bit)
f64_matrix = np.matrix(bytes_b16)
print("\nInserted base 16 values into matrix:     ", f64_matrix)

# Generate Key Matrix
k = np.random.randint(2, 10, f64_matrix.shape, dtype=np.int)
print("\nGenerated key matrix : ", k)

# encrypt
print("\nEncrypting base16 values with key...")
encrypted = np.multiply(k, f64_matrix)
print("\nEncrypted base16 values: ", encrypted)
base16_list = np.array(encrypted)[0].tolist()  # Convert matrix to array then list for base16 conversion.
# Convert base16 back to hex
print("\nConverting encrypted base16 values to hexadecimal...")

encrypted_hex_a, encrypted_hex_b = [hex(x)[2:].zfill(9) for x in base16_list]
print("\nNew, encrypted 32-bit hexadecimal value :      ", encrypted_hex_a, encrypted_hex_b)

removed = file_to_hex[16:]
appended = [encrypted_hex_a + encrypted_hex_b + removed.decode("utf-8")]
appended_to_string = appended
appended_string = ''.join(str(e) for e in appended_to_string)
print("\nAdded encrypted segments to file :     ", appended_string)
print("\nSaving encrypted file...")
with open('encryptedFile' + file_type, 'wb') as encrypted_file:
    encrypted_file.write(binascii.a2b_hex(appended_string.strip()))
    encrypted_file.close()

# Decrypt
print("\nDecrypting file...")
decrypt_segments = np.floor_divide(encrypted, k)
print("Decrypted initial 64-bits from hex", decrypt_segments)
decrypted_base16_list = np.array(decrypt_segments)[0].tolist()  # Convert to list.
# Convert base16 back to hex
decrypted_hex_a, decrypted_hex_b = [hex(x)[2:].zfill(8) for x in decrypted_base16_list]
print("\nConverted encrypted base16 values to original hexadecimal :    ", decrypted_hex_a, decrypted_hex_b)

removed_encrypted = file_to_hex[16:]
append_decrypted = [decrypted_hex_a + decrypted_hex_b + removed_encrypted.decode("utf-8")]
decrypted_to_string = append_decrypted
decrypted_string = ''.join(str(e) for e in decrypted_to_string)
print("Added decrypted segments back to file :      ", decrypted_string)

print("Saving decrypted file...")
decrypted_data = decrypted_string
decrypted_data = decrypted_data.upper()
decrypted_data = decrypted_data.strip()
decrypted_data = decrypted_data.replace(' ', '')
decrypted_data = decrypted_data.replace('\n', '')
decrypted_data = binascii.a2b_hex(decrypted_data)
with open('decryptedFile' + file_type, 'wb') as image_file:
    image_file.write(decrypted_data)


