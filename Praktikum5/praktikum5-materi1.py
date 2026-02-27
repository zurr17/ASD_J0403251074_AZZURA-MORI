# ==================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ==================================================
# MATERI 1: Konsep Dasar Rekursif
# ==================================================

def faktorial(n):
    if n == 0: # base case: 0! = 1
        return 1
    return n * faktorial(n - 1) # recursive: n * (n-1)!
print(faktorial(5)) # output: 120