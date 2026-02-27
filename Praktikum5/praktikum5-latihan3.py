# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# LATIHAN 3: Konsep Dasar Rekursif
# ==================================================
def cari_maks(data, index=0):
    if index == len(data) - 1: # base case: mencari kondisi elemen terakhir
        return data[index]
    maks_sisa = cari_maks(data, index + 1) # mencari maks dari sisa list
    if data[index] > maks_sisa: # mencari kondisi perbandinan elemen data dengan maks sisa
        return data[index]
    else:
        return maks_sisa
angka = [3, 7, 2, 9, 5]
print('Nilai maks: ', cari_maks(angka))
# base = 5, 9 > 5 = 9, 2 < 9 = 9, 7 < 9 = 9, 3 < 9 = 9