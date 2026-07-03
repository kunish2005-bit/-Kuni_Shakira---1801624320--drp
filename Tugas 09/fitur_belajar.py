def hitung_durasi_belajar():
    """Fitur untuk menghitung durasi belajar berdasarkan input waktu mulai dan waktu selesai"""
    print("\n=== Hitung Durasi Belajar ===")
    try:
        waktu_mulai = input("Masukkan waktu mulai belajar (HH:MM, 24 jam): ")
        waktu_selesai = input("Masukkan waktu selesai belajar (HH:MM, 24 jam): ")

        # Validasi format waktu
        if len(waktu_mulai) != 5 or len(waktu_selesai) != 5 or waktu_mulai[2] != ':' or waktu_selesai[2] != ':':
            raise ValueError("Format waktu harus HH:MM")

        jam_mulai, menit_mulai = map(int, waktu_mulai.split(':'))
        jam_selesai, menit_selesai = map(int, waktu_selesai.split(':'))

        # Validasi nilai jam dan menit
        if not (0 <= jam_mulai < 24 and 0 <= menit_mulai < 60 and 0 <= jam_selesai < 24 and 0 <= menit_selesai < 60):
            raise ValueError("Jam harus antara 00-23 dan menit harus antara 00-59")

        # Hitung durasi dalam menit
        total_mulai = jam_mulai * 60 + menit_mulai
        total_selesai = jam_selesai * 60 + menit_selesai

        if total_selesai < total_mulai:
            raise ValueError("Waktu selesai harus lebih besar dari waktu mulai")

        durasi_menit = total_selesai - total_mulai
        durasi_jam = durasi_menit // 60
        durasi_menit = durasi_menit % 60

        print(f"Durasi belajar Anda adalah {durasi_jam} jam dan {durasi_menit} menit.")
    except ValueError as e:
        print(f"Input tidak valid: {e}")
