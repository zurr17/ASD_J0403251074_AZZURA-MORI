# =====================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ASD PERTEMUAN 11
# =====================================================


nodes = ["Router", "Server", "PC1", "PC2", "Laptop", "Printer"] # 6 node perangkat jaringan
edges = [("Router", "Server"), ("Router", "PC1"), ("Router", "PC2"), ("Router", "Laptop"), ("Server", "PC1"), ("PC2", "Printer"), ("Laptop", "Printer")] # 7 edge

# membuat adjacency list
adjList = {} # membuat dictionary kosong
for node in nodes: # loop setiap node
    adjList[node] = [] # membuat list kosong untuk setiap node

for u, v in edges: # loop setiap edge
    adjList[u].append(v) # menambah v ke tetangga u
    adjList[v].append(u) # menambah u ke tetangga v (undirected) yang di-swap

# membuat adjacency matrix
n = len(nodes) # jumlah node
index = {node: i for i, node in enumerate(nodes)} # mapping nama node ke indeks
matrix = [[0] * n for _ in range(n)] # membuat matrix n x n berisi 0

for u, v in edges: # loop setiap edge
    i, j = index[u], index[v] # mengambil indeks kedua node
    matrix[i][j] = 1 # menandai koneksi u ke v
    matrix[j][i] = 1 # menandai koneksi v ke u (undirected)


# menampilkan adjacency list
print("\nAdjacency List")
for node in nodes: # loop setiap node
    print(f"{node}: {adjList[node]}") # menampilkan node dan tetangganya

# menampilkan adjacency matrix
print("\nAdjacency Matrix")
for i in range(n): # loop setiap baris
    for j in range(n): # loop setiap kolom
        print(matrix[i][j], end=" ") # menampilkan nilai matrix
    print() # pindah baris baru

# menampilkan daftar node
print("Nama Node")
for i, node in enumerate(nodes): # loop setiap node
    print(f"{i}. {node}") # menampilkan indeks dan nama node

# menampilkan hubungan antar node
print("\nHubungan Antar Node")
for i, (u, v) in enumerate(edges, 1): # loop setiap edge
    print(f"{i}. {u} <-> {v}") # menampilkan koneksi antar node

