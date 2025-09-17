cart = []
harga = 0

def menu ():
    print("\n\n====== Cashier alat tulis ======")
    print("1. Tambah Barang")
    print("2. Kurang Barang")
    print("3. Lihat Keranjang")
    print("4. Total Harga")
    print("5. Keluar")

    menu = int(input("Pilih Menu (1-5) : "))

    if menu == 1:
        tambahBarang()
    elif menu == 2:
        kurangBarang()
    elif menu == 3:
        keranjang()
    elif menu == 4:
        totalHarga()
    elif menu == 5:
        return False
    else:
        print("inputan salah, coba lagi")

    return True

def tambahBarang():
    global harga 
    print("\n\n====Pilih barang====")
    print("1. buku")
    print("2. tipe-x")
    print("3. bolpen")
    print("4. penggaris")
    print("5. keluar")

    pilihBarang = int(input("Pilih barang (1-4): "))

    if pilihBarang == 1:
        cart.append("buku")
        harga += 5000
        tambahBarang()
    elif pilihBarang == 2:
        cart.append("tipe-x")
        harga += 2500
        tambahBarang()
    elif pilihBarang == 3:
        cart.append("bolpen")
        harga += 3000
        tambahBarang()
    elif pilihBarang == 4:
        cart.append("penggaris")
        harga += 4000
        tambahBarang()
    elif pilihBarang == 5:
        menu()
    else:
        print("masukan salah, coba lagi")
        tambahBarang()

def keranjang ():
    if not cart:
        print("\n\nkeranjang kosong")
    else:
        for i in range (len(cart)):
            print(f"{i+1}. {cart[i]}")

def totalHarga():
    print(f"\n\nTotal harga : Rp. {harga}")
    
def kurangBarang():
    keranjang()
    global harga
    
    hapus = int(input("pilih barang yang mau dihapus (urutan barang) : ")) - 1

    if hapus != 0 or hapus < len(cart):
        item = cart.pop(hapus)

        if item == "buku":
            harga -= 5000
        elif item == "tipe-x":
            harga -= 2500
        elif item == "bolpen":
            harga -= 3000
        elif item == "penggaris" :
            harga -= 4000
        print(f"{item} berhasil dihapus")
    else:
        print("inputan salah")




