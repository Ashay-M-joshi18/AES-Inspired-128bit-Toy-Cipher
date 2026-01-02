from core import (
    rep, deb_bck, sub_bytes, shift_rows,
    getMixColumns, add_round_key,
    hex_to_matrix
)
from key_schedule import generate_round_key

# Input and Key in hex
input_hex = "3243f6a8885a308d313198a2e0370734"
key_hex = "2b7e151628aed2a6abf7158809cf4f3c"

print(f"Input: {input_hex}")
print(f"Master Key: {key_hex}")

# Convert to matrices
state = hex_to_matrix(input_hex)
key_matrix = hex_to_matrix(key_hex)

# Generate round keys
all_round_keys = generate_round_key(key_matrix)

# -------- PRE-ROUND --------
state = add_round_key(state, all_round_keys[0])
print(f"Round 0 (After pre-round AddRoundKey): {deb_bck(state, hex_output=True)}\n")

# -------- ROUNDS 1 TO 9 --------
for r in range(1, 10):
    print(f"--- Round {r} ---")
    
    # SubBytes
    state = sub_bytes(state, inverse=False)
    print(f"After SubBytes: {deb_bck(state, hex_output=True)}")
    
    # ShiftRows
    state = shift_rows(state)
    print(f"After ShiftRows: {deb_bck(state, hex_output=True)}")
    
    # MixColumns
    state = getMixColumns(state)
    print(f"After MixColumns: {deb_bck(state, hex_output=True)}")
    
    # AddRoundKey
    state = add_round_key(state, all_round_keys[r])
    print(f"After AddRoundKey {r}: {deb_bck(state, hex_output=True)}\n")

# -------- FINAL ROUND (ROUND 10) --------
print(f"--- Round 10 (Final Round) ---")
state = sub_bytes(state, inverse=False)
print(f"After SubBytes: {deb_bck(state, hex_output=True)}")

state = shift_rows(state)
print(f"After ShiftRows: {deb_bck(state, hex_output=True)}")

state = add_round_key(state, all_round_keys[10])
print(f"Final Ciphertext: {deb_bck(state, hex_output=True)}")