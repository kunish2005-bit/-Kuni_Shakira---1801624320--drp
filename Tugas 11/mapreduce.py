import json
import os 
from functools import reduce

folder = os.path.dirname(__file__)
file_json = os.path.join(folder, "StudiO_dummy.json")

with open(file_json, "r") as file:
    data = json.load(file)
[
 {
   "tanggal":"2026-07-01",
   "mata_kuliah":"Python",
   "durasi":60,
   "evaluasi":"Baik"
 },
 {
   "tanggal":"2026-07-02",
   "mata_kuliah":"Statistika",
   "durasi":90,
   "evaluasi":"Sangat Baik"
 }
]
durasi = list(map(lambda item: item["durasi"], data))
total_durasi = reduce(lambda a, b: a + b, durasi)
rata_rata = total_durasi / len(durasi)
print("===== HASIL MAPREDUCE =====")
print(f"Total Durasi : {total_durasi} menit")
print(f"Rata-rata Durasi : {rata_rata:.2f} menit")
