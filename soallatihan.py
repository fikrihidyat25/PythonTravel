asal = ""
tujuan = ""
jumlah_orang = 0
nama = ""
hargaHotel = 0
harga_satuan = 0
pilih_hotel = ""
total_kamar = 0
totalHari = 0
kelas = ""
total_harga = 0


def menu():
    print("TRAVEL & PESANAN HOTEL")


def transaksi():
    global asal, tujuan, jumlah_orang, nama, harga_satuan, harga, pilih_hotel, hargaHotel, totalHari, hargaSatuanhotel
    harga_satuan = 0
    print("Silahkan masukan informasi")
    nama = input("Nama : ")
    asal = input("Asal : ")
    tujuan = input("Tujuan : ")
    jumlah_orang = int(input("Jumlah Orang : "))

    if asal == "padang" and tujuan == "bukittinggi":
        harga_satuan = 1000000
    elif asal == "padang" and tujuan == "pariaman":
        harga_satuan = 500000
    elif asal == "padang" and tujuan == "solok":
        harga_satuan = 750000
    elif asal == "padang" and tujuan == "medan":
        harga_satuan = 1500000
    elif asal == "padang" and tujuan == "pekanbaru":
        harga_satuan = 1250000
    elif asal == "padang" and tujuan == "dumai":
        harga_satuan = 1000000

    harga_satuan = jumlah_orang * harga_satuan

    pilih_hotel = input("Mau pesan hotel? (y/n)")
    if pilih_hotel == "y" or pilih_hotel == "Y":
        hotel()
        transaksihotel()
        total_harga = jumlah_orang * harga_satuan + hargaHotel
    elif pilih_hotel == "n" or pilih_hotel == "N":
        total_harga = jumlah_orang * harga_satuan
        # print("Transaksi dibatalkan")


def hotel():
    print("Kelas Penginapan")
    print("1.kelas 1")
    print("2.kelas 2")
    print("3.kelas 3")


def transaksihotel():
    global totalHari, kelas, total_kamar, harga_satuan, hargaHotel

    kelas = int(input("pilih kelas :"))
    totalHari = int(input("jumlah hari :"))
    total_kamar = int(input("jumlah kamar :"))
    if kelas == 1:
        hargaSatuanhotel = 1000000
    elif kelas == 2:
        hargaSatuanhotel = 750000
    elif kelas == 3:
        hargaSatuanhotel = 500000

    hargaHotel = hargaSatuanhotel * total_kamar * totalHari


def tampilDetail():
    global asal, tujuan, jumlah_orang, harga_satuan, pilih_hotel, kelas, total_kamar, totalHari, total_harga
    if pilih_hotel == "n" or pilih_hotel == "N":
        print("")
        print("    ADMINISTRASI     ")
        print("")
        print("nama :", nama)
        print("Asal :", asal)
        print("Tujuan :", tujuan)
        print("Jumlah orang :", jumlah_orang)
        print("Total Harga Pesanan Kursi :", harga_satuan)
    elif  pilih_hotel == "y" or pilih_hotel == "Y" :
      print("")
      print("    ADMINISTRASI     ")
      print("")
      print("nama :", nama)
      print("Asal :", asal)
      print("Tujuan :", tujuan)
      print("Jumlah orang :", jumlah_orang)
      print("Total Harga Pesanan Kursi :", harga_satuan)
      print("Jenis hotel :", kelas)
      print("Jumlah kamar :", total_kamar)
      print("Total Hari :", totalHari)


def total():
    global jumlah_orang, harga_satuan, hargaHotel
    total_harga = harga_satuan + hargaHotel
    print("")
    print("===== TOTAL BIAYA ====="
          )
    print("Total pembayaran : Rp", total_harga)


def cetakStruk():
    global asal, tujuan, jumlah_orang, harga_satuan, pilih_hotel, kelas, total_kamar, totalHari, total_harga
    print("")
    cetakStruk = input("cetak struk?(y/n)")
    if pilih_hotel == "y" or pilih_hotel == "Y":
        print("")
        print("===== STRUK PEMBAYARAN =====")
        print("Nama :", nama)
        print("Asal :", asal)
        print("Tujuan :", tujuan)
        print("Jumlah kursi :", jumlah_orang)
        print("Total Harga Pesanan Kursi :", harga_satuan)
        print("")
        print("===== STRUK PESANAN HOTEL =====")
        print("")
        print("Jenis hotel:", kelas)
        print("Jumlah kamar:", total_kamar)
        print("Total Hari :", totalHari)
        print("Total harga penginapan Pesanan Hotel :", hargaHotel)
        print("")
        print("===== TOTAL =====")
        print("Total pembayaran :", harga_satuan + hargaHotel)
    elif pilih_hotel == "n" or pilih_hotel == "N":
        print("===== STRUK PEMBAYARAN =====")
        print("Nama :", nama)
        print("Asal :", asal)
        print("Tujuan :", tujuan)
        print("Jumlah kursi :", jumlah_orang)
        print("Total Harga Pesanan Kursi :", harga_satuan)
        print("===== TOTAL =====")
        print("Total pembayaran :", harga_satuan)
        print("")
        

menu()
transaksi()
tampilDetail()
total()
cetakStruk()
