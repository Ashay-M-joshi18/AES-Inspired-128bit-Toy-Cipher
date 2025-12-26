from ecb import encrypt_ecb, decrypt_ecb
from io_utils import get_user_choice, get_plaintext, get_master_key, print_encrypted , get_ciphertext , print_decrypted


def main():
    print("=== AES (Educational Implementation) ===\n")

    choice = get_user_choice()


    if choice == 1:
        message = get_plaintext()
        key = get_master_key()
        cipher_blocks = encrypt_ecb(message, key)
        print_encrypted(cipher_blocks)

    elif choice == 2:
        cipher_text = get_ciphertext()
        key = get_master_key()
        plain_blocks = decrypt_ecb(cipher_text, key)
        print_decrypted(plain_blocks)

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
