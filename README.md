The code provided is a Python script that implements a simple Caesar cipher for encrypting and decrypting messages. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Here’s a detailed explanation of each part of the code:

Caesar Cipher Functions
1. `caesar_cipher_encrypt(text, shift)`:
    - This function takes a string `text` and an integer `shift` as input.
    - It initializes an empty list `encrypted_text` to store the encrypted characters.
    - It iterates through each character in `text`.
    - If the character is a letter (`char.isalpha()`), it shifts the character by the `shift` value:
        - For lowercase letters, it checks if the shifted character goes beyond 'z' or before 'a' and adjusts accordingly.
        - For uppercase letters, it checks if the shifted character goes beyond 'Z' or before 'A' and adjusts accordingly.
    - Non-alphabetic characters are appended to `encrypted_text` without change.
    - The function returns the encrypted message as a single string by joining the list `encrypted_text`.

2. `caesar_cipher_decrypt(text, shift)`:
    - This function decrypts a message by calling the `caesar_cipher_encrypt` function with the `shift` value negated (`-shift`). 
    - This effectively reverses the encryption.

User Interaction Functions
1. `encrypt_message()`:
    - This function prompts the user to input a message to encrypt and the shift value.
    - It calls `caesar_cipher_encrypt` with these inputs and prints the encrypted message.

2. `decrypt_message()`:
    - This function prompts the user to input a message to decrypt and the shift value.
    - It calls `caesar_cipher_decrypt` with these inputs and prints the decrypted message.

Main Menu Function
1. `main()`:
    - This function provides a menu for the user to choose between encrypting a message, decrypting a message, or exiting the program.
    - It runs in a loop until the user chooses to exit (option '3').
    - It calls the appropriate function based on the user’s choice and handles invalid input by prompting the user to select a valid option.

Program Entry Point
- The `if __name__ == "__main__": main()` block ensures that the `main` function is called when the script is executed directly. This starts the program and presents the user with the menu.

Overall, this script is a user-interactive program that allows users to encrypt and decrypt messages using the Caesar cipher, providing a simple interface to input messages and shift values and to see the results of the encryption or decryption.
