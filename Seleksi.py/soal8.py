print("Kelulusan Ujian")
print("Kategori ujian : 1.Teori 2.Praktik")

kategori = int(input("Pilih kategori ujian tsb: "))

match kategori :
 case 1 :
  print("\nAnda memilih kategori Teori")
 case 2 :
  print("\nAnda memilih kategori Praktik")
 case _:
  print("\nKategori ujian tidak valid")

nilai_siswa = int(input("\nMasukkan nilai ujian anda berdasarkan kategori yang dipilih: "))

if nilai_siswa >= 75 :
    print("\nSelamat anda lulus!")
else :
    print("\nMaaf,anda harus mengulang!")