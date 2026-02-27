# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# LATIHAN 1: Rekursi Dasar
# ==================================================
def pangkat(a, n):
    if n == 0: # base case: a^0 = 1
        return 1
    return a * pangkat(a, n-1) # recursive case: a * a^(n-1)
print(pangkat(2,4)) # contoh: 2 pangkat 4. 2*2*2*2. output: 16