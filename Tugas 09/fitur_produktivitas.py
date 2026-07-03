def cari_hari_produktif_belajar():
    """Fitur untuk mencari hari produktif belajar"""
    print("================================")
    print("Fitur Hari Produktif Belajar")
    print("================================")


    try:
        jumlah_hari = int(input("Masukkan jumlah hari yang ingin Anda evaluasi: "))
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih besar dari 0")

        hari_produktif = None
        durasi_terlama = -1

        for i in range(1, jumlah_hari + 1):
            durasi = int(input(f"Masukkan durasi belajar pada hari ke-{i} (dalam menit): "))
            if durasi < 0:
                raise ValueError("Durasi tidak boleh negatif")

            if durasi > durasi_terlama:
                durasi_terlama = durasi
                hari_produktif = i

            print(f"Hari paling produktif belajar Anda adalah hari ke-{hari_produktif} dengan durasi {durasi_terlama} menit.")
            
    except ValueError as e:
            print(f"input tidak valid: {e}")
