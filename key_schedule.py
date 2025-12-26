from core import form_words, sub_bytes , rotate, Add_Rcon , sbox

# ---------- KEY ----------

def generate_round_key(initial_key):
    all_round_keys = []
    all_round_keys.append(initial_key)

    for r in range(10):
        prev_key = all_round_keys[r]
        words = []

        # ---- w0 ----
        temp = form_words(prev_key, 3)      # w3
        temp = rotate(temp, 1)              # RotWord
        for i in range(4):
            temp[i] = sbox[temp[i]]# SubWord
        Add_Rcon(temp, r)                   # Rcon
        w0 = [temp[i] ^ prev_key[i][0] for i in range(4)]
        words.append(w0)

        # ---- w1, w2, w3 ----
        for j in range(1, 4):
            prev_word = form_words(prev_key, j)
            new_word = [prev_word[i] ^ words[j-1][i] for i in range(4)]
            words.append(new_word)

        # ---- convert words → round key matrix ----
        round_key = [[words[c][r_] for c in range(4)] for r_ in range(4)]
        all_round_keys.append(round_key)

    return all_round_keys
