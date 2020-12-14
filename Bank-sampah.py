#SinduMP/AlgoritmaUTS
#

      
def kembali():
  kembali = input("Apa Anda ingin kembali ke Menu Utama[ y / t ]: ")
  if kembali == 'y':
      masuk()
  elif kembali == 't':
      exit
  else:
      print("Maaf yang anda masukkan salah")
      kembali()
def tanya():
      tanya = input("Ada ada sampah yang ingin disetorkan lagi? [ y / t ] : ")
      if tanya == 'y':
          setor()
      elif tanya == 't':
          hitung()
          a = sum(saldo)
          saldoakhir = a
          b = sum(berat)
          beratakhir = b
          kembali()
      else :
          print("Maaf yang anda masukkan salah")
          tanya()
def setor():
  print('='*115)
  print("Daftar Sampah: ")
  print("1. Kwaci \t 6. Aluminium")
  print("2. Kardus\t 7. Besi     ")
  print("3. Koran \t 8. Kaleng   ")
  print("4. Buku  \t 9. Tembaga  ")
  print("5. Botol \t 10.Lain-lain")
  print('='*115)
  kode = input(" nomor sampah yang ingin disetorkan: ")
  if kode == 1:
      jumlah1 = input("Berapa Kilogram: ")
      setor1 = 1000 * jumlah1
      berat.append(jumlah1)
      setor.append(setor1)
      tanya()
  elif kode == 2:
      jumlah2 = input("Berapa Kilogram: ")
      setor2 = 2000 * jumlah2
      berat.append(jumlah2)
      setor.append(setor2)
      tanya()
  elif kode == 3:
      jumlah3 = input("Berapa Kilogram: ")
      setor3 = 1000 * jumlah3
      berat.append(jumlah3)
      setor.append(setor3)
      tanya()
  elif kode == 4:
      jumlah4 = input("Berapa Kilogram: ")
      setor4 = 1000 * jumlah4
      berat.append(jumlah4)
      setor.append(setor4)
      tanya()
  elif kode == 5:
      jumlah5 = input("Berapa Kilogram: ")
      setor5 = 2000 * jumlah5
      berat.append(jumlah5)
      setor.append(setor5)
      tanya()
  elif kode == 6:
      jumlah6 = input("Berapa Kilogram: ")
      setor6 = 5000 * jumlah6
      berat.append(jumlah6)
      setor.append(setor6)
      tanya()
  elif kode == 7:
      jumlah7 = input("Berapa Kilogram: ")
      setor7 = 1000 * jumlah7
      berat.append(jumlah7)
      setor.append(setor7)
      tanya()
  elif kode == 8:
      jumlah8 = input("Berapa Kilogram: ")
      setor8 = 5000 * jumlah8
      berat.append(jumlah8)
      setor.append(setor8)
      tanya()
  elif kode == 9:
      jumlah9 = input("Berapa Kilogram: ")
      setor9 = 2000 * jumlah9
      berat.append(jumlah9)
      setor.append(setor9)
      tanya()
  elif kode == 10:
      jumlah10 = input("Berapa Kilogram: ")
      setor10 = 1000 * jumlah10
      berat.append(jumlah10)
      setor.append(setor10)
      tanya()
  return
def jenis():
  print('='*115)
  print("No | Nama Sampah  \t | Harga per Kg")
  print("1. | Kwaci     \t | Rp.1000")
  print("2. | Kardus    \t | Rp.2000")
  print("3. | Koran     \t | Rp.1000")
  print("4. | Buku      \t | Rp.1000")
  print("5. | Botol     \t | Rp.2000")
  print("6. | Aluminium \t | Rp.5000")
  print("7. | Besi      \t | Rp.1000")
  print("8. | Kaleng    \t | Rp.5000")
  print("9. | Galon     \t | Rp.2000")
  print("10.| lain-lain \t | Rp.1000")
  kembali()
def hitung():
  a = sum(saldo)
  saldoakhir = a
  b = sum(berat)
  beratakhir = b
def tarik():
  a = sum(saldo)
  saldoakhir = a
  b = sum(berat)
  beratakhir = b
  print("Penarikan Saldo")
  print("Saldo Anda sekarang : ",saldoakhir)
  tarik = int(input("Jumlah yang ingin diambil: "))
  if tarik > saldoakhir:
      print("Maaf saldo anda tidak cukup")
      tarik()
  elif tarik < 0 :
      print("Anda sedang bercanda ya?")
      tarik()
  else:
      hasil = saldoakhir - tarik
      print("saldo anda tersisa: Rp.",hasil)
  kembali()
def masuk():
  a = sum(saldo)
  saldoakhir = a
  b = sum(berat)
  beratakhir = b
  print('')
  print('='*115)
  print("Selamat Datang")
  print('',username)
  print('Saldo Anda: Rp.',saldoakhir)
  print(beratakhir,' Kg')
  print('')
  print('='*115)
  print("1. Setor Sampah")
  print("2. Jenis Sampah")
  print("3. Penarikan Uang")
  print("4. keluar aplikasi")
  print('='*115)
  pilihan = input("Pilih menu: ")
  if pilihan == '1':
      setor()
  elif pilihan == '2':
      jenis()
  elif pilihan == '3':
      tarik()
  elif pilihan == '4':
      exit
  else:
      print("Pilihan anda tidak ada")
      kembali()
#login
print("Login Akun :")
username = input("Username : ")
passwd = input("Password : ")
if username == 'admin':
    if passwd == 'admin':
          saldo = [0]
          berat = [0]
          masuk()
    else :
          print ("Maaf Username atau Password salah")
          exit
elif username == 'nasabah':
    if passwd == 'nasabah':
          saldo = [0]
          berat = [0]
          masuk()
    else :
          print ("Maaf Username atau Password salah")
          exit
else:
    print ("Maaf Username atau Password salah")
    exit

