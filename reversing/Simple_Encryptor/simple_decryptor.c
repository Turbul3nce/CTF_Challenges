#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp = fopen("flag.enc", "rb");  // Open the encrypted file
    if (fp != NULL) {
        fseek(fp, 0, SEEK_END);  // Move the file pointer to the end of the file
        long size = ftell(fp);    // Get the size of the file
        rewind(fp);               // Move the file pointer back to the beginning

        char *fileContents = malloc(size);  // Allocate memory to store file contents
        if (fileContents != NULL) {
            fread(fileContents, sizeof(char), size, fp);  // Read file into memory

            // Print the hexadecimal representation of file contents
            printf("Encrypted data (hexadecimal):\n");
            for (int i = 0; i < size; i++) {
                printf("%02X", (unsigned char)fileContents[i]);
            }
            printf("\n\n");

            // Extract the seed (first 4 bytes) from file contents
            int seed;
            memcpy(&seed, fileContents, sizeof(seed));
            printf("Seed: %d\n", seed);

            srand(seed);  // Initialize random number generator with the seed
            int rand1, rand2;

            // Decrypt data starting from the 5th byte
            for (int i = 4; i < size; i++) {
                rand1 = rand();                // Generate first random number
                rand2 = rand() & 7;            // Generate second random number (0 to 7)

                printf("Current byte: %02X\n", fileContents[i]);
                printf("Right shift: %d\n", rand2);
                printf("XOR key: %d\n", rand1);

                // Perform right shift and XOR operations
                fileContents[i] = ((unsigned char)fileContents[i] >> rand2) | 
                                   ((fileContents[i]) << (8 - rand2));
                printf("Byte after rotate right: %02X\n", fileContents[i]);

                fileContents[i] = rand1 ^ fileContents[i];  // Perform XOR decryption
                printf("Byte after full decryption: %02X\n", fileContents[i]);
                getchar();  // Pause for debugging purposes
            }

            // Print the decrypted flag
            printf("\nDecrypted flag:\n");
            for (int i = 4; i < size; i++) {
                printf("%c", fileContents[i]);
            }
            printf("\n");

            free(fileContents);  // Free allocated memory
        }
        
        fclose(fp);  // Close the file
    }

    return 0;
}
