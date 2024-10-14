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

def hapus_lapangan():
    lihat_lapangan()
    nama = input("Masukkan nama lapangan yang ingin dihapus: ")
    if nama in lapangan:
        del lapangan[nama]
        del reservasi[nama] 
        print(f"Lapangan {nama} berhasil dihapus")
    else:
        print(f"Lapangan {nama} tidak ditemukan.")

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
        print("Belum ada reservasi yang dilakukan.")

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
