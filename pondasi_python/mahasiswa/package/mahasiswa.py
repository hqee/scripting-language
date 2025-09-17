ma = {}

def menu():
    print("1. Tambah Mahasiswa")
    print("2. cari identitas Mahasiswa")
    print("3. Daftar Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. keluar Program")

    menu = int(input("Pilih Menu : "))

    if menu == 1: 
        tambahMA()
    elif menu == 2:
        cariMA()
    elif menu == 3:
        daftarMA()
    elif menu == 4:
        hapusMA()
    elif menu == 5:
        return False
    else :
        print("input salah, coba lagi")
        menu()

def tambahMA():
    nama = str(input("Nama MA : "))
    nim = int(input("NIM MA : "))
    jurusan = str(input("jurusan MA : "))

    if nim in ma:
        print("data sudah ada")
        menu() 
    else : 
        ma[nim] = {"nama" : nama, "jurusan" : jurusan}
        print(f"{nama} Berhasil ditambah")

    menu()

def cariMA():
    cari = str(input("Masukkan NIM MA yang dicari : "))

    if cari in ma:
        data = ma["nim"]  
        print(f"data ditemukan -> Nama : {data['nama']}, Jurusan : {data['jurusan']}")
    
    else:
        print("data tidak ditemukan")
    
    menu()

def daftarMA():
    for key in ma.keys():
        print(key, " -> ", ma[key])
    else:
        print("Daftar Mahasiswa kosong")
    menu()

def hapusMA():
    for key in ma.keys():
        print(key, " -> ", ma[key])
    
    hapus = int(input("Pilih Nim yang mau dihapus : "))

    if hapus in ma:
        del ma[hapus]
    else:
        print("Daftar mahasiswa kosong")
    menu()




    
