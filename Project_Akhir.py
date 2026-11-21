from collections import deque

## Data kendaraan ##

kendaraan = [
    {"kode": 1, "nama": "Sepeda BMX", "tarif": 1000, "stok": 50},
    {"kode": 2, "nama": "Sepeda Motor Vario", "tarif": 2000, "stok": 200},
    {"kode": 3, "nama": "Mobil AUDI", "tarif": 5000, "stok": 60},
    {"kode": 4, "nama": "Minibus", "tarif": 10000, "stok": 5},
    {"kode": 5, "nama": "Truck Material", "tarif": 15000, "stok": 3}
    
]

riwayat = []
stack_undo = []
antrean = deque()
## ENDING DARI FITUR DAFTAR KENDARAAN ##
########################################
## FUNGSI Daftar Parkir ##

def tampil_daftar():
    print("\n========== DAFTAR PARKIR ==========")
    print(f"{'Kode':<8}{'Kendaraan':<20}{'Tarif/Jam':<15}{'Stok'}")
    print("-" * 55)

    for item in kendaraan:
        print(
            f"{item['kode']:<8}"
            f"{item['nama']:<20}"
            f"Rp {item['tarif']:<12,}"
            f"{item['stok']}"
        )

    print("=" * 55)
## ENDING CODE DARI FUNGSI DAFTAR PARKIR ##
###########################################
## FUNGSI Transaksi Parkir ##

def transaksi_parkir():
    print("\n========== TRANSAKSI PARKIR ==========")

    pemilik = input("Nama: ")

    while pemilik.strip() == "":
        print("Nama atau plat tidak boleh kosong!")
        pemilik = input("Nama: ")

    while True:
        try:
            kode = int(input("Masukkan kode kendaraan (1-5): "))

            if 1 <= kode <= 5:
                break
            else:
                print("Kode harus antara 1 sampai 5!")

        except ValueError:
            print("Input harus berupa angka!")

    kendaraan_pilih = None

    for item in kendaraan:
        if item["kode"] == kode:
            kendaraan_pilih = item
            break

    print(f"Kendaraan dipilih: {kendaraan_pilih['nama']}")
    print(f"Stok tersedia: {kendaraan_pilih['stok']}")

    if kendaraan_pilih["stok"] <= 0:
        print("Maaf, stok kendaraan sudah habis.")
        return

    while True:
        try:
            jumlah = int(input("Jumlah kendaraan: "))

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
            elif jumlah > kendaraan_pilih["stok"]:
                print("Jumlah melebihi stok tersedia!")
            else:
                break

        except ValueError:
            print("Input harus berupa angka!")

    while True:
        try:
            jam = float(input("Lama parkir (jam): "))

            if jam <= 0:
                print("Lama parkir harus lebih dari 0!")
            else:
                break

        except ValueError:
            print("Input harus berupa angka!")

    tarif = kendaraan_pilih["tarif"]
    subtotal = round(tarif * jumlah * jam)

    if jam <= 2:
        total = subtotal
        keterangan = "Tarif normal"

    elif jam <= 8:
        total = round(subtotal * 0.8)
        keterangan = "Diskon 20%"

    else:
        total = subtotal + (20000 * jumlah)
        keterangan = "Tambahan biaya menginap"

    kendaraan_pilih["stok"] -= jumlah

    transaksi = {
        "pemilik": pemilik,
        "kode": kode,
        "nama": kendaraan_pilih["nama"],
        "jumlah": jumlah,
        "jam": jam,
        "subtotal": subtotal,
        "total": total
    }

    riwayat.append(transaksi)
    stack_undo.append(transaksi.copy())

## ENDING CODE DARI FUNGSI TRANSAKSI PARKIR ##
#############################################
## FUNGSI RIWAYAT TRANSAKSI ##

def tampil_riwayat():
    print("\n========== RIWAYAT TRANSAKSI ==========")

    if len(riwayat) == 0:
        print("Belum ada transaksi.")
        return

    print(f"{'No':<5}{'Pemilik/Plat':<18}{'Kendaraan':<18}{'Jumlah':<10}{'Total'}")
    print("-" * 70)

    for i, trx in enumerate(riwayat, start=1):
        print(
            f"{i:<5}"
            f"{trx['pemilik']:<18}"
            f"{trx['nama']:<18}"
            f"{trx['jumlah']:<10}"
            f"Rp {trx['total']:,}"
        )

    print("=" * 70)
## ENDING CODE DARI FUNGSI RIWAYAT TRANSAKSI ##
###############################################
## FUNGSI LAPORAN PARKIR ##

def tampil_laporan():
    print("\n========== LAPORAN PARKIR ==========")

    if len(riwayat) == 0:
        print("Belum ada transaksi untuk dilaporkan.")
        return

    pendapatan = 0

    for trx in riwayat:
        pendapatan += trx["total"]

    jumlah_transaksi = len(riwayat)
    rata_rata = pendapatan / jumlah_transaksi

    transaksi_terbesar = max(riwayat, key=lambda trx: trx["total"])

    parkir_menginap = 0

    for trx in riwayat:
        if trx["jam"] > 8:
            parkir_menginap += 1

    print(f"Total pendapatan       : Rp {pendapatan:,}")
    print(f"Jumlah transaksi       : {jumlah_transaksi}")
    print(f"Rata-rata transaksi    : Rp {rata_rata:,.0f}")
    print("-" * 40)
    print("TRANSAKSI TERBESAR")
    print(f"Pemilik/Plat           : {transaksi_terbesar['pemilik']}")
    print(f"Kendaraan              : {transaksi_terbesar['nama']}")
    print(f"Total                  : Rp {transaksi_terbesar['total']:,}")
    print("-" * 40)
    print(f"Parkir lebih dari 8 jam: {parkir_menginap}")
    print("=" * 40)
## ENDING CODE DARI FUNGSI LAPORAN PARKIR ##
############################################
## CODE UNTUK FUNGSI CARI DAN URUTKAN ##

def cari_kendaraan(nama_dicari):
    hasil = []

    for item in kendaraan:
        if nama_dicari.lower() in item["nama"].lower():
            hasil.append(item)

    return hasil


def urutkan_tarif():
    hasil = sorted(kendaraan, key=lambda item: item["tarif"])
    return hasil


def menu_cari_urutkan():
    print("\n========== CARI DAN URUTKAN ==========")
    print("1. Cari kendaraan berdasarkan nama")
    print("2. Urutkan kendaraan berdasarkan tarif")
    
    pilih = input("Pilih fitur: ")

    if pilih == "1":
        nama_dicari = input("Masukkan nama kendaraan: ")

        hasil = cari_kendaraan(nama_dicari)

        if len(hasil) > 0:
            print("\nKendaraan ditemukan:")
            print(f"{'Kode':<8}{'Nama':<20}{'Tarif/Jam':<15}{'Stok'}")
            print("-" * 55)

            for item in hasil:
                print(
                    f"{item['kode']:<8}"
                    f"{item['nama']:<20}"
                    f"Rp {item['tarif']:<12,}"
                    f"{item['stok']}"
                )
        else:
            print("Kendaraan tidak ditemukan!")

    elif pilih == "2":
        hasil = urutkan_tarif()

        print("\nDaftar kendaraan berdasarkan tarif:")
        print(f"{'Kode':<8}{'Nama':<20}{'Tarif/Jam':<15}{'Stok'}")
        print("-" * 55)

        for item in hasil:
            print(
                f"{item['kode']:<8}"
                f"{item['nama']:<20}"
                f"Rp {item['tarif']:<12,}"
                f"{item['stok']}"
            )

    else:
        print("Pilihan tidak valid!")
## ENDING CODE UNTUK FUNGSI CARI DAN URUTKAN ##
##############################################
## CODE STRUK PARKIR ##

while True:
    print("\n===== SISTEM PARKIR KAMPUS TEKNIK =====")
    print("1. Daftar Kendaraan")
    print("2. Transaksi Parkir")
    print("3. Riwayat Transaksi")
    print("4. Laporan Parkir")
    print("5. Cari dan Urutkan")
    print("6. Undo Transaksi")
    print("7. Antrean Parkir")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tampil_daftar()

    elif pilih == "2":
        transaksi_parkir()

    elif pilih == "3":
        tampil_riwayat()

    elif pilih == "4":
        tampil_laporan()

    elif pilih == "5":
        menu_cari_urutkan()

    elif pilih == "0":
        print("Terima kasih telah menggunakan sistem parkir Teknik.")
        break

    else:
        print("Pilihan tidak valid.")


