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


def get_plaintext():
    return input("Enter your Message: ")

def get_ciphertext():
    return input("Enter your Ciphertext: ")

def get_master_key():
    return input("Enter your Masterkey: ")

def print_encrypted(blocks):
    print("Encrypted Message:", *blocks)

def print_decrypted(blocks):
    print("Decrypted Message:", *blocks)
