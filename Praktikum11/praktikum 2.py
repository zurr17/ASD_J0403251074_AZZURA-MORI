# =====================================================
# AZZURA MORI
# J0403251074
# TPL A/P1
# ASD PERTEMUAN 11
# =====================================================

def createGraph(edges): # fungsi untuk membuat graph
    graph = {} # membuat dictionary kosong untuk adjacency list

    for it in edges: # loop setiap edge
        u = it[0] # mengambil node pertama
        v = it[1] # mengambil node kedua

        if u not in graph: # jika node u belum ada di dictionary
            graph[u] = [] # membuat list kosong untuk u
        if v not in graph: # jika node v belum ada di dictionary
            graph[v] = [] # membuat list kosong untuk v

        graph[u].append(v) # menambah v ke tetangga u
        graph[v].append(u) # menambah u ke tetangga v (undirected)

    return graph # mengembalikan dictionary graph

if __name__ == "__main__": # main program
    edges = [["A", "B"], ["A", "C"], ["B", "D"], ["D", "C"]] # daftar edge

    graph = createGraph(edges) # membuat graph dari edge

    print("Adjacency List Representation:") # judul
    for node in sorted(graph): # loop setiap node (urut abjad)
        print(f"{node}: {graph[node]}") # menampilkan node dan tetangganya
