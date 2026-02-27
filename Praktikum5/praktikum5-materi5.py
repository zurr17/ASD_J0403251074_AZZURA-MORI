# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 5: Backtracking dengan Pruning
# ==================================================
def biner_batas(n, batas, hasil='', jumlah_1=0):
    if jumlah_1 > batas: # pruning: menghilangkan cabang yg melanggar syarat batas
        return
    if len(hasil) == n: # base case: print jika sudah length n
        print(hasil)
        return
    biner_batas(n, batas, hasil + '0', jumlah_1) # pilih 0
    biner_batas(n, batas, hasil + '1', jumlah_1 + 1) # pilih 1 dan tambah counter
biner_batas(4, 2) # 4 digit dengan maksa dua angka 1