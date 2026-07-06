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
    print("8. export data json")
    print("9. import data json")
    print("10. Keluar")

    pilihan = input("pilih menu (1-10): ")
    
    if pilihan == "1":
        print("Menu Tambah sesi belajar")
    elif pilihan == "2":
        print("Menu Lihat riwayat belajar")
    elif pilihan == "3":
        print("Menu Update sesi belajar")
    elif pilihan == "4":
        print("Menu Hapus sesi belajar")
    elif pilihan == "5":
        print("Menu Total durasi belajar")
    elif pilihan == "6":
        print("Menu Hari paling produktif")
    elif pilihan == "7":
        print("Menu Lihat evaluasi belajar")
    elif pilihan == "8":
        export_json()
    elif pilihan == "9":
        import_json()
    elif pilihan == "10":
        print("Terima kasih telah menggunakan StudiO")
        break

    else:
        print("Pilihan tidak valid. Silahkan coba lagi")