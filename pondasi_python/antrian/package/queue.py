queue = []

def menu():
    print("==== Menu ====")
    print("1. Tambah Antrian")
    print("2. Panggil Antrian")
    print("3. Lihat Antrian")
    print("4. Selesai")

    menu = int(input("masukkan input menu (1-4) : "))

    if menu == 1:
        tambahAntrian()
    elif menu == 2:
        panggilAntrian()
    elif menu == 3:
        lihatAntrian()
    elif menu == 4:
        print("Terimakasih telah menggunakan layanan kami")
        return False
    else:
        print("input salah, coba lagi")
        menu()
        
def tambahAntrian():
    nama = str(input("Masukkan Nama : "))
    queue.append(nama)
    print(f"{nama} berhasil ditambahkan\n\n")
    menu()

def panggilAntrian():
    nama = queue[0]
    queue.pop(0)
    
    print(f"{nama} dipanggil")
    menu()

def lihatAntrian():
    for i in range(len(queue)):
        print(f"{i+1}. {queue[i]}")
    menu()
