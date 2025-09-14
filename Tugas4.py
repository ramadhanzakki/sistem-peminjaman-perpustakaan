'''
    Tugas Algoritma Pemrograman 2.9
    Kelompok 8 Offering TI-A:
    1. Muhammad Zakki Fitra Ramadhan
    2. Fadhlan Nashrullah Shiddiq
    3. Dzauq Bachrul Zakariya 'Ulum
'''

# perintah print dibawah ini berfungsi untuk menampilkan judul program ini pada terminal, yaitu sistem peminjaman pada perpustakaan
print("\n=== Sistem Peminjaman Perpustakaan ===\n")

# ini adalah variabel yang memuat biaya per hari peminjaman buku
biayaPerHari = 5000
# ini adalah variabel yang memuat berapa hari maksimal peminjaman buku
hariMaksimum = 30
# ini adalah variabel yang berisi total biaya yang nantinya akan digunakan unutk menghitung total biaya peminjaman buku jika buku yang dipinjam lebih dari satu
totalBiaya = 0
# ini adalah variabel yang menampilkan berapa buku yang di pinjam. isi variable ini akan berubah isinya sesuai jumlah buku yang dipinjam
jumlahBukuDipinjam = 0
# variabel ini berisi jumlah maksimal buku yang dipinjam, yaitu 3 buku saja
jumlahBukuMaksimal = 3


#ini adalah fungsi untuk menghitung biaya peminjaman satu buku
def biayaPeminjaman(jumlahHari):
    #biaya peminjaman buku dihitung dari jumlah hari peminjaman buku yang di berikan oleh user kemudian dikalikan dengan variabel biaya perhari, yaitu 5000 per hari
    biaya = int(jumlahHari) * biayaPerHari
    #mengembalikan hasil perhitungan biaya
    return biaya

#Loop utama untuk validasi input awal dari pengguna (nama dan jumlah buku)
while True:
    #dibawah adalah perintah pada user untuk menginput namanya
    inputNamaPeminjam = input("Nama Peminjam: ")
    #dibawah adalah perintah pada user untuk memasukan jumlah buku yang ingin dipinjam
    jumlahBuku = int(input("Jumlah buku yang dipinjam: "))
    #ini adalah perintah untuk mengecek kondisi dari input pengguna, yaitu:
    #1. dibawah ini adalah untuk memvalidasi bahwa pengguna tidak memasukan angka negatif untuk jumlah buku yang ingin dipinjam
    if jumlahBuku <= 0:
        #jika pengguna memasukan angka negatif maka akan muncul pesan seperti ini "=== input tidak valid ===" di terminal dan terminal akan mengulangi untuk menginput nama dan jumlah buku yang dipinjam
        print("\n=== input tidak valid ===\n")
    #2. dibawah ini adalah perintah untuk mengecek apakah jumlah buku yang dipinjam itu melebihi batas peminjaman atau tidak
    elif jumlahBuku > jumlahBukuMaksimal:
        #jika buku yang dipinjam melebihi batas peminjaman, maka akan muncul pesan seperti ini 
        '''
            === WARNING ===
            maksimal peminjaman buku hanya 3
        '''
        #kemudian mengulangi loop
        print("\n=== WARNING ===\n\nmaksimal peminjaman buku hanya 3")
    #dibawah ini adalah perintah jika kedua kondisi diatas tidak terpenuhi
    else:
        #ini akan menghentikan while loop dan melanjutkan ke proses selanjutnya
        break


#ini adalah perintah loop yang akan terus mengulang sesuai jumlah buku yang dipinjam pengguna. ini digunakan untuk mendata satu per satu buku yang dipinjam pengguna
for buku in range(jumlahBuku):
    #Loop ini akan terus meminta input untuk satu buku sampai data yang dimasukkan valid
    while True:
        #dibawah ini adalah perintah untuk menampilkan buku ke berapa yang di data
        print(f"\n=== Buku {buku + 1} ===\n")
        #memerintahkan pengguna untuk memasukan judul buku yang dipinjam
        inputJudulBuku = input("Judul buku: ")
        #memerintahkan pengguna untuk memasukan berapa hari buku yang dipinjam
        inputJumlahHari = int(input("Hari: "))
        #ini adalah perintah untuk mengecek kondisi dari input pengguna, yaitu:
        #dibawah adalah perintah untuk mengecek apakah lama pengguna meminjam buku melebihi batas waktu yang ditentukan atau tidak
        if inputJumlahHari > hariMaksimum:
            #jika pengguna ingin meminjam lebih dari hari yang ditentukan, maka akan muncul peringatan seperti ini
            '''
                === PERINGATAN ===
                Maksimal peminjaman hanya 30 hari
            '''
            print("\n\n=== PERINGATAN ===\n\nMaksimal peminjaman hanya 30 hari")
        #ini adalah perintah yang akan dijalankan bila kondisi sebelumnya tidak ada yang terpenuhi
        else:
            #ini adalah variabel yang berisi biaya 1 buku yang dipinjam. variabel ini mendapat nilainya dengan mengambil fungsi yang bernama "biayaPeminjaman" yang telah megngitung biaya peminjaman nya sesuai hari yang diinginkan pengguna
            biayaBukuIni = biayaPeminjaman(inputJumlahHari)
            #Menambahkan 1 ke total buku yang berhasil didata. Variabel ini digunakan untuk rekap di akhir.
            jumlahBukuDipinjam += 1
            #menambahkan biaya buku saat ini ke total biaya keseluruhan
            totalBiaya += biayaBukuIni
            #perintah untuk menghentikan perintah while loop
            break

#ringkasan total pembayaran
#perintah untuk menampilkan "=== Total Pembayaran ==="
print(f"\n=== Total Pembayaran ===\n")
#merupakan nota akhir yang berisi nama peminjam, jumlah total buku yang dipinjam, dan total biaya peminjaman
print(f"Nama : {inputNamaPeminjam} Jumlah buku yang dipinjam : {jumlahBukuDipinjam} Total harga : {totalBiaya}")
