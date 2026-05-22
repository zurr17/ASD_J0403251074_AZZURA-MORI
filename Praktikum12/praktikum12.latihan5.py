# Nama  : Azzura Mori
# NIM   : J0403251074
# Kelas : TPL A/P1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari " + start_node + ":")
for kota, jarak in hasil.items():
    print(start_node, "->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Jawab: Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Jawab: Depok
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jawab: Bandung
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Jawab: Algoritma memulai dari Bogor dan selalu memilih kota tetangga terdekat, Depok. Di situ, ia menemukan bahwa ke Jakarta lebih cepat lewat Depok, dan ke Bandung paling cepat rutenya Bogor > Depok > Bandung