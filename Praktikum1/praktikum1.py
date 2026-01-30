# Konsep ADT dan File Handling
# LD1: Membaca seluruh isi file data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)
print(f"Tipe data: {type(isi_file)}")

# Membuka file per baris
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
    for baris in file:
        jumlah_baris += 1
        print(f"Baris ke-{jumlah_baris}")
        print(f"Isi baris: {baris}")

# LD2: Parsing data
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print(f"NIM: {nim} | Nama: {nama} | Nilai: {nilai}")

# LD3: Membaca data dan menyimpannya dalam struktur data list
data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_list.append([nim, nama, int(nilai)])

print(f"Contoh record ke-1: {data_list[0]}")
print(f"Contoh record ke-2: {data_list[1]}")
print(f"Jumlah record: {len(data_list)}")

# LD4: Membaca data dan menyimpannya ke struktur data dictionary
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        data_dict[nim] = {
            'nama': nama,
            'nilai': int(nilai)
        }

print(data_dict)