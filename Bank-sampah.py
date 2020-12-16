#Program Bank Sampah

#Buatan: 
#Sindu Masri Priadana
#Politeknik Negeri Semarang


#Akun untuk login :
# 1. username: admin
#    password: admin
# 2. username: customer1
#    password: customer1
# 3. username: customer2
#    password: customer2
# 4. masih rencana agar buat akun sendiri

i=n=0 
n==0
def kembali():
  
  kembali = input("Apa Anda ingin kembali ke Menu Utama[ y / t ]: ")
  if kembali == 'y':
      masuk()
  elif kembali == 't':
      exit
  else:
      print("Maaf yang anda masukkan salah")
      kembali()
def kembaliadmin():
  
  kembali = input("Apa Anda ingin kembali ke Menu Utama[ y / t ]: ")
  if kembali == 'y':
      masukadmin()
  elif kembali == 't':
      exit
  else:
      print("Maaf yang anda masukkan salah")
      kembaliadmin()
  
def tanya():
      
      tanya = input("Apa ada sampah yang ingin disetorkan lagi? [ y / t ] : ")
      if tanya == 'y':
          setor()
      elif tanya == 't':
          hitung()
          a = sum(saldo)
          saldohasil = a
          b = sum(berat)
          beratakhir = b
          kembali()
      else :
          print("Maaf yang anda masukkan salah")
          tanya()
def tanyaadmin():
      
      tanya = input("Apa ada sampah yang ingin disetorkan lagi? [ y / t ] : ")
      if tanya == 'y':
          setoradmin()
      elif tanya == 't':
          hitung()
          a = sum(saldo)
          saldohasil = a
          b = sum(berat)
          beratakhir = b
          kembaliadmin()
      else :
          print("Maaf yang anda masukkan salah")
          tanyaadmin()
      
def setor():
    print("\t==============================")
    print("\t|       Daftar Sampah        |")
    print("\t|----------------------------|")
    print("\t|1. Kwaci \t 6. Aluminium|")
    print("\t|2. Kardus\t 7. Besi     |")
    print("\t|3. Koran \t 8. Kaleng   |")
    print("\t|4. Buku  \t 9. Tembaga  |")
    print("\t|5. Botol \t 10.Lain-lain|")
    print("\t==============================")

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
    else:
        print("Yang anda masukkan tidak ada")
        tanya()
    return
def setoradmin():
    print("\t==============================")
    print("\t|       Daftar Sampah        |")
    print("\t|----------------------------|")
    print("\t|1. Kwaci \t 6. Aluminium|")
    print("\t|2. Kardus\t 7. Besi     |")
    print("\t|3. Koran \t 8. Kaleng   |")
    print("\t|4. Buku  \t 9. Tembaga  |")
    print("\t|5. Botol \t 10.Lain-lain|")
    print("\t==============================")

    kode = int(input("nomor Sampah yang ingin disetorkan : "))
    if kode == 1:
        jumlah1 = int(input("Berapa Kilogram: "))
        total1 = 1000 * jumlah1
        saldo.append(total1)
        berat.append(jumlah1)
        tanyaadmin()
    elif kode == 2:
        jumlah2 = int(input("Berapa Kilogram: "))
        total2 = 2000 * jumlah2
        saldo.append(total2)
        berat.append(jumlah2)
        tanyaadmin()
    elif kode == 3:
        jumlah3 = int(input("Berapa Kilogram: "))
        total3 = 1000 * jumlah3 
        saldo.append(total3)
        berat.append(jumlah3)
        tanyaadmin()
    elif kode == 4:
        jumlah4 = int(input("Berapa Kilogram: "))
        total4 = 1000 * jumlah4 
        saldo.append(total4)
        berat.append(jumlah4)
        tanyaadmin()
    elif kode == 5:
        jumlah5 = int(input("Berapa Kilogram: "))
        total5 = 2000 * jumlah5
        saldo.append(total5)
        berat.append(jumlah5)
        tanyaadmin()
    elif kode == 6:
        jumlah6 = int(input("Berapa Kilogram: "))
        total6 = 5000 * jumlah6   
        saldo.append(total6)
        berat.append(jumlah6)
        tanyaadmin()
    elif kode == 7:
        jumlah7 = int(input("Berapa Kilogram: "))
        total7 = 1000 * jumlah7
        saldo.append(total7)
        berat.append(jumlah7)
        tanyaadmin()
    elif kode == 8:
        jumlah8 = int(input("Berapa Kilogram: "))
        total8 = 5000 * jumlah8   
        saldo.append(total8)
        berat.append(jumlah8)
        tanyaadmin()
    elif kode == 9:
        jumlah9 = int(input("Berapa Kilogram: "))
        total9 = 2000 * jumlah9
        saldo.append(total9)
        berat.append(jumlah9)
        tanyaadmin()
    elif kode == 10:
        jumlah10 = int(input("Berapa Kilogram: "))
        total10 = 1000 * jumlah10
        saldo.append(total10)
        berat.append(jumlah10)
        tanyaadmin()
    else:
        print("Yang anda masukkan tidak ada")
        tanyaadmin()
    return
def jenis():
  print("\t================================================")
  print("\t|No | Nama Sampah  \t\t | Harga per Kg|")
  print("\t|---|----------------------------|-------------|")
  print("\t|1. | Kwaci     \t\t | Rp. 1000    |")     
  print("\t|2. | Kardus    \t\t | Rp. 2000    |")
  print("\t|3. | Koran     \t\t | Rp. 1000    |")
  print("\t|4. | Buku      \t\t | Rp. 1000    |")
  print("\t|5. | Botol     \t\t | Rp. 2000    |")
  print("\t|6. | Aluminium \t\t | Rp. 5000    |")
  print("\t|7. | Besi      \t\t | Rp. 1000    |")
  print("\t|8. | Kaleng    \t\t | Rp. 5000    |")
  print("\t|9. | Galon     \t\t | Rp. 2000    |")
  print("\t|10.| lain-lain \t\t | Rp. 1000    |")
  print("\t================================================")
  kembali()
