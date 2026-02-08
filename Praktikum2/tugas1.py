# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Azzura Mori
# NIM  : J0403251074
# Kelas: A/P1
# ==========================================================

nama_file = "stok_barang.txt"

def baca_stok(nama_file):
    stok_dict = {}
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                baris = baris.strip()
                if baris:
                    kode, nama, stok = baris.split(",")
                    stok_dict[kode] = {"nama": nama, "stok": int(stok)}
    return stok_dict

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as f:
        for kode, data in stok_dict.items():
            f.write(f"{kode},{data['nama']},{data['stok']}\n")

def tampilkan_semua(stok_dict):
    if not stok_dict:
        print("Stok kosong.")
        return
    print(f"{'Kode':<10}{'Nama':<20}{'Stok':<10}")
    print("-" * 40)
    for kode, data in stok_dict.items():
        print(f"{kode:<10}{data['nama']:<20}{data['stok']:<10}")

def cari_barang(stok_dict):
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict:
        data = stok_dict[kode]
        print(f"Kode: {kode}, Nama: {data['nama']}, Stok: {data['stok']}")
    else:
        print("Barang tidak ditemukan.")

def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    nama = input("Masukkan nama barang: ").strip()
    stok_awal = int(input("Masukkan stok awal: "))
    stok_dict[kode] = {"nama": nama, "stok": stok_awal}
    print("Barang berhasil ditambahkan.")

def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih (1/2): ").strip()
    jumlah = int(input("Masukkan jumlah: "))
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambah.")
    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Error: Stok tidak boleh negatif.")
        else:
            stok_dict[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")

def main():
    stok_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":

    main()
