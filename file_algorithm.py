#!/usr/bin/env python3
# File encryption only (micro-arch).
# This test implements file encryption encryption and decryption.
# Files are encrypted with one round of encryption with the same algorithm as the secret message cipher.
# Further work on this function would implement encryption rounds with key permutation.
# Test 006 is the final script.
import binascii
import numpy as np
import os.path
from tkinter import *
from tkinter.filedialog import askopenfilename


# open file, read as hex, grab first 64-bits, split into 32-bit, convert to base 16, create matrix.
def open_file_handler():
    global file_type, filename, file_to_hex, f64_matrix
    root = Tk()
    root.withdraw()
    # File to be encrypted
    filename = askopenfilename()
    # filename = 'test.png'
    file_type = os.path.splitext(filename)[1]
    # Open file and read as binary
    with open(filename, 'rb') as f:
        content = f.read()
    file_to_hex = binascii.hexlify(content)  # Convert entire file to hexadecimal
    # Show user file hex file conversion
    print("\n[START] Converted file to hexadecimal.")  # Decode byte string
    # Get first 64 bits of file
    first_64_bits = file_to_hex[:16] # Grab first 16 characters (8 characters = 4 bytes)
    # Show user first 64-bits of file
    print("\n[STEP 1] Collected first 64-bits of file :    ", first_64_bits.decode("utf-8"))
    # Split 64-bit segment into two 32-bit segments
    print("\n[STEP 2] Splitting 64-bits into two 32-bit segments...")
    split_64 = first_64_bits.decode("utf-8")
    splits = 8
    two_bytes = [split_64[i:i + splits] for i in range(0, len(split_64), splits)]
    print("\n[STEP 3] Split complete :     ", two_bytes)
    # Convert hex to base16 for simple arithmetic
    bytes_b16 = [int(x, 16) for x in two_bytes]
    print("\n[STEP 4] Converted hex to base 16 :    ", bytes_b16)
    # Create matrix of two bytes (32-bit)
    f64_matrix = np.matrix(bytes_b16)
    print("\n[STEP 5] Inserted base 16 values into matrix:     ", f64_matrix)


# Generate key matrix
def key_gen_f():
    global k
    # Generate Key Matrix
    k = np.random.randint(2, 10, f64_matrix.shape, dtype=np.int)
    print("\n[STEP 6] Generated key matrix : ", k)
    print("\nReady to start encryption!")


# Encryption function
def run_file_encryption():
    global encrypted, encrypted_file, encrypted_hex_a, encrypted_hex_b
    # encrypt
    print("\n[STEP 7] Encrypting base16 values with key...")
    encrypted = np.multiply(k, f64_matrix)
    print("\n[STEP 8] Encrypted base16 values: ", encrypted)
    base16_list = np.array(encrypted)[0].tolist()  # Convert matrix to array then list for base16 conversion.
    # Convert base16 back to hex
    print("\n[STEP 9] Converting encrypted base16 values to hexadecimal...")
    encrypted_hex_a, encrypted_hex_b = [hex(x)[2:].zfill(9) for x in base16_list]
    print("\n[STEP 10] New, encrypted 32-bit hexadecimal value :      ", encrypted_hex_a, encrypted_hex_b)
    removed = file_to_hex[16:]  # remove first 16 (64-bits) characters
    appended = [encrypted_hex_a + encrypted_hex_b + removed.decode("utf-8")]
    appended_to_string = appended
    appended_string = ''.join(str(e) for e in appended_to_string)  # Add encrypted bits to file
    print("\n[STEP 11] Added encrypted segments to file :     ")
    print("\n[STEP 12] Saving encrypted file...")
    # Save file as encryptedFile + file type
    with open('encryptedFile' + file_type, 'wb') as encrypted_file:
        encrypted_file.write(binascii.a2b_hex(appended_string.strip()))
        encrypted_file.close()


# Decryption function
def run_file_decryption():
    print("\nReady to start decryption!")
    # Decrypt
    print("\n[STEP 13] Decrypting file...")
    decrypt_segments = np.floor_divide(encrypted, k)
    print("[STEP 14] Decrypted initial 64-bits from hex", decrypt_segments)
    decrypted_base16_list = np.array(decrypt_segments)[0].tolist()  # Convert to list.
    # Convert base16 back to hex
    decrypted_hex_a, decrypted_hex_b = [hex(x)[2:].zfill(8) for x in decrypted_base16_list]  # split list into two variables
    print("\n[STEP 15] Converted encrypted base16 values to original hexadecimal :    ", decrypted_hex_a, decrypted_hex_b)
    removed_encrypted = file_to_hex[16:]  # Remove encrypted bits from file
    append_decrypted = [decrypted_hex_a + decrypted_hex_b + removed_encrypted.decode("utf-8")]
    decrypted_to_string = append_decrypted
    decrypted_string = ''.join(str(e) for e in decrypted_to_string)  # Add decrypted bits back to file
    print("[STEP 16] Added decrypted segments back to file.")
    print("[FINISHED] Saving decrypted file...")
    # Pythonic byte conversion
    decrypted_data = decrypted_string
    decrypted_data = decrypted_data.upper()
    decrypted_data = decrypted_data.strip()
    decrypted_data = decrypted_data.replace(' ', '')
    decrypted_data = decrypted_data.replace('\n', '')
    decrypted_data = binascii.a2b_hex(decrypted_data)
    # Save file (thanks to the byte conversion ;))
    with open('decryptedFile' + file_type, 'wb') as image_file:
        image_file.write(decrypted_data)


if __name__ == '__main__':
    open_file_handler()
    key_gen_f()
    run_file_encryption()
    run_file_decryption()

