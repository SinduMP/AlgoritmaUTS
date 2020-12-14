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
      tanya = input("Apa ada sampah yang ingin disetorkan lagi? [ y / t ] : ")
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

    print("-------------------------------")
    kode = int(input("nomor Sampah yang ingin disetorkan : "))
    if kode == 1:
        jumlah1 = int(input("Berapa Kilogram: "))
        total1 = 1000 * jumlah1
        saldo.append(total1)
        berat.append(jumlah1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Berapa Kilogram: "))
        total2 = 2000 * jumlah2
        saldo.append(total2)
        berat.append(jumlah2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Berapa Kilogram: "))
        total3 = 1000 * jumlah3 
        saldo.append(total3)
        berat.append(jumlah3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Berapa Kilogram: "))
        total4 = 1000 * jumlah4 
        saldo.append(total4)
        berat.append(jumlah4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("Berapa Kilogram: "))
        total5 = 2000 * jumlah5
        saldo.append(total5)
        berat.append(jumlah5)
        tanya()
    elif kode == 6:
        jumlah6 = int(input("Berapa Kilogram: "))
        total6 = 5000 * jumlah6   
        saldo.append(total6)
        berat.append(jumlah6)
        tanya()
    elif kode == 7:
        jumlah7 = int(input("Berapa Kilogram: "))
        total7 = 1000 * jumlah7
        saldo.append(total7)
        berat.append(jumlah7)
        tanya()
    elif kode == 8:
        jumlah8 = int(input("Berapa Kilogram: "))
        total8 = 5000 * jumlah8   
        saldo.append(total8)
        berat.append(jumlah8)
        tanya()
    elif kode == 9:
        jumlah9 = int(input("Berapa Kilogram: "))
        total9 = 2000 * jumlah9
        saldo.append(total9)
        berat.append(jumlah9)
        tanya()
    elif kode == 10:
        jumlah10 = int(input("Berapa Kilogram: "))
        total10 = 1000 * jumlah10
        saldo.append(total10)
        berat.append(jumlah10)
        tanya()
    return
def jenis():
  print('='*115)
  print("No | Nama Sampah  \t | Harga per Kg")
  print("1. | Kwaci     \t\t | Rp.1000")
  print("2. | Kardus    \t\t | Rp.2000")
  print("3. | Koran     \t\t | Rp.1000")
  print("4. | Buku      \t\t | Rp.1000")
  print("5. | Botol     \t\t | Rp.2000")
  print("6. | Aluminium \t\t | Rp.5000")
  print("7. | Besi      \t\t | Rp.1000")
  print("8. | Kaleng    \t\t | Rp.5000")
  print("9. | Galon     \t\t | Rp.2000")
  print("10.| lain-lain \t\t | Rp.1000")
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
  keluar = int(input("Jumlah yang ingin diambil: "))
  if keluar > saldoakhir:
      print("Maaf saldo anda tidak cukup")
      tarik()
  elif keluar < 0 :
      print("Anda sedang bercanda ya?")
      tarik()
  else:
      hasil = saldoakhir - keluar
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
  print('berat setor-an:',beratakhir,' Kg')
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
print('='*115)
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

