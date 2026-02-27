# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# LATIHAN 4: Konsep Dasar Rekursif
# ==================================================
def kombinasi(n, hasil=''):
    if len(hasil) == n: # base case: kondisi jika length hasil sama dengan n
        print(hasil)
        return
    kombinasi(n, hasil + 'A') # cabang A
    kombinasi(n, hasil + 'B') # cabang B
kombinasi(2) # output: AA, AB, BA, BB
# jumlah kombinasi = 2^n, yakni setiap posisi memiliki 2 pilihan