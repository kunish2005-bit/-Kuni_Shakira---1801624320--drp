import sqlite3
conn = sqlite3.connect("studiO .db")
cursor = conn.cursor()
cursor .execute("""
CREATE TABLE IF NOT EXISTS StudiO (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    tanggal TEXT NOT NULL ,
    mata_kuliah TEXT NOT NULL ,
    durasi INTEGER NOT NULL ,
    evaluasi TEXT
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat")