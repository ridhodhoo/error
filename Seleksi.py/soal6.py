print("Menentukan 1-6 nama bulan")

bulan = int(input("Masukkan angka(1-6): "))

match bulan :
 case 1 :
  print("1.Januari")
 case 2 :
  print("2.Februari")
 case 3 :
  print("3.Maret")
 case 4 :
  print("4.April")
 case 5 :
  print("5.Mei")
 case 6 :
  print("6.Juni")
 case _:
  print("Bulan tidak tersedia")