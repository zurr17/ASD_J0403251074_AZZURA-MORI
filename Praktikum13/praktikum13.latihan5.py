# Nama  : Azzura Mori
# NIM   : J0403251074
# Kelas : TPL A/P1
# Praktikum 13 - Graph III: Spanning Tree

edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

edges.sort()

def find(parent, node):
    while parent[node] != node:
        parent[node] = parent[parent[node]]
        node = parent[node]
    return node

def union(parent, a, b):
    parent[find(parent, a)] = find(parent, b)

nodes = set()
for w, u, v in edges:
    nodes.add(u)
    nodes.add(v)

parent = {node: node for node in nodes}

mst = []
total_bobot = 0
for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, u, v)
        mst.append((u, v, weight))
        total_bobot += weight

print("Minimum Spanning Tree (Jaringan Komputer):")
for u, v, w in mst:
    print(f"  {u} - {v} = {w}")
print("Total bobot minimum =", total_bobot)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# Jawab: Jaringan Komputer
# 2. Algoritma apa yang digunakan?
# Jawab: Kruskal
# 3. Edge mana saja yang dipilih dalam MST?
# Jawab: C-D (1), A-C (2), A-B (3)
# 4. Berapa total bobot MST?
# Jawab: 6
# 5. Mengapa edge tertentu tidak dipilih?
# Jawab: Karena akan membentuk cycle
