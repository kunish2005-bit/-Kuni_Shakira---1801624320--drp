while True:
    print("\n===== StudiO ======")
    print("1. Tambah sesi belajar")
    print("2. Lihat riwayat belajar")
    print("3. Update sesi belajar")
    print("4. Hapus sesi belajar")
    print("5. Total durasi belajar")
    print("6. Hari paling produktif")
    print("7. Lihat evaluasi belajar")
    print("8. Keluar")

    pilihan = input("pilih menu (1-8): ")
    
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
        print("Terima kasih telah menggunakan StudiO")
        break

    else:
        print("Pilihan tidak valid. Silahkan coba lagi")