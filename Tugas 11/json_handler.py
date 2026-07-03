import sqlite3
import json

def export_json():
    
    conn = sqlite3.connect("StudiO.db")
    cursor = conn.cursor() 

    cursor.execute("SELECT * FROM studiO")
    data = cursor.fetchall()

    with open("study.json","w") as file:
        json.dump(data, file)

    conn.close()

    print("Data berhasil di export")

