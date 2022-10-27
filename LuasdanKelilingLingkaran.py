print("Program Python Hitung Luas dan Keliling Lingkaran")
print("---------------Riris Naomi Gurning---------------\n")

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya : "))
luas   = pi*(jari*jari)
keliling   = 2*pi*jari

print("\n-----------------Hasilnya-----------------")
print("Luas Lingkaran =","{:.3f}".format(luas))
print("Keliling Lingkaran =","{:.3f}".format(keliling))