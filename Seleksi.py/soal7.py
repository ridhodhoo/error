print("Menu minuman")
print("Pilihan : (1.Esteh : 5.000)(2.Es jeruk : 7.000)(3.Kopi : 8.000)(4.Susu : 6.000)")

menu = int(input("Pilihlah Minuman yang ingin dipilih: "))

match menu :
 case 1 :
  print("1.Esteh : 5.000")
 case 2 :
  print("2.Es jeruk : 7.000")
 case 3 :
  print("3.Kopi : 8.000")
 case 4 :
  print("4.Susu : 6.000")
 case _:
  print("Menu tidak tersedia")