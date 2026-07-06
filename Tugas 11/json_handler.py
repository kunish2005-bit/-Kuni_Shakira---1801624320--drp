import sqlite3
import json

def export_json():
    
    conn = sqlite3.connect("StudiO.db")
    cursor = conn.cursor() 
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studio (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kolom2 TEXT,
        kolom3 TEXT,
        kolom4 TEXT
    )
    """)
    conn.commit()  

    cursor.execute("SELECT * FROM studiO")
    data = cursor.fetchall()
    
    with open("study.json","w") as file:
        json.dump(data, file)

    conn.close()

    print("Data berhasil di export")

def import_json():
    conn = sqlite3.connect("studio.db")
    cursor = conn.cursor()
    
    with open("study.json", "r") as file:
        data = json.load(file)
        
    for item in data:
        cursor.execute(
            "INSERT INTO studio VALUES (?, ?, ?, ?)",
            tuple(item.values()) if isinstance(item, dict) else item
        )
        
    conn.commit()
    conn.close()
    
    print("Data berhasil di import")

