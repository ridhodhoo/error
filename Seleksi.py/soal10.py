#Buatlah program untuk kasus : jika usia pengunjung lebih dari atau sama dengan 17 tahun maka bisa memilih
# film, genre filmnya ada horor, komedi, keluarga, dan aksi. jika memilih film horor, maka pengunjung bisa
# memilih apakah film horor indonesia atau horor luar negeri, begitupun jika memilih film komedi, keluarga
#. jika memilih film aksi maka pengunjung bisa memilih film hollywood, indonesia, atau bollywood. jika
# usia pengunjung kurang dari 17 tahun maka pengunjung bisa memilih film animasi 2 dimensi, atau 3 dimensi
#. jika memilih 2 dimensi maka pengunjung bisa memilih film naruto atau one piace, jika memilih 3 dimensi
# maka pengunjung bisa memilih film nemo atau kungfu panda. Saat sudah memilih maka munculkan kalimat
# "Selamat Menyaksikan "Judul Film".

print("Film Movie terbaik")
print("\nNote:")
print("(16+)JIKA SUDAH LEBIH DARI 16 TAHUN MAKA DAPAT MENONTON FILM HORROR,COMEDY,FAMILY DAN ACTION")
print("JIKA DIBAWAH DARI 17 TAHUN MAKA DAPAT MENONTON FILM 2D DAN 3D")

usia = int(input("Masukkan usia anda: "))

if usia >= 17 :
   print("\nPilihlah tema film berikut")
   print("1.Horror")
   print("2.Comedy")
   print("3.Family")
   print("4.Action")

   kategori = int(input("Masukkan tema film (1-4): "))

   match kategori :
    case 1 :
     print("\nAnda memilih Film horror")
     ket = input("pilihlan film 1.Indonesia atau 2.Luar negeri: ")

     match ket :
       case "1":
         print("Anda memilih film horror indonesia")
         print("Selamat menyaksikan Film Agak lain")
       case "2":
         print("Anda memilih film horror luar negeri")
         print("Selamat menyaksikan Film The Nun")

    case 2 :
     print("\nAnda memilih Film comedy")
     ket2 = input("pilihlan film 1.Indonesia atau 2.Luar negeri: ")
      
     match ket2 :
       case "1":
         print("Anda memilih film comedy indonesia")
         print("Selamat menyaksikan Film Agak lain")
       case "2":
         print("Anda memilih film comedy luar negeri")
         print("Selamat menyaksikan Film Deadpool")
 
    case 3 :
     print("\nAnda memilih Film family")
     ket3 = input("pilihlan film 1.Indonesia atau 2.Luar negeri: ")
      
     match ket3 :
       case "1":
         print("Anda memilih film family indonesia")
         print("Selamat menyaksikan Film GGS")
       case "2":
         print("Anda memilih film family luar negeri")
         print("Selamat menyaksikan Film Sonic 2")
    
    case 4 :
     print("\nAnda memilih Film action")
     ket4 = input("pilihlan film 1.Indonesia atau 2.Luar negeri: ")
      
     match ket4 :
       case "1":
         print("Anda memilih film action indonesia")
         print("Selamat menyaksikan Film Sepatu super")
       case "2":
         print("Anda memilih film action luar negeri")
         print("Selamat menyaksikan Film Spiderman")

    case _:
     print("\nKategori tidak valid")

else :
  print("\nPilihlah tema film berikut")
  print("1.2D")
  print("2.3D")

  kategori2 = int(input("Masukkan tema film (1-2): "))

  match kategori2 :
   case 1 :
     print("\nAnda memilih Film 2D")
     keta = input("pilihlan film 1.One piece atau 2.naruto: ")

     match keta :
       case "1":
         print("Selamat menyaksikan Film One piece")
       case "2":
         print("Selamat menyaksikan Film naruto")

   case 2 :
      print("\nAnda memilih Film 3D")
      keta1 = input("pilihlan film 1.Nemo atau 2.Kung Fu Panda: ")
      
      match keta1 :
       case "1":
         print("Selamat menyaksikan Film Nemo")
       case "2":
         print("Selamat menyaksikan Film Kung Fu Panda")