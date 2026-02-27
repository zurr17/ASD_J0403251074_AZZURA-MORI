# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 2: Tracing Call Stack
# ==================================================
def hitung(n):
    if n == 0:
        print('Selesai')
        return
    print('Masuk: ', n) # false stacking (turun)
    hitung(n - 1)
    print('Keluar: ', n) # false unwinding (naik balik)
hitung(3)