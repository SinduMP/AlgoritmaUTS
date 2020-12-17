#Program Bank Sampah

#Buatan: 
#Sindu Masri Priadana
#Politeknik Negeri Semarang
#          2020

#Akun untuk login :
# 1. username: admin
#    password: admin
# 2. username: customer1
#    password: customer1
# 3. username: customer2
#    password: customer2
# 4. register mandiri

# Keterangan:
# agar list akun merata minimal 6 huruf/angka/symbol (masih pengembangan)
# akun regestrasi hanya mengubah data akun ke 4, belum digunakan untuk menambah akun lebih banyak.

# Program:
i=n=0 
n==0

#class color
class color:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

def kembali():
  
  kembali = input("Apa Anda ingin kembali ke Menu Utama[ y=ya / t=logout ]: ")
  if kembali == 'y':
      masuk()
  elif kembali == 't':
      menuawal()
  else:
      print("Maaf yang anda masukkan salah")
      kembali()
def kembaliadmin():
  
  kembali = input("Apa Anda ingin kembali ke Menu Utama[ y=ya / t=logout ]: ")
  if kembali == 'y':
      masukadmin()
  elif kembali == 't':
      menuawal()
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
#Menu Customer
def masuk():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print('='*115)
  print(color.BLUE +color.BOLD+"Selamat Datang, "+color.END,nama)
  print('')
  print('Saldo Anda    : Rp.',saldohasil)
  print('berat setor-an:    ',beratakhir,'Kg')
  print('')
  print(color.GREEN + "\t|====================|")
  print("\t| 1. Setor Sampah    |")
  print("\t| 2. Jenis Sampah    |")
  print("\t| 3. Penarikan Uang  |")
  print("\t| 4. keluar aplikasi |")
  print("\t| 5. Logout          |")
  print("\t|====================|" +color.END)
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
  elif pilihan == '5':
      print('='*115)
      login()
  else:
      print("Pilihan anda tidak ada")
      kembali()

def setor():
    print(color.GREEN +"\t==============================")
    print("\t|       Daftar Sampah        |")
    print("\t|----------------------------|")
    print("\t|1. Kwaci \t 6. Aluminium|")
    print("\t|2. Kardus\t 7. Besi     |")
    print("\t|3. Koran \t 8. Kaleng   |")
    print("\t|4. Buku  \t 9. Tembaga  |")
    print("\t|5. Botol \t 10.Lain-lain|")
    print("\t==============================" +color.END)

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
def jenis():
  print(color.GREEN +"\t================================================")
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
  print("\t================================================" +color.END)
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
  print(color.BLUE +"Penarikan Saldo"+color.END)
  bank = input ("Bank                     : ")
  no_rekening = input ("No rekening              : ")
  print('')
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
      print (color.RED +"="*30)
      print ("\tBank Sampah")
      print ("\t  E-Cash")
      print ('')
      print ("Transfer Berhasil")
      print ("No Rek :",no_rekening)
      print ("Nama   :",nama)
      print ("Bank   :",bank)
      print ('')
      print ("Jumlah : Rp.",keluar)
      print ("="*30 + color.END)
      print ('') 
      
  kembali()
#Menu Admin
def setoradmin():
    print(color.GREEN + "\t==============================")
    print("\t|       Daftar Sampah        |")
    print("\t|----------------------------|")
    print("\t|1. Kwaci \t 6. Aluminium|")
    print("\t|2. Kardus\t 7. Besi     |")
    print("\t|3. Koran \t 8. Kaleng   |")
    print("\t|4. Buku  \t 9. Tembaga  |")
    print("\t|5. Botol \t 10.Lain-lain|")
    print("\t==============================" +color.END)

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

def tarikadmin():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print(color.BLUE +"Penarikan Saldo"+color.END)
  bank = input ("Bank                     : ")
  no_rekening = input ("No rekening              : ")
  print('')
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
      print (color.RED +"="*30)
      print ("\tBank Sampah")
      print ("\t  E-Cash")
      print ('')
      print ("Transfer Berhasil")
      print ("No Rek :",no_rekening)
      print ("Nama   :",nama)
      print ("Bank   :",bank)
      print ('')
      print ("Jumlah : Rp.",keluar)
      print ("="*30 + color.END)
      print ('') 
      
  kembaliadmin()
