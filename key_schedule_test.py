from core import hex_to_matrix, deb_bck
from key_schedule import generate_round_key

# Initial key in hex: 2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c
key_hex = "2b7e151628aed2a6abf7158809cf4f3c"

# Convert to matrix
key_matrix = hex_to_matrix(key_hex)

# Generate all round keys
all_round_keys = generate_round_key(key_matrix)

# Print each round key in hex
for i, round_key in enumerate(all_round_keys):
    hex_output = deb_bck(round_key, hex_output=True)
    print(f"Round {i}: {hex_output}")