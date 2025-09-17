def hitung():
    uts = float(input("Masukkan Nilai UTS : "))
    uas = float(input("Masukkan Nilai UAS : "))
    kuis = float(input("Masukkan Nilai Kuis : "))

    nilaiAkhir = ((uts * 30 / 100) + (uas * 30 / 100) + (kuis * 40 / 100))

    print("=============================")

    print(f"Nilai Akhir adalah {nilaiAkhir}")

    if 0 <= nilaiAkhir <= 50:
        print("Nilai Akhir adalah D")
    elif 50 < nilaiAkhir <= 70:
        print("Nilai Akhir adalah C")
    elif 70 < nilaiAkhir <= 90:
        print("Nilai Akhir adalah B")
    elif 90 < nilaiAkhir <= 100:
        print("Nilai Akhir adalah A")
    else:
        print("Tidak Valid") 