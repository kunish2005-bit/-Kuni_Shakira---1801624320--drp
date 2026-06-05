from tools import display_menu, Select_menu
from fitur_belajar import hitung_durasi_belajar
from fitur_produktivitas import cari_hari_produktif_belajar
from fitur_evaluasi import evaluasi_kebiasaan_belajar

if __name__ == '__main__':
    print('=============================')
    print('Selamat Datang di StudiO📒')
    print('Aplikasi Study Tracker Kesayangan Anda!❤️')

    nama = input("Masukkan nama Anda: ")

    print(f"\nSelamat Datang, {nama}!")

    while True:
        display_menu()
        menu = input("Pilih menu: ")
        if Select_menu(menu):
            break
        elif menu == '1':
            hitung_durasi_belajar()
        elif menu == '2':
            cari_hari_produktif_belajar()
        elif menu == '3':
            evaluasi_kebiasaan_belajar()

            menu = input("Apakah Anda ingin kembali ke menu utama? (nama): ")


            is_done = Select_menu(menu=menu)
            if is_done:
                break
