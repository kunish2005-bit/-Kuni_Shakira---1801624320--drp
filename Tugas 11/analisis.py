import sqlite3

def hitung_jumlah_sesi():

    conn = sqlite3.connect("StudiO.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM StudiO")

    hasil = cursor.fetchone()[0]

    print(f"\nJumlah sesi belajar: {hasil}")

    conn.close()

def rata_rata_durasi():

    conn = sqlite3.connect("StudiO.db")
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(durasi) FROM study")

    hasil = cursor.fetchone()[0]

    print(f"Rata-rata durasi belajar : {hasil:.2f} menit")

    conn.close()