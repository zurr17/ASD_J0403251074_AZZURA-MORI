# PRAKTIKUM 2
#L1: Baca data dari file data_mahasiswa.txt
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding ="utf-8") as file:
        for eachLine in file:
            baris = eachLine.strip()
            nim, nama, nilai = baris.split(",")
            # simpan data ke dict
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict

#L2: Menampilkan data
def tampilkan_data(data_dict):
    print("\n === DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'NAMA' : <12} | {'NILAI' : >5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")


#L3: Membuat fungsi nyari data
def cari_data(data_dict):
    nim_Input = input("Masukkan NIM yang mau dicari: ").strip().title()
    if nim_Input in data_dict:
        nama = data_dict[nim_Input]['nama']
        nilai = data_dict[nim_Input]['nilai']
        print("Data ditemukan!")
        print(f"NIM: {nim_Input}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data tidak ditemukan!")


#L4: Membuat fungsi update data
def ubah_data(data_dict):
    buka_data = baca_data(nama_file)
    nim_input = input("Masukkan NIM yang mau diubah: ").strip().title()

    if nim_input not in data_dict:
        print("Data tidak ditemukan!")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Input tidak valid! harus angka")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Input tidak valid! nilai harus antara 0 dan 100")
        return

    nilai_lama = data_dict[nim_input]["nilai"]
    data_dict[nim_input]["nilai"] = nilai_baru
    print(f"update bisa, nilai lama {nilai_lama} jadi {nilai_baru}")
    tampilkan_data(buka_data)
    

def simpan_data(data_dict, nama_file):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")
    print("Data berhasil disimpan ke file!")


def main():
    buka_data = baca_data(nama_file)
    
    while True:
        print("\n === MENU ===")
        print("1. Tampilkan Data")
        print("2. Cari Data")
        print("3. Ubah Data")
        print("4. Simpan Data")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ").strip()
        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(buka_data, nama_file)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()