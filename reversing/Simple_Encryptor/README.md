# Reversing a Simple Encryptor

This challenge involves decrypting a flag that was encrypted using a custom encryption algorithm implemented in C. The provided encrypted file (`flag.enc`) contains the encrypted flag and is encrypted using a seed-based encryption algorithm.

## Solution Overview

To solve this challenge, I followed these steps:

1. **Understanding the Encryption Algorithm**: I first opened up the executable in Ghidra to analyze it and get the decmpiled C code to understand how the encryption algorithm works. The algorithm reads the contents of the `flag` file, encrypts them using a custom algorithm, and writes the encrypted data to a new file named `flag.enc`. The encryption process involves generating a random seed, using it to encrypt the data, and writing the seed along with the encrypted data to the output file.

2. **Decrypting the Flag**: ChatGPT wrote a C program to decrypt the `flag.enc` file and retrieve the original flag. The decryption process involved reading the seed and encrypted data from the file, initializing the random number generator with the seed, and performing the reverse operations of the encryption algorithm to decrypt the data.

3. **Debugging and Testing**: Debugging statements and comments were added to the decryption code to understand each step of the process and identify any potential issues. This helped ensure the correctness of the decryption process and allowed us to verify that the decrypted flag matched the original flag.

4. **Validation and Cleanup**: Finally, I validated the decrypted flag to ensure it was correct and matched the expected format.

## ChatGPT Explanation
"Explain the following main function:"

<img src= gpt_main_explained.PNG> 

"How do we go about decrypting the flag:"

<img src= gpt_reverse_code.PNG>


## Instructions

To decrypt the flag, follow these steps:

1. Compile the `simple_decryptor.c` program using a C compiler:
   ```bash
   gcc -o simple_decryptor simple_decryptor.c
2. Run the decryptor:
   ```bash
   ./simple_decryptor
