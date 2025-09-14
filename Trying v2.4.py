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
# ini adalah list untuk menyimpan detail semua buku yang dipinjam
daftarBuku = []

# fungsi untuk menghitung biaya peminjaman satu buku
def biayaPeminjaman(jumlahHari):
    #biaya peminjaman buku dihitung dari jumlah hari peminjaman buku yang di berikan oleh user kemudian dikalikan dengan variabel biaya perhari, yaitu 5000 per hari
    biaya = int(jumlahHari) * biayaPerHari
    #mengembalikan hasil perhitungan biaya
    return biaya

# Loop utama untuk validasi input awal dari pengguna (nama dan jumlah buku)
while True:
    #dibawah adalah perintah pada user untuk menginput namanya
    inputNamaPeminjam = input("Nama Peminjam: ")
    #1. dibawah adalah perintah pada user untuk memasukan jumlah buku yang ingin dipinjam
    try:
        jumlahBuku = int(input("Jumlah buku yang dipinjam: "))
    except ValueError:
        print("\n=== Input harus berupa angka ===\n")
        continue
    #dibawah ini adalah untuk memvalidasi bahwa pengguna tidak memasukan angka negatif untuk jumlah buku yang ingin dipinjam
    if jumlahBuku <= 0:
        #jika pengguna memasukan angka negatif maka akan muncul pesan seperti ini "=== input tidak valid ===" di terminal dan terminal akan mengulangi untuk menginput nama dan jumlah buku yang dipinjam
        print("\n=== Input tidak valid, jumlah buku harus > 0 ===\n")
    else:
        break

# loop untuk mendata setiap buku yang dipinjam
    #ini digunakan untuk mendata satu per satu buku yang dipinjam pengguna
for buku in range(jumlahBuku):
    #Loop ini akan terus meminta input untuk satu buku sampai data yang dimasukkan valid
    while True:
        #dibawah ini adalah perintah untuk menampilkan buku ke berapa yang di data
        print(f"\n=== Buku {buku + 1} ===\n")
        #memerintahkan pengguna untuk memasukan judul buku yang dipinjam
        inputJudulBuku = input("Judul buku: ")

        try:
            #memerintahkan pengguna untuk memasukan berapa hari buku yang dipinjam
            inputJumlahHari = int(input("Hari: "))
        except ValueError:
            print("\n=== Input hari harus berupa angka ===\n")
            continue

        #ini adalah perintah untuk mengecek kondisi dari input pengguna, yaitu:
        #pengecekan apakah lama pengguna meminjam buku melebihi batas waktu yang sudah ditentukan atau tidak
        if inputJumlahHari > hariMaksimum:
            #jika pengguna ingin meminjam lebih dari hari yang ditentukan, maka akan muncul peringatan seperti ini
            print("\n\n=== PERINGATAN ===\nMaksimal peminjaman hanya 30 hari")
        elif inputJumlahHari <= 0:
            print("\n\n=== ERROR ===\nLama peminjaman harus lebih dari 0 hari")
        #ini adalah perintah yang akan dijalankan bila kondisi sebelumnya tidak ada yang terpenuhi
        else:
            #ini adalah variabel yang berisi biaya 1 buku yang dipinjam. variabel ini mendapat nilainya dengan mengambil fungsi yang bernama "biayaPeminjaman" yang telah megngitung biaya peminjaman nya sesuai hari yang diinginkan pengguna
            biayaBukuIni = biayaPeminjaman(inputJumlahHari)
            #Menambahkan 1 ke total buku yang berhasil didata. Variabel ini digunakan untuk rekap di akhir.
            jumlahBukuDipinjam += 1
            #menambahkan biaya buku saat ini ke total biaya keseluruhan
            totalBiaya += biayaBukuIni
            # simpan detail buku dalam list
            daftarBuku.append((inputJudulBuku, inputJumlahHari, biayaBukuIni))
            #perintah untuk menghentikan perintah while loop
            break

# ringkasan total pembayaran berisikan nama peminjam, jumlah buku
print(f"\n=== Nota Peminjaman ===\n")
print(f"Nama Peminjam  : {inputNamaPeminjam}")
print(f"Jumlah Buku    : {jumlahBukuDipinjam}")
print("\n--- Detail Buku ---")

# menampilakn detail buku dari judul, hari, serta biaya
for i, (judul, hari, biaya) in enumerate(daftarBuku, start=1):
    print(f"{i}. Judul: {judul} | Lama Pinjam: {hari} hari | Biaya: Rp{biaya}")

# menampilkan total keseluruhan biaya yang perlu dibayar
print("\n--- Ringkasan ---")
print(f"Total Biaya    : Rp{totalBiaya}")