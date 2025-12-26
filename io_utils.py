def split_into_blocks(message, size=16):
    """
    Splits a message into blocks of given size.
    Pads the last block with spaces if needed.
    
    Args:
        message (str): Input string (plain text or hex).
        size (int): Block size (16 for encryption, 32 for hex blocks).
    
    Returns:
        list[str]: List of blocks of length `size`.
    """
    sarr = list(message)
    blocks = []

    for _ in range((len(message) + size - 1) // size):
        temp_str = ""
        for _ in range(size):
            if sarr:
                temp_str += sarr.pop(0)
        temp_str = temp_str.ljust(size)
        blocks.append(temp_str)

    return blocks

def get_user_choice():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        user_input = input("Enter 1 OR 2:   ")

        try:
            choice = int(user_input)
            if choice not in (1,2):
                raise ValueError
            return choice
        except ValueError:
            print("Please Enter Valid Input:    ")
            print("Please Enter The Integer 1 OR 2: ")


def get_plaintext():
    while True:
        try:
            message = input("Enter your Message: ")
            if not message.strip():
                raise ValueError("Message cannot be empty. Please enter a valid message.")
            return message
        except ValueError as e:
            print(e)

def get_ciphertext():
    while True:
        try:
            ciphertext = input("Enter your Ciphertext: ")
            if not ciphertext:
                raise ValueError("Ciphertext cannot be empty.")
            if len(ciphertext) % 32 != 0:
                raise ValueError("Ciphertext length must be a multiple of 32.")
            if not all(c in '0123456789abcdefABCDEF' for c in ciphertext):
                raise ValueError("Ciphertext must contain only hexadecimal characters (0-9, a-f, A-F).")
            return ciphertext
        except ValueError as e:
            print(e)

def get_master_key():
    while True:
        try:
            key = input("Enter your Masterkey: ")
            if len(key) != 16:
                raise ValueError("Master key must be exactly 16 characters.")
            return key
        except ValueError as e:
            print(e)

def print_encrypted(blocks):
    print("Encrypted Message:", blocks)

def print_decrypted(blocks):
    print("Decrypted Message:", blocks)