def jenisadmin():
  print(color.GREEN +"\t================================================")
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
  print("\t================================================" +color.END)
  kembaliadmin()
def listakun():
    print("No\tNama\t\tUsername\tpassword")
    i = len(data_base_user)
    for n in range(i):
        print(n+1,'.\t',data_base_nama[n][0:11],'\t',data_base_user[n],'\t',data_base_pass[n])
    kembaliadmin()
def masukadmin():
  a = sum(saldo)
  saldohasil = a
  b = sum(berat)
  beratakhir = b
  print('='*115)
  print(color.BLUE+color.BOLD+"Selamat Datang, "+color.END,nama)
  print('')
  print('Saldo Anda    : Rp.',saldohasil)
  print('berat setor-an:    ',beratakhir,'Kg')
  print(color.GREEN + '')
  print("\t|====================|")
  print("\t| 1. Setor Sampah    |")
  print("\t| 2. Jenis Sampah    |")
  print("\t| 3. Penarikan Uang  |")
  print("\t| 4. List Akun       |")
  print("\t| 5. Logout          |")
  print("\t| 6. keluar aplikasi |")
  print("\t|====================|" + color.END)
  pilihan = input("Pilih menu: ")
  if pilihan == '1':
      print('='*115)
      setoradmin()
  elif pilihan == '2':
      print('='*115)
      jenisadmin()
  elif pilihan == '3':
      print('='*115)
      tarikadmin()
  elif pilihan == '4':
      print('='*115)
      listakun()
  elif pilihan == '5':
      print('='*115)
      login()
  elif pilihan == '6':
      print('='*115)
      exit
  else:
      print("Pilihan anda tidak ada")
      kembali()
#login
def login():
    global  username, saldo, berat, password, nama
    print(color.BOLD + color.BLUE + "Login: " +color.END)
    print('')
    username = input("Username: ")
    password = input("Password: ")

    if username == data_base_user[0]:
        if password == data_base_pass[0]:
              saldo = []
              data_base_saldo[0] = sum(saldo)
              berat = []
              data_base_berat[0] = sum(berat)
              nama = data_base_nama[0]
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
              nama = data_base_nama[1]
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
              nama = data_base_nama[2]
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
              nama = data_base_nama[3]
              print('')
              masuk()
        else :
              print ("Maaf Username atau Password salah")
              exit

    else:
        print ("Maaf Username atau Password salah")
        tanya = input("Apa anda ingin membuat akun? [ y / t ]: ")
        if tanya == 'y':
            register()
        elif tanya == 't':
            menuawal()
        else:
            print("Maaf ada kesalahan")
            login()
def register():
    print('='*115)
    print(color.BOLD + color.BLUE +"Register Account" +color.END)
    print('')
    nama = input("Nama    : ")
    user = input("Username: ")
    passw= input("Password: ")
    data_base_nama[3] = nama
    data_base_user[3] = user
    data_base_pass[3] = passw
    tanya = input("Apa anda sudah yakin data benar? [ y / t ]: ")
    if tanya == 'y':
        login()
    elif tanya == 't':
        register()
    else:
        print("Maaf ada kesalahan")
        menuawal()
    print('='*115)
def menuawal():
    print('='*115)
    print(color.BOLD + color.GREEN + "Bank Sampah" + color.END)
    print('')
    print("Selamat datang")
    print("1. Login")
    print("2. Register")
    print("3. Keluar Aplikasi")
    pil = input("Pilih [1 / 2 / 3]: ")
    if pil == '1':
        login()
    elif pil == '2':
        register()
    elif pil == '3':
        exit
    else:
        print("Maaf yang anda masukkan salah")
        menuawal()
def data_base():
    global data_base_user, data_base_pass, data_base_saldo, data_base_berat, data_base_nama
    data_base_user = ['admin','customer1','customer2','-']
    data_base_pass = ['admin','customer1','customer2','-']
    data_base_saldo =[ 0, 0, 0, 0 ]
    data_base_berat =[ 0, 0, 0, 0 ]
    data_base_nama = ['Admin Bank Sampah','Customer1','Customer2','-']
data_base()
menuawal()
