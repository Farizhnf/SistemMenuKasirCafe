#Ucapan Welcome to Projek kami
print("")
print("======================================================================")
print("                    Selamat Datang Di Coffee Life")
print("======================================================================")
print("")

# Menggunakan Append agar bisa Membuat list
produk = []
harga = []
Total = 0

def ulang():
    # Memakai Global Agar Bisa Mengambil Variable diluar Function
    global Total
    print("                Silahkan Pilih Menu Minuman & Makanan ")
    print("----------------------------------------------------------------------")
    print(" 1.Coffee")
    print(" 2.NonCoffee")
    print(" 3.Makanan & Cemilan   ")
    print("")
    print("Lanjut Ke Kasir? Ketik [y]")
    kode = input("Masukan Kode Kategori Produk [1][2][3] : ")
    print("----------------------------------------------------------------------")
    print("\n")
    if kode == "y":
        print("----------------------------------------------------------------------")
        print("Keranjang Anda Saat Ini              :", produk)
        print("Masing-Masing Harga Makanan/Minuman  :", harga)
        print("Total Yang harus dibayar             :", Total)
        print("")
        print("Apakah Anda Ingin Membayar nya?")
        kasir = input("ketik [y] Lanjut pembayaran, ketik [n] Balik ke menu : ")
        print("----------------------------------------------------------------------")
        if kasir == "y" or kasir == "ya" or kasir == "Y" :
            def Kurang():
                print("Total Anda Saat Ini                                   : Rp.",Total)
                bayar = int(input("Masukan Nominal Yang Akan Anda bayar                  : Rp. "))
                if bayar > Total:
                    kembalian = bayar - Total
                    print("Kembalian Anda                                        : Rp.",kembalian)
                    print("======================================================================")
                    print("               Terima kasih Sudah Berbelanja Disini :)")
                    print("======================================================================")
                    exit()
                elif bayar == Total:
                    print("Kembalian Anda                                        : 0")
                    print("")
                    print("======================================================================")
                    print("         Terima kasih Sudah Berbelanja Disini, Uang Anda Pas")
                    print("======================================================================")
                    exit()
                else:
                    print("Mohon Maaf, Uang anda Kurang         :")
                    Kurang()
        elif kasir == "n":
            ulang()
        else:
            ulang()

        Kurang()

    if kode == "1":
        print("                             Menu Coffee    ")
        print("----------------------------------------------------------------------")
        print(" 1.Coffee Cappucino")
        print("     Harga : Rp.20.000")
        print("")
        print(" 2.Coffee Americano")
        print("     Harga : Rp.18.000")
        print("")
        print(" 3.Coffee Macchiato")
        print("     Harga : Rp.22.000")
        print("")
        print(" 4.Coffee Moccacino")
        print("     Harga : Rp.20.000")
        print("----------------------------------------------------------------------")
        print("Balik Ke Menu Kategori?, Ketik [ya/y]")
        kodeprot = input("Masukan Kode Yang Akan Dibeli [1][2][3][4] : ")
        print("\n")
        if kodeprot == "1":
            produk.append("Coffee Cappucino")
            harga.append(20000)
            Total += 20000
            ulang()
        elif kodeprot == "2":
            produk.append("Coffee Americano")
            harga.append(18000)
            Total += 18000
            ulang()
        elif kodeprot == "3":
            produk.append("Coffee Macchiato")
            harga.append(22000)
            Total += 22000
            ulang()
        elif kodeprot == "4":
            produk.append("Coffee Moccacinno")
            harga.append(20000)
            Total += 20000
            ulang()
        elif kodeprot == "ya" or kodeprot == "y":
            ulang()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("         Kode Yang Anda Masukan Salah!, Coba Masukan Lagi")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            ulang()

    if kode == "2":
        print("                         Menu NonCoffee    ")
        print("----------------------------------------------------------------------")
        print(" 1.Ice Tea Lychee")
        print("     Harga : Rp.12.000")
        print("")
        print(" 2.Ice Tea Manggo")
        print("     Harga : Rp.12.000")
        print("")
        print(" 3.Ice/Hot Tea Jasmine")
        print("     Harga : Rp.10.000")
        print("")
        print(" 4.Air Mineral Botol 600ml")
        print("     Harga : Rp.5000")
        print("----------------------------------------------------------------------")
        print("Balik Ke Menu Kategori?, Ketik [ya/y]")
        kodeprot = input("Masukan Kode Yang Akan Dibeli [1][2][3][4] : ")
        print("\n")
        if kodeprot == "1":
            produk.append("Ice Tea Lychee")
            harga.append(12000)
            Total += 12000
            ulang()
        elif kodeprot == "2":
            produk.append("Ice Tea Manggo")
            harga.append(12000)
            Total += 12000
            ulang()
        elif kodeprot == "3":
            produk.append("Tea Jasmine")
            harga.append(10000)
            Total += 10000
            ulang()
        elif kodeprot == "4":
            produk.append("Air Mineral Botol 600ml")
            harga.append(5000)
            Total += 5000
            ulang()
        elif kodeprot == "ya" or kodeprot == "y":
            ulang()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("         Kode Yang Anda Masukan Salah!, Coba Masukan Lagi")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            ulang()

    if kode == "3":
        print("                        Menu Makanan/Cemilan    ")
        print("----------------------------------------------------------------------")
        print(" 1.Croffle (3pcs)")
        print("     Harga : Rp.15.000")
        print("")
        print(" 2.Roti Bakar")
        print("     Harga : Rp.12.000")
        print("")
        print(" 3.Indomie Kuah + Telur")
        print("     Harga : Rp.12.000")
        print("")
        print(" 4.Cookies")
        print("     Harga : Rp.7000")
        print("----------------------------------------------------------------------")
        print("Balik Ke Menu Kategori?, Ketik [ya/y]")
        kodeprot = input("Masukan Kode Yang Akan Dibeli [1][2][3][4] : ")
        print("\n")
        if kodeprot == "1":
            produk.append("Croffle")
            harga.append(15000)
            Total += 15000
            ulang()
        elif kodeprot == "2":
            produk.append("Roti Bakar")
            harga.append(12000)
            Total += 12000
            ulang()
        elif kodeprot == "3":
            produk.append("Indomie + Telur")
            harga.append(12000)
            Total += 12000
            ulang()
        elif kodeprot == "4":
            produk.append("Cookies")
            harga.append(7000)
            Total += 7000
            ulang()
        elif kodeprot == "ya" or kodeprot == "y":
            ulang()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("         Kode Yang Anda Masukan Salah!, Coba Masukan Lagi")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("")
            ulang()
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("         Kode Yang Anda Masukan Salah!, Coba Masukan Lagi")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        ulang()

ulang()
