```markdown
# Caesar Cipher Encryption and Decryption Tool

This is a simple Python program that allows users to encrypt and decrypt messages using the Caesar cipher technique. The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt messages by shifting characters by a specified number of positions.
- Decrypt messages by reversing the shift.
- Simple user interface through the command line.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

```sh
git clone https://github.com/metaphor11/caesar-cipher-tool.git
cd caesar-cipher-tool
```

2. Run the script:

```sh
python caesar_cipher.py
```

3. Follow the on-screen instructions:

- To encrypt a message, select option `1`:
  - Enter the message you want to encrypt.
  - Enter the shift value (a positive integer).
  - The encrypted message will be displayed.

- To decrypt a message, select option `2`:
  - Enter the message you want to decrypt.
  - Enter the shift value (a positive integer).
  - The decrypted message will be displayed.

- To exit the program, select option `3`.

## Example

Encrypt a message:

```sh
Enter the message you want to encrypt: Hello, World!
Enter the shift value (positive integer): 3
Encrypted Message: Khoor, Zruog!
```

Decrypt a message:

```sh
Enter the message you want to decrypt: Khoor, Zruog!
Enter the shift value (positive integer): 3
Decrypted Message: Hello, World!
```

## Code Explanation

### `caesar_cipher_encrypt(text, shift)`

This function encrypts the input text by shifting each alphabetic character by the specified shift value. Non-alphabetic characters remain unchanged.

### `caesar_cipher_decrypt(text, shift)`

This function decrypts the input text by calling `caesar_cipher_encrypt` with the negative of the shift value, effectively reversing the encryption.

### `encrypt_message()`

Prompts the user to input a message and a shift value, then displays the encrypted message.

### `decrypt_message()`

Prompts the user to input a message and a shift value, then displays the decrypted message.

### `main()`

Provides a menu for the user to choose between encrypting a message, decrypting a message, or exiting the program.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
