def display_menu():
    print('=======================')
    print('Selamat Datang di StudiO!')
    print('1. Durasi belajar Anda⏱️')
    print('2. Hari paling produktif Anda🏃‍♂️‍➡️')
    print('3. Evaluasi kebiasaan belajar Anda⚙️')
    print('4. Selesai✅')
    print('=======================')

def Select_menu(menu):
    if menu == '1':
        print('Anda memilih menu durasi belajar')
    elif menu == '2':
        print('Anda memilih menu hari paling produktif')
    elif menu == '3':
        print('Anda memilih menu evaluasi kebiasaan belajar')
    elif menu == '4':
        print('===========================')
        print('Terima Kasih telah menggunakan StudiO!')
        print('Semoga kegiatan belajar Anda tetap produktif ya!')
        return True
    else:
        print('menu tidak valid')
    return False  


