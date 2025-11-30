# Program Data Nilai Mahasiswa

mahasiswa = {}


# ------------------------------
# FUNGSI TAMBAH DATA
# ------------------------------
def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

    mahasiswa[nama] = {
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Akhir": akhir
    }
    print(f"Data mahasiswa '{nama}' berhasil ditambahkan!\n")


# ------------------------------
# FUNGSI TAMPILKAN DATA
# ------------------------------
def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not mahasiswa:
        print("Data masih kosong!\n")
        return

    print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"
    ))

    for nama, data in mahasiswa.items():
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:.2f}".format(
            nama, data["NIM"], data["Tugas"], data["UTS"], data["UAS"], data["Akhir"]
        ))
    print()


# ------------------------------
# FUNGSI HAPUS DATA
# ------------------------------
def hapus(nama):
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan!\n")


# ------------------------------
# FUNGSI UBAH DATA
# ------------------------------
def ubah(nama):
    if nama in mahasiswa:
        print(f"\n=== Ubah Data Mahasiswa: {nama} ===")
        nim = input("NIM baru         : ")
        tugas = float(input("Nilai Tugas baru : "))
        uts = float(input("Nilai UTS baru   : "))
        uas = float(input("Nilai UAS baru   : "))

        akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

        mahasiswa[nama] = {
            "NIM": nim,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Akhir": akhir
        }
        print("Data berhasil diubah!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan!\n")


# ------------------------------
# MENU UTAMA
# ------------------------------
while True:
    print("=== MENU PROGRAM DATA MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Nama yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Nama yang akan diubah : ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!\n")
