# Nama  : Azzura Mori
# NIM   : J0403251074
# Kelas : TPL A/P1
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
    
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# Jawab: Graph awal memiliki semua edge (5), sedangkan spanning tree hanya memiliki subset edge (3) yang tetap menghubungkan semua node.
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Jawab: Karena syarat tree adalah graf terhubung yang tidak memiliki cycle
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jawab: Karena spanning tree dengan n node selalu memiliki tepat n-1 edge sedangkan graph awal bisa memiliki lebih banyak edge