from core import (
    rep, deb_bck, sub_bytes, shift_rows,
    getMixColumns, add_round_key,
    inv_shift_rows, inv_mix_columns,
    hex_to_matrix
)

from key_schedule import generate_round_key
from io_utils import split_into_blocks


def encrypt_ecb(message, master_key):
    if not isinstance(message, str) or not message:
        raise ValueError("Message must be a non-empty string")
    # Split plaintext into 16-byte blocks
    blocks = split_into_blocks(message, size=16)

    # Generate round keys (11 keys: K0 to K10)
    round_key_matrix = rep(master_key)
    all_round_keys = generate_round_key(round_key_matrix)

    encrypted_blocks = []

    for block in blocks:
        # Initial state
        state = rep(block)

        # -------- PRE-ROUND --------
        state = add_round_key(state, all_round_keys[0])

        # -------- ROUNDS 1 to 9 --------
        for r in range(1, 10):
            state = sub_bytes(state, inverse=False)
            state = shift_rows(state)
            state = getMixColumns(state)
            state = add_round_key(state, all_round_keys[r])

        # -------- FINAL ROUND (NO MIXCOLUMNS) --------
        state = sub_bytes(state, inverse=False)
        state = shift_rows(state)
        state = add_round_key(state, all_round_keys[10])

        # Convert state to hex string
        encrypted_blocks.append(deb_bck(state, hex_output=True))

    # ECB returns concatenated ciphertext
    return "".join(encrypted_blocks)


def decrypt_ecb(ciphertext, master_key):
    if not isinstance(ciphertext, str) or not ciphertext:
        raise ValueError("Ciphertext must be a non-empty string")
    if len(ciphertext) % 32 != 0:
        raise ValueError("Ciphertext length must be a multiple of 32")
    if not all(c in '0123456789abcdefABCDEF' for c in ciphertext):
        raise ValueError("Ciphertext must contain only hexadecimal characters")
    blocks = split_into_blocks(ciphertext, size=32)

    round_key_matrix = rep(master_key)
    all_round_keys = generate_round_key(round_key_matrix)

    decrypted_blocks = []

    for block in blocks:
        state = hex_to_matrix(block)

        # -------- INVERSE FINAL ROUND --------
        state = add_round_key(state, all_round_keys[10])
        state = inv_shift_rows(state)
        state = sub_bytes(state, inverse=True)

        # -------- INVERSE ROUNDS 9 → 1 --------
        for r in range(9, 0, -1):
            state = add_round_key(state, all_round_keys[r])
            state = inv_mix_columns(state)
            state = inv_shift_rows(state)
            state = sub_bytes(state, inverse=True)

        # -------- INVERSE PRE-ROUND --------
        state = add_round_key(state, all_round_keys[0])

        decrypted_blocks.append(deb_bck(state, hex_output=False))

    # Remove padding / trailing spaces
    return "".join(decrypted_blocks).rstrip()
