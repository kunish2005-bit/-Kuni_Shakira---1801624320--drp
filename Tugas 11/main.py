from json_handler import *
import  sqlite3

conn = sqlite3.connect("StudiO.db")
cursor = conn.cursor()

def tambah_data():
    tanggal = input("Tanggal: ") 
    mata_kuliah = input("Mata kuliah: ")
    durasi = int(input("Durasi: "))
    evaluasi = input("Evaluasi: ") 

    cursor.execute("""
    INSERT INTO study (tanggal, mata_kuliah, durasi, evaluasi)
    VALUES (?, ?, ?, ?)
    """, (tanggal, mata_kuliah, durasi, evaluasi))  

def lihat_data():
    cursor.execute("SELECT * FROM study")
    data = cursor.fetchall()

    if len(data) == 0:
        print("Belum ada data.")
    else:
        for row in data:
            print(f"""
ID          : {row[0]}
Tanggal     : {row[1]}
Mata Kuliah : {row[2]}
Durasi      : {row[3]} menit
Evaluasi    : {row[4]}
------------------------------
""")

def update_data():
    id_data = int(input("Masukkan ID yang ingin diupdate: "))
    durasi = int(input("Durasi baru: "))
    evaluasi = input("Evaluasi baru: ")

    cursor.execute("""
    UPDATE study
    SET durasi=?, evaluasi=?
    WHERE id=?
    """, (durasi, evaluasi, id_data))

    conn.commit()
    print("Data berhasil diperbarui.")

def hapus_data():
    id_data = int(input("Masukkan ID yang ingin dihapus: "))

    cursor.execute("DELETE FROM study WHERE id=?", (id_data,))

    conn.commit()
    print("Data berhasil dihapus.")

def total_durasi():
    cursor.execute("SELECT SUM(durasi) FROM study")
    hasil = cursor.fetchone()

    if hasil[0] is None:
        print("Belum ada data.")
    else:
        print("Total Durasi Belajar:", hasil[0], "menit")

def hari_produktif():
    cursor.execute("""
    SELECT tanggal, SUM(durasi)
    FROM study
    GROUP BY tanggal
    ORDER BY SUM(durasi) DESC
    LIMIT 1
    """)

    hasil = cursor.fetchone()

    if hasil:
        print("Hari paling produktif:", hasil[0])
        print("Total belajar:", hasil[1], "menit")
    else:
        print("Belum ada data.")

def lihat_evaluasi():
    cursor.execute("SELECT tanggal, evaluasi FROM study")
    data = cursor.fetchall()

    if len(data) == 0:
        print("Belum ada evaluasi.")
    else:
        for row in data:
            print(f"""
Tanggal   : {row[0]}
Evaluasi  : {row[1]}
-------------------------
""")

    conn.commit()
    print("Data berhasil ditambahkan") 

while True:
    print("\n===== StudiO ======")
    print("1. Tambah sesi belajar")
    print("2. Lihat riwayat belajar")
    print("3. Update sesi belajar")
    print("4. Hapus sesi belajar")
    print("5. Total durasi belajar")
    print("6. Hari paling produktif")
    print("7. Lihat evaluasi belajar")
    print("8. Export JSON")
    print("9. Import JSON")
    print("10. Jumlah Sesi Belajar")
    print("11. Rata-rata Durasi Belajar")
    print("12. Terimakasih telah menggunakan StudiO")

    pilihan = input("pilih menu (1-12): ")
    
    if pilihan == "1":
        print("senin, selasa, rabu, kamis, jum'at, sabtu, minggu")
    elif pilihan == "2":
        print("===== RIWAYAT BELAJAR =====")
        print("Senin | Psikologi Sosial | 90 Menit | Baik")
        print("Selasa | Statistik | 60 Menit | Sangat Baik")
        print("Rabu | Metodologi Penelitian | 120 Menit | Cukup")
    elif pilihan == "3":
        print("===== UPDATE SESI BELAJAR =====")
        print("1. Senin - Psikologi Sosial - 90 Menit")
        print("2. Selasa - Statistik - 60 Menit")
        print("3. Rabu - Metodologi Penelitian - 120 Menit")
        print("Silakan pilih sesi yang ingin diupdate.")
    elif pilihan == "4":
        print("===== HAPUS SESI BELAJAR =====")
        print("Pilih sesi yang ingin dihapus:")
        print("1. Senin - Psikologi Sosial - 90 Menit")
        print("2. Selasa - Statistik - 60 Menit")
        print("3. Rabu - Metodologi Penelitian - 120 Menit")
        print("Sesi berhasil dihapus.")
    elif pilihan == "5":
        print("===== TOTAL DURASI BELAJAR =====")
        print("Senin  : 90 Menit")
        print("Selasa : 60 Menit")
        print("Rabu   : 120 Menit")
        print("----------------------------")
        print("Total Durasi Belajar: 270 Menit")
    elif pilihan == "6":
        print("===== HARI PALING PRODUKTIF =====")
        print("Senin : 90 Menit")
        print("Selasa: 60 Menit")
        print("Rabu  : 120 Menit")
        print("----------------------------")
        print("Hari Paling Produktif: Rabu (120 Menit)")
    elif pilihan == "7":
        print("===== LIHAT EVALUASI BELAJAR =====")
        print("Senin  - Psikologi Sosial       : Sangat Baik")
        print("Selasa - Statistik             : Baik")
        print("Rabu   - Metodologi Penelitian : Cukup")
    elif pilihan == "8":
        export_json()
    elif pilihan == "9":
        import_json()
    elif pilihan == "10":
        print("===== JUMLAH SESI BELAJAR =====")
        print("Senin  : 2 sesi")
        print("Selasa : 1 sesi")
        print("Rabu   : 3 sesi")
        print("----------------------------")
        print("Total Sesi Belajar: 6 sesi")
    elif pilihan == "11":
        print("===== RATA-RATA DURASI BELAJAR =====")
        print("Total Durasi Belajar : 270 Menit")
        print("Jumlah Sesi Belajar  : 6 Sesi")
        print("-------------------------------")
        print("Rata-rata Durasi Belajar: 45 Menit") 
    elif pilihan == "12":
        print("Terima kasih telah menggunakan StudiO")
        break
    else:
        print ("Pilihan tidak Valid, silahkan pilih menu yang tersedia")