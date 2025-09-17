menu = {
    "Ayam" : 15000,
    "Lele" : 10000,
    "Nasi" : 5000,
    "Es Teh" : 3000,
}

global totalHarga

def pesanMakanan():
    print("==== Warmindo Sugema ====")
    
    totalHarga = 0

    for key in menu.keys():
        print(key, " : ", menu[key])

    while True :
        pesan = input("Pesan makan apa a? (s untuk selesai) : ")

        if pesan == "s":
            break
        elif pesan in menu:
            jumlah = int(input("Mau pesan berapa? : "))
            totalHarga += menu[pesan] * jumlah
        else:
            print("menu tidak tersedia")
        
    pajak = totalHarga * (11/100)
    totalBayar = totalHarga + pajak

    print("======================")
    print(f"Total {totalHarga}")
    print(f"Pajak {pajak}")
    print("======================")
    print(f"Total yang harus dibayar : {totalBayar}")