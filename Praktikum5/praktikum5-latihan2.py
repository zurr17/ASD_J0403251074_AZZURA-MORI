# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# LATIHAN 2: Tracing Rekursi
# ==================================================
def countdown(n):
    if n == 0:
        print('Selesai')
        return
    print('Masuk: ', n) # dieksekusi sebelum rekursi
    countdown(n-1)
    print('Keluar: ', n) # dieksekusi setelah rekursi karena LIFO (last in first out)

countdown(3) # keluar terbalik karena call stack bekerja dengan konsep LIFO (last in first out)