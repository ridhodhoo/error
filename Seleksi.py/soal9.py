print("Jenis pelanggan+Diskonnya")

kategori = int(input("Masukkan jenis pelanggan (1.Member 2.Non member): "))

match kategori :
 case 1 :
  print("\nAnda mendapatkan diskon 10% jika total belanja lebih dari 100.000")
 case 2 :
  print("\nAnda mendapatkan diskon 5% jika total belanja lebih dari 100.000")
 case _:
  print("\nKategori jenis pelanggan tidak valid")

total_belanja = int(input("\nMasukkan total belanja anda: "))

if total_belanja >= 100000 :
    print("\nSelamat anda mendaptkan diskon sesuai jenis pelanggannya")
else :
    print("\nMaaf,anda tidak mendapatkan diskon karena jumlah total belanja tidak sesuai")