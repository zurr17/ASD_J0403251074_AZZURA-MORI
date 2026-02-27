# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 3: Rekursi List
# ==================================================
def jumlah_list(data, index=0):
    if index == len(data): # base case: semua elemen yg sudah diproses
        return 0
    return data[index] + jumlah_list(data, index + 1) # elemen + sisa
print(jumlah_list([2, 4, 6, 8])) # output: 20