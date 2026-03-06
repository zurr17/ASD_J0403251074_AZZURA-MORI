skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

def selectionsort(data):
    for fillslot in range(len(data)-1, 0, -1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if data[location] > data[maxpos]:
                maxpos = location
        temp = data[fillslot]
        data[fillslot] = data[maxpos]
        data[maxpos] = temp

selectionsort(skor)
skor = skor[::-1]

print("5 Skor Tertinggi:", skor[:5])
print("Kandidat yang lolos:")
for i in range(5):
    print(f"  Peringkat {i+1}: Skor {skor[i]}")