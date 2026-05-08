# =====================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ASD PERTEMUAN 11
# =====================================================

def matrixToList(matrix): # fungsi mengubah matrix ke adjacency list
    adjList = {} # membuat dictionary kosong

    for i in range(len(matrix)): # loop setiap baris (node)
        adjList[i] = [] # membuat list kosong untuk node i
        for j in range(len(matrix[i])): # loop setiap kolom
            if matrix[i][j] == 1: # jika ada koneksi (nilai 1)
                adjList[i].append(j) # menambah j ke tetangga node i

    return adjList # mengembalikan adjacency list

if __name__ == "__main__": # main program
    matrix = [ # adjacency matrix
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    adjList = matrixToList(matrix) # mengubah matrix ke adjacency list

    print("Adjacency List Representation:") # judul
    for node in adjList: # loop setiap node
        print(f"{node}: {adjList[node]}") # menampilkan node dan tetangganya

