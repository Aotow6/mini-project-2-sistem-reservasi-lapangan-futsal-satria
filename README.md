-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        FLOWCHART
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                            ![Salinan Diagram Tanpa Judul drawio (1)](https://github.com/user-attachments/assets/cd2af81e-6592-4c78-a669-67866e8942f0)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from prettytable import PrettyTable

usnadmin = "admin"
pwadmin = "admin"
usnuser = "user"
pwuser = "user"

lapangan = {
    "lapangan rumput A": {"harga": "100000"},
}

reservasi = {
    "lapangan rumput A": [
        {"pemesan": "Pras", "tanggal": "2024-10-15", "jam_mulai": 18.00, "jam_selesai": 20.00, "password": "12"},
    ]
}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Baris 1-16 
  jadi disini saya ada import pretty table untuk menggunakan nya nanti saat menanpilkan data dari lapangan dan reservasi terus ada variable2 buat login admin dan user lalu ada dictionary dari lapangan dan disini lapangan terdiri dari harga saja  sama nama baut nanti dipanggil2 terus reservasi ini dictionary yang didalamnya adalah list yang didalamnya lagi adalah dictionary mengapa? karena sebelumnya struktur nya hanya dictionary dan itu setiap saya tambah reservasi untuk suatu lapangan bukanya nambah maalah nge update data jadi cuma bisa menyimpan 1 reservasi dalam 1 lapangan akhirnya saya ubah jadi ini yg sekarang bisa banyak reservasi dalam 1 lapangan.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login():
    print("==== CHAMPION FUTSAL ====")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == usnadmin and password == pwadmin:
        print(f"Welcome {usnadmin} ")
        admin_menu()
    elif username == usnuser and password == pwuser:
        print(f"Welcome {usnuser} ")
        pengguna_menu()
    else:
        print("Username atau password salah. Silakan coba lagi.")
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Baris 18-30
  disini ada function login yang dimana input usn dan password nah jika usn and password 2 2 nya sama dengan variable buat login yang di baris 4-7 maka mereka akan membuka menu berdasarkan hak akses mereka dan untuk membukanya memmanggil function menu dari hak akses tersebut
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_menu():
    while True:
        print("\n==== MENU ADMIN ====")
        print("1. Tambah Lapangan")
        print("2. Lihat Lapangan")
        print("3. Edit Lapangan")
        print("4. Hapus Lapangan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            tambah_lapangan()
        elif pilihan == "2":
            lihat_lapangan()
        elif pilihan == "3":
            edit_lapangan()
        elif pilihan == "4":
            hapus_lapangan()
        elif pilihan == "5":
            print("Keluar dari menu admin.")
            login()  
            break
        else:
            print("Pilihan tidak valid.")

def pengguna_menu():
    while True:
        print("\n==== MENU PENGGUNA ====")
        print("1. Lihat Lapangan")
        print("2. Reservasi Lapangan")
        print("3. Lihat Reservasi")
        print("4. Batalkan Reservasi")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            lihat_lapangan()
        elif pilihan == "2":
            reservasi_lapangan()
        elif pilihan == "3":
            lihat_reservasi()
        elif pilihan == "4":
            batalkan_reservasi()    
        elif pilihan == "5":
            print("Keluar dari menu pengguna.")
            login()  
            break
        else:
            print("Pilihan tidak valid.")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Baris 33-81
disini ada function untuk membuka menu dari admin dan user yang kurang lebih sama  yang dimana ada loopin while dan looping nya baru akan berhenti jika karena  "break" nah itu ada di opsi 5 yang dimana itu balik ke menu login lagi, ya disini cuman buat kek navigasi aja sih kalo pilih nomor sekian bakal manggil funcuion ini dan itu.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def tambah_lapangan():
    nama = input("Masukkan nama lapangan: ")
    while True:
        try:
            harga = int(input("Masukkan harga sewa per jam: "))
            if harga <= 0:
                print("Harga tidak boleh 0 atau kurang.")
            else:
                break
        except ValueError:
            print("Input harus berupa angka.")
    lapangan[nama] = {"harga": harga}
    reservasi[nama] = []
    print(f"Lapangan {nama} berhasil ditambahkan")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Baris 83-96
disini ada function untuk create lapangan kita input nama terlebih dahulu lalu input harga nah disini ada thile true dan try except untuk security dan validasi agar data yang di input valid seperti nilau harus berupa angka dan tidak boleh bernilai 0 dan dibawahnya  lalu setelah terpenuhi lapangan ditambahkan ke dalam dictionary lapangan dengan nama sebagai kunci nya dan harga sebagai nilai nah disini kita juga mengisi dictionary reservasi dengan kunci yang sama tapi hanya menyimpan data kosong untuk sementara ini bakal digunakan nanti untuk mencata reservasi yang terkait dengan lapangan ini ya terus setelah seperti biasa pesan sukses jika berhasil menginput data.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def lihat_lapangan():
    if lapangan:
        print("\n==== DAFTAR LAPANGAN ====")
        table = PrettyTable()
        table.field_names = ["Nama Lapangan", "Harga per Jam"]
        for nama_lapangan in lapangan:
            table.add_row([nama_lapangan, f"Rp{lapangan[nama_lapangan]["harga"]}"])
        print(table)
    else:
        print("Belum ada lapangan yang tersedia.")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Baris 98-107
nah fungsi ini dipake buat nampilin daftar lapangan yang tersedia sama harganya terus saya pakai pretty tabel biar dapet tambahan nilai. nah function diawalai dengan pengecekan apakah dictionary lapangan berisi data jika tidak maka muncul "belum ada lapangan" tapi kalo ada maka akan tampil, disini field names nya hanya nama lapangan dan harga lalu ada looping for untuk iterasi setiap bilangan yang ada dalam lapangan. setiap baris yang ditambahkan ke tabel menggunakan add_row() dimana nama lapangan dan harga sewa nya ditampilkan nah harga juga ditampilkan dengan format Rp.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def edit_lapangan():
    lihat_lapangan()
    nama = input("Masukkan nama lapangan yang ingin diedit: ")
    if nama in lapangan:
        while True:
            try:
                harga_baru = int(input(f"Masukkan harga baru untuk lapangan {nama}: "))
                if harga_baru <= 0:
                    print("Harga tidak boleh 0 atau kurang.")
                else:
                    break
            except ValueError:
                print("Input harus berupa angka.")      
        lapangan[nama]["harga"] = harga_baru
        print(f"Lapangan {nama} berhasil diperbarui")
    else:
        print(f"Lapangan {nama} tidak ditemukan.")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
109 - 125
seperti nama funtion nya ini digunakan untuk mengedit lapangan nah tapi saya bikin hanya untuk edit harga saja.
yang pertama ada input untuk nama lapangan kan nama lapangan ini sebagai key  baru ada next nya ada input harga_baru  yang akan digunakan untuk mengubah harga dari key yang dimasukan lalu seperti biasa ada while dan try untuk security dan validasi agar bernilai angka dan lebih dari 0 lalu ada perkondisian juga sebelumnya jika nama lapangan tidak ditemukan.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hapus_lapangan():
    lihat_lapangan()
    nama = input("Masukkan nama lapangan yang ingin dihapus: ")
    if nama in lapangan:
        del lapangan[nama]
        del reservasi[nama] 
        print(f"Lapangan {nama} berhasil dihapus")
    else:
        print(f"Lapangan {nama} tidak ditemukan.")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
127-135
fungsi ini digunakan untuk menghapus lapangan dengan kita menginput nama lapangan sebagai key lalu akan menghapus lapangan dan reservasi yang mempunyai nama tersebut  sebelumnya juga ada perkondisian jika nama lapangan tidak ditemukan.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def reservasi_lapangan():
    lihat_lapangan()
    nama = input("Masukkan nama lapangan yang ingin dipesan: ")
    if nama in lapangan:
        tanggal = input("Masukkan tanggal pemesanan (YYYY-MM-DD): ")
        try:
            jam_mulai = float(input("Masukkan jam mulai (misal: 18.00): "))
            jam_selesai = float(input("Masukkan jam selesai (misal: 20.00): "))

            if jam_mulai <= 0 or jam_selesai <= 0:
                print("Jam tidak boleh 0 atau kurang.")
                return

            if jam_mulai >= 24 or jam_selesai > 24:
                print("Jam hanya valid antara 0 hingga 24.")
                return

            if jam_mulai >= jam_selesai:
                print("Jam selesai harus lebih besar dari jam mulai.")
                return

        except ValueError:
            print("Input jam harus berupa angka desimal.")
            return

        nama_pemesan = input("Masukkan nama Anda: ")
        password = input("Masukan password Anda: ")

        for reservasi_item in reservasi[nama]:
            if reservasi_item["tanggal"] == tanggal:
                jam_mulai_reservasi = reservasi_item["jam_mulai"]
                jam_selesai_reservasi = reservasi_item["jam_selesai"]
                
                if (jam_mulai < jam_selesai_reservasi and jam_selesai > jam_mulai_reservasi):
                    print(f"Lapangan {nama} sudah dipesan pada tanggal {tanggal} dari jam {jam_mulai_reservasi:.2f} sampai {jam_selesai_reservasi:.2f}. Silakan pilih waktu lain.")
                    return

        durasi = jam_selesai - jam_mulai
        total_harga = durasi * int(lapangan[nama]["harga"])

        reservasi[nama].append({
            "pemesan": nama_pemesan, 
            "tanggal": tanggal, 
            "jam_mulai": jam_mulai, 
            "jam_selesai": jam_selesai, 
            "password": password
        })
        print(f"Lapangan {nama} berhasil dipesan oleh {nama_pemesan} pada tanggal {tanggal} dari jam {jam_mulai:.2f} sampai {jam_selesai:.2f}. Total harga: Rp{total_harga:,.0f}.")
    else:
        print(f"Lapangan {nama} tidak ditemukan.")

def lihat_reservasi():
    if any(reservasi.values()):
        print("\n==== DAFTAR RESERVASI ====")
        table = PrettyTable()
        table.field_names = ["Nama Lapangan", "Nama Pemesan", "Tanggal", "Jam Mulai", "Jam Selesai"]
        for lapangan_dipesan in reservasi:
            for reservasi_item in reservasi[lapangan_dipesan]:
                table.add_row([lapangan_dipesan, reservasi_item["pemesan"], reservasi_item["tanggal"], reservasi_item["jam_mulai"], reservasi_item["jam_selesai"]])
        print(table)
    else:
        print("Belum ada reservasi yang dilakukan.")0
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
137-198.
fungsi ini digunkan untuk reservasi lapangan nah ada input dari pengguna, seperti tanggal, jam mulai, jam selesai, password, dan nama pemesan. saat mulai saya memanggil function untuk melihat daftar lapangan biar enak inputnya. input pertama ada input nama lapangan yang ingin dipesan yg akan digunakan sebagai key untuk mengakses data dari 2 dictionary yaitu reservasi dan lapangan jika nama lapangan ada makan program akan lanjut untuk menginput tanggal pemesanan dengan format yyyy-mm-dd kemudian ada input float jam mulai dan jam selesai mereka ada try dan perkondisian untuk validasi dan security  agar nilai mereka berupa angka bukan 0 dan dibawahnya , jam selese harus lebih besar dari jam mulai,dan nilai nya tidak lebih besar dari 24 jika sarat terpenuhi maka ada input nama pemesan dan password untuk melengkapi proses reservasi. nah sebelum menyimpan reservasi sistem bakal memeriksa apakah sudah ada reservasi pada tanggal dan jam yang sama untuk lapangan itu jika ada bentrok maka reservasi gagal jaika tidak maka reservasi akan disimpan ke dictionary. disitu juga ada total harga yang dimana durasi yaitu (jam selesai - jam mulai) * harga.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def batalkan_reservasi():
    lihat_reservasi() 
    nama = input("Masukkan nama lapangan yang reservasinya ingin dibatalkan: ")
    if nama in reservasi:
        password = input("Masukkan password Anda: ")
        for reservasi_item in reservasi[nama]:
            if reservasi_item["password"] == password:
                reservasi[nama].remove(reservasi_item) 
                print(f"Reservasi untuk lapangan {nama} berhasil dibatalkan.")
                return
        print("Password salah Tidak dapat membatalkan reservasi.")
    else:
        print(f"Tidak ada reservasi untuk lapangan {nama}.")

login()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
200- 238.
fungsi ini diawalai dengan melihat resevervasi dengan memanggil function lalu kita input nama lapangan yang akan digunakan sebagai key jika nama lapangan ada maka kita akan diminta untuk menginput password dan jika password salah maka pembatalan reservasi tidak dapat dilakukan tapi kalo bener ya bakal kehapus 

240.
baris login() ini digunakan untuk memanggil function login yang dimana itu adalah awal dari sistem ini.
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        OUTPUT & INPUT PROGRAM
![{3C2ACA64-0023-4769-AEB1-F7BDD633B71C}](https://github.com/user-attachments/assets/b75f7d30-840b-4297-9fda-357670a9e2c3)
![{9E537557-829E-4851-9A1E-858B7F033892}](https://github.com/user-attachments/assets/0812a3e7-c379-417d-9f81-6045c22e2e2a)
tampilan menu dari login dan admin lalu fitur crud lapangan
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![{5CE81159-78AA-44B2-8FA3-521A18D63A84}](https://github.com/user-attachments/assets/88c51b13-5c82-4fa6-8861-168a5aff38cc)
![{60AFC109-6AE0-4872-ADF2-9E3335126232}](https://github.com/user-attachments/assets/3573e000-1e4c-4c74-b1b2-ffe5f6f64b59)
tampilan menu dari user dan fitur crd reservasi 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




