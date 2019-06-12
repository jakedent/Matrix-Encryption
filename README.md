# Matrix-Encryption

Requires: NumPy, BinAscii, tKinter. 

Run: python3 setup.py 

OR: pip3 install numpy && pip3 install binascii && pip3 install tkinter

Run: python3 main.py

This is a demonstration where encryption and decryption functions are called consecutively once the script has been run.

# Description of algorithm
Theoretical planning of the cipher arrived from technical analyses of existing ciphers and their algorithmic foundations. Certain technical aspects like, the symmetric structuring of Feistel Cipher, matrix operations in AES, the key generation and permutation functions of DES and the substitution characteristics of Hill Cipher have been integrated into the functionality of this cipher demonstration. 

The algorithms created to encrypt and decrypt both plaintext and files are fundamentally the same; a plaintext matrix is created based on input data, which is multiplied for encryption and divided for decryption against a key matrix. The key matrix is generated based on the shape of the plaintext matrix to be encrypted. Encryption and key permutation rounds have been implemented into the plaintext algorithm to incorporate Shannon’s confusion and diffusion theory. The file algorithm uses one round of encryption and decryption of the first 64 bits of a file, against the key matrix. Further work will focus on full file encryption using compression standards.

# How the algorithm currently works on files
Where the plaintext algorithm would normally take user input and store the alpha-numeric values of the input as a plaintext matrix; the file algorithm requests the user open a file, the file is then read as hexadecimal where the first 64-bits of the hexadecimal values are selected, these values are then placed into the plaintext matrix. The 64-bit hex values are converted to base 16 in order for arithmetic to be applied to them. The applied arithmetic is of course the multiplication and division as per the ciphers functions for encryption and decryption.

Once encryption has been applied, the encrypted base16 values are converted back into encrypted hexadecimal values and appended to the start of the file, in replace for the original bits. Decryption is the process of converting the encrypted hex values back to base 16 and dividing them against the key matrix to reveal the original base 16 values. These original base16 values are then converted back to the original hex values and appended to the start of the file, where the encrypted values are removed.

This was created in part with my BSc in Cyber Security and IT Forensics. A full paper explaining the mathematics of the algorithm is available here: https://jacobdent.com/blog
