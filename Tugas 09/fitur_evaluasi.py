def evaluasi_kebiasaan_belajar():
    """Fitur untuk mengevaluasi kebiasaan belajar"""
    print("================================")
    print("Fitur Evaluasi Kebiasaan Belajar")
    print("================================")

    try:
        jumlah_hari = int(input("Masukkan jumlah hari yang ingin Anda evaluasi: "))
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih besar dari 0")

        total_durasi = 0

        for i in range(1, jumlah_hari + 1):
            durasi = int(input(f"Masukkan durasi belajar pada hari ke-{i} (dalam menit): "))
            if durasi < 0:
                raise ValueError("Durasi tidak boleh negatif")

            total_durasi += durasi

        rata_rata_durasi = total_durasi / jumlah_hari
        print(f"Rata-rata durasi belajar Anda adalah {rata_rata_durasi:.2f} menit per hari.")
    except ValueError as e:
        print(f"Input tidak valid: {e}")
