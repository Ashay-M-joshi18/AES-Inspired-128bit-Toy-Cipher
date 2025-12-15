from core import shift_col

# ---------- KEY ----------

def generate_round_key(round_key):
    all_round_key=[]
    for i in range(10):
        if i==0:
            all_round_key.append(round_key)
        else:
            copy_key = [row[:] for row in all_round_key[i-1]]
            diffused_key=shift_rows(copy_key)
            
            diffused_key=shift_col(diffused_key)
            diffused_key=sub_bytes(diffused_key,inverse =False)
            temp_round_key=[]
            for j in range(4):
                temp_row=[]
                for k in range(4):
                    temp_row.append(diffused_key[j][k]^all_round_key[i-1][j][k])
                temp_round_key.append(temp_row)
            all_round_key.append(temp_round_key)
    return all_round_key