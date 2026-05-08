# =====================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ASD PERTEMUAN 11
# =====================================================

def createGraph(V, edges): # func utk  membuat graph
    mat = [[0 for _ in range(V)] for _ in range(V)] # membuat matriks VxV yg berisi 0

    for it in edges: # loop setiap edge
        u = it[0] # vertex pertama
        v = it[1] # vertex kedua
        mat[u][v] = 1 # koneksi u ke v

        mat[v][u] = 1 # koneksi v ke u (undirected) yg di-swap
    return mat # kembalikan matriks

if __name__ == "__main__": # main program
    V = 4 # jumlah vertex (0, 1, 2, 3)

    edges = [[0, 1], [0, 2], [1, 2], [2, 3]] # daftar edge

    mat = createGraph(V, edges) # graph dr vertex & edge

    print("Adjacency Matrix Representation:") # judul
    for i in range(V): # loop baris
        for j in range(V): # loop kolom
            print(mat[i][j], end=" ") # nilai matriks
        print() # pindah baris
