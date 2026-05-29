# Nama  : Azzura Mori
# NIM   : J0403251074
# Kelas : TPL A/P1
# Praktikum 13 - Graph III: Spanning Tree

edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

edges.sort()

def find(parent, node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    parent[rootA] = rootB

nodes = set()
for w, u, v in edges:
    nodes.add(u)
    nodes.add(v)

parent = {node: node for node in nodes}


mst = []
total_biaya = 0
for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        mst.append((u, v, weight))
        total_biaya += weight

print("Jaringan kabel dengan biaya minimum (MST):")
for u, v, w in mst:
    print(f"  {u} - {v} = {w}")
print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# Jawab: Kruskal
# 2. Edge mana saja yang dipilih?
# Jawab: C-D (1), A-C (2), B-D (3)
# 3. Berapa total biaya minimum?
# Jawab: 6
# 4. Mengapa MST cocok digunakan pada kasus ini?
# Jawab: Karena MST menghubungkan semua gedung dengan total biaya paling minimum