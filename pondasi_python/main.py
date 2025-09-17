from package import kalkulator
from package import pagi, siang, malam 
from package import menyapa
from package import celcius_fahrenheit, fahrenheit_celcius

# suhu
print(celcius_fahrenheit(34))
print(fahrenheit_celcius(89))

a = int(input("masukkan nilai a : "))
b = int(input("masukkan nilai b : "))

# kalkulator
print(kalkulator.tambah(a, b))
print(kalkulator.tambah(23, 92))


menyapa.pagi()
