from ecb import encrypt_ecb, decrypt_ecb
from io_utils import get_user_choice, get_message, get_key, print_result


def main():
    print("=== AES (Educational Implementation) ===\n")

    choice = get_user_choice()

    if choice == 1:
        message = get_message("Enter your message: ")
        key = get_key("Enter your master key (16 chars): ")
        cipher_blocks = encrypt_ecb(message, key)
        print_result("Encrypted Message", cipher_blocks)

    elif choice == 2:
        cipher_text = get_message("Enter your ciphertext (hex): ")
        key = get_key("Enter your master key (16 chars): ")
        plain_blocks = decrypt_ecb(cipher_text, key)
        print_result("Decrypted Message", plain_blocks)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()