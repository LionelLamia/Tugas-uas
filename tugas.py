import json

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan penulis: ")
    tahun_terbit = int(input("Masukkan tahun terbit: "))
    kategori = input("Masukkan kategori: ")
    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun_terbit,
        "kategori": kategori,
        "tersedia": True
    }
    daftar_buku.append(buku_baru)
    simpan_data()
    print("Buku berhasil ditambahkan")

def hapus_buku():
    judul = input("judul buku yang dihapus: ")
    for i, buku in enumerate(daftar_buku):
        if buku["judul"] == judul:
            del daftar_buku[i]
            simpan_data()
            print("Buku berhasil dihapus")
            return
    print("buku berhasil dihapus.")

def cari_buku():
    kata_kunci = input("Masukkan kata kunci pencarian: ")
    hasil_pencarian = []
    for buku in daftar_buku:
        if kata_kunci.lower() in buku["judul"].lower() or \
           kata_kunci.lower() in buku["penulis"].lower() or \
           kata_kunci.lower() in buku["kategori"].lower():
            hasil_pencarian.append(buku)
    if hasil_pencarian:
        print("Hasil pencarian:")
        for buku in hasil_pencarian:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun Terbit: {buku['tahun_terbit']}, Kategori: {buku['kategori']}")
    else:
        print("Buku tidak ditemukan.")

def pinjam_buku():
    judul = input("Masukkan judul buku yang ingin dipinjam: ")
    for buku in daftar_buku:
        if buku["judul"] == judul and buku["tersedia"]:
            buku["tersedia"] = True
            return
    print("Buku dipinjam.")

def kembalikan_buku():
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
    for buku in daftar_buku:
        if buku["judul"] == judul:
            buku["tersedia"] = True
            return
    print("Buku dikembalikan.")

def tampilkan_buku_dipinjam():
    buku_dipinjam = [buku for buku in daftar_buku if not buku]
    if buku_dipinjam:
        print("Daftar buku yang dipinjam:")
        for buku in buku_dipinjam:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}")
    else:
        print("Tidak ada buku yang dipinjam.")

def simpan_data():
    with open("perpustakaan.json", "w") as file:
        json.dump(daftar_buku, file, indent=4)

def muat_data():
    global daftar_buku
    try:
        with open("perpustakaan.json", "r") as file:
            daftar_buku = json.load(file)
    except FileNotFoundError:
        daftar_buku = []

daftar_buku = []
muat_data()

def tampilkan_menu():
    print("tampilan menu")
    print("Pilih opsi:")
    print("1.Tambah buku")
    print("2.Hapus buku")
    print("3.Cari buku")
    print("4.Pinjam buku")
    print("5.Kembalikan buku")
    print("6.Tampilkan buku yang dipinjam")
    print("7.keluar")


while True:
    tampilkan_menu()
    pilihan = int(input("Masukkan pilihan: "))
    if pilihan == 1:
        tambah_buku()
    elif pilihan == 2:
        hapus_buku()
    elif pilihan == 3:
        cari_buku()
    elif pilihan == 4:
        pinjam_buku()
    elif pilihan == 5:
        kembalikan_buku()
    elif pilihan == 6:
        tampilkan_buku_dipinjam()
    elif pilihan == 7:
        break
    else:
        print("Pilihan tidak valid.")