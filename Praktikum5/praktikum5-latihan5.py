# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 5: Generator PIN
# ==================================================
def buat_pin (panjang, hasil=''):
    if len(hasil) == panjang: # base case: kelengkapan PIN
        print('PIN: ', hasil)
        return
    for angka in ['0','1','2']: # looping setiap angka menggunakan angka 0 - 2
        if angka in hasil: # kondisi jika angka berulang
            continue # skip angka yang sudah dipakai
        buat_pin(panjang, hasil + angka)
buat_pin(3) # output: 27 PIN (000 - 222) dengan total 3^3

