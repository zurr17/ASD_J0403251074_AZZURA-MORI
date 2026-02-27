# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 4: Backtracking Kombinasi Biner
# ==================================================
def biner(n, hasil=''):
    if len(hasil) == n: # base case: string dengan length n
        print(hasil)
        return
    biner(n, hasil + '0') # pilih 0
    biner(n, hasil + '1') # pilih 1