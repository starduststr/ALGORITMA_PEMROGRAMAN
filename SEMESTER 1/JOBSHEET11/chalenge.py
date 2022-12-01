def menu():
    menu = ['Ayam Geprek','Ayam Penyet', 'Nasi Goreng', 'Nasi Briyani', 'Jus Alpukat', 'Jus Jeruk']

    while True:
        print('\n\nMenu pilhan : ')
        print('--------------------------------')

        count = 1
        for data in menu:
            print('{}. {}'.format(count, data))
            count+=1
        print('0. Keluar')

        pilih_menu = eval(input('\nPilihan anda : '))

        print('\nMenu yang anda pilih adalah : {}'.format(menu[pilih_menu-1]))

        return menu[pilih_menu-1]

def main():
    data_pilih = []
    repeat = 1

    while True:

        data_pilih.append(menu())
        repeat = input('\nApakah anda mau memilih pesanan lagi (Y/N) : ')

        if repeat == 'n' or repeat == 'N' or repeat == 0:
            print('\n\nPesanan anda : ')
        
            for hasil in data_pilih:
                print(hasil)
                
            print('\nTerima kasih atas pesanannya.')

            break
            

main()