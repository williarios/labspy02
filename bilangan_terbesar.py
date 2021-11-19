angka1 = input("Msukan angka pertama: ")
angka2 = input("Masukan angka kedua: ")
angka3 = input("Masukan angka ketiga: ")

if(int(angka1)>int(angka2) and int(angka1)>int(angka3)):
    print(angka1, "merupakan bilangan terbesar")
if(int(angka2)>int(angka1) and int(angka2)>int(angka3)) :
    print(angka2, "merupakan bilangan terbesar")
if(int(angka3)>int(angka1) and int(angka3)>int(angka2)):
    print(angka3, "merupakan bilangan terbesar")