def hitung():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
def tarik():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print("Penarikan Saldo")
  print("Saldo Anda sekarang      : Rp.",saldohasil)
  keluar = int(input("Jumlah yang ingin diambil: Rp. "))
  if keluar > saldohasil:
      print("Maaf saldo anda tidak cukup")
      tarik()
  elif keluar < 0 :
      print("Anda sedang bercanda ya?")
      tarik()
  else:
      hasil = saldohasil - keluar
      print("saldo anda tersisa       : Rp.",hasil)
      saldo[0] = hasil
      del saldo[1:10] 
      
  kembali()
def tarikadmin():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print("Penarikan Saldo")
  print("Saldo Anda sekarang      : Rp.",saldohasil)
  keluar = int(input("Jumlah yang ingin diambil: Rp. "))
  if keluar > saldohasil:
      print("Maaf saldo anda tidak cukup")
      tarikadmin()
  elif keluar < 0 :
      print("Anda sedang bercanda ya?")
      tarikadmin()
  else:
      hasil = saldohasil - keluar
      print("saldo anda tersisa       : Rp.",hasil)
      saldo[0] = hasil
      del saldo[1:10] 
      
  kembaliadmin()
def listakun():
    print("No\tNama\tUsername\tpassword\tsaldo\tsetoran")
    i = len(data_base_user)
    for n in range(i):
        print(n+1,'.\t',data_base_nama[n][0:11],'\t',data_base_user[n],'\t',data_base_pass[n],'\t',data_base_saldo[n],'\t',data_base_berat,'')
    kembaliadmin()
def masukadmin():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print('='*115)
  print("Selamat Datang, ",username)
  print('')
  print('Saldo Anda    : Rp.',saldohasil)
  print('berat setor-an:    ',beratakhir,'Kg')
  print('')
  print("\t|====================|")
  print("\t| 1. Setor Sampah    |")
  print("\t| 2. Jenis Sampah    |")
  print("\t| 3. Penarikan Uang  |")
  print("\t| 4. List Akun     |")
  print("\t| 5. keluar aplikasi |")
  print("\t|====================|")
  pilihan = input("Pilih menu: ")
  if pilihan == '1':
      print('='*115)
      setoradmin()
  elif pilihan == '2':
      print('='*115)
      jenis()
  elif pilihan == '3':
      print('='*115)
      tarikadmin()
  elif pilihan == '4':
      print('='*115)
      listakun()
  elif pilihan == '5':
      print('='*115)
      exit
  else:
      print("Pilihan anda tidak ada")
      kembali()
def masuk():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print('='*115)
  print("Selamat Datang, ",username)
  print('')
  print('Saldo Anda    : Rp.',saldohasil)
  print('berat setor-an:    ',beratakhir,'Kg')
  print('')
  print("\t|====================|")
  print("\t| 1. Setor Sampah    |")
  print("\t| 2. Jenis Sampah    |")
  print("\t| 3. Penarikan Uang  |")
  print("\t| 4. keluar aplikasi |")
  print("\t|====================|")
  pilihan = input("Pilih menu: ")
  if pilihan == '1':
      print('='*115)
      setor()
  elif pilihan == '2':
      print('='*115)
      jenis()
  elif pilihan == '3':
      print('='*115)
      tarik()
  elif pilihan == '4':
      print('='*115)
      exit
  else:
      print("Pilihan anda tidak ada")
      kembali()
#login
def login():
    global data_base_user, data_base_pass, data_base_saldo, data_base_berat, data_base_nama, username, saldo, berat, password
    data_base_user = ['admin','customer1','customer2','0']
    data_base_pass = ['admin','customer1','customer2','0']
    data_base_saldo =[ 0, 0, 0, 0 ]
    data_base_berat =[ 0, 0, 0, 0 ]
    data_base_nama = ['admin','customer1','customer2','0']
    username = input("Username: ")
    password = input("Password: ")

    if username == data_base_user[0]:
        if password == data_base_pass[0]:
              saldo = []
              data_base_saldo[0] = sum(saldo)
              berat = []
              data_base_berat[0] = sum(berat)
              print('')
              masukadmin()
        else :
              print ("Maaf Username atau Password salah")
              exit
    elif username == data_base_user[1]:
        if password == data_base_pass[1]:
              saldo = []
              data_base_saldo[1] = sum(saldo)
              berat = []
              data_base_berat[1] = sum(berat)
              print('')
              masuk()
        else :
              print ("Maaf Username atau Password salah")
              exit
    elif username == data_base_user[2]:
        if password == data_base_pass[2]:
              saldo = []
              data_base_saldo[2] = sum(saldo)
              berat = []
              data_base_berat[2] = sum(berat)
              print('')
              masuk()
        else :
              print ("Maaf Username atau Password salah")
              exit
    elif username == data_base_user[3]:
        if password == data_base_pass[3]:
              saldo = []
              data_base_saldo[3] = sum(saldo)
              berat = []
              data_base_berat[3] = sum(berat)
              print('')
              masuk()
        else :
              print ("Maaf Username atau Password salah")
              exit

    else:
        print ("Maaf Username atau Password salah")
        exit

login()
