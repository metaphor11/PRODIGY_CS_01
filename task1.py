def caesar_cipher_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text.append(chr(shifted))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decrypt by shifting in the opposite direction

def encrypt_message():
    text = input("Enter the message you want to encrypt: ")
    shift = int(input("Enter the shift value (positive integer): "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted Message:", encrypted_text)

def decrypt_message():
    text = input("Enter the message you want to decrypt: ")
    shift = int(input("Enter the shift value (positive integer): "))
    decrypted_text = caesar_cipher_decrypt(text, shift)
    print("Decrypted Message:", decrypted_text)

def main():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Select an option (1, 2, or 3): ")

        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
