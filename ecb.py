from core import (
    rep, deb_bck, sub_bytes, shift_rows,
    getMixColumns, add_round_key,
    inv_shift_rows, inv_mix_columns,
    hex_to_matrix
)

from key_schedule import generate_round_key
from io_utils import split_into_blocks


def encrypt_ecb(message, master_key):
    blocks = split_into_blocks(message, size=16)

    round_key = rep(master_key)
    all_round_keys = generate_round_key(round_key)

    encrypted_blocks = []

    for block in blocks:
        state = rep(block)

        for r in range(10):
            state = sub_bytes(state, inverse=False)
            state = shift_rows(state)
            state = getMixColumns(state)
            state = add_round_key(state, all_round_keys[r])

        encrypted_blocks.append(deb_bck(state, hex_output=True))

    return encrypted_blocks
    
    
    def decrypt_ecb(ciphertext, master_key):
    blocks = split_into_blocks(ciphertext, size=32)

    round_key = rep(master_key)
    all_round_keys = generate_round_key(round_key)

    decrypted_blocks = []

    for block in blocks:
        state = hex_to_matrix(block)

        for r in range(10):
            state = add_round_key(state, all_round_keys[9 - r])
            state = inv_mix_columns(state)
            state = inv_shift_rows(state)
            state = sub_bytes(state, inverse=True)

        decrypted_blocks.append(deb_bck(state, hex_output=False))

    return decrypted_blocks