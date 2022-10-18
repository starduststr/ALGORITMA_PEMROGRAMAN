def main():
    namaBulan = ['Januari', 'Februari', 'Maret',
            'April', 'Mei', 'Juni', 'Juli', 'Agustus',
            'September', 'Oktober', 'November', 'Desember']

    inputTanggal = input('Enter a date(mm/dd/yyyy): ')

    hasilInput = inputTanggal.split('/')
    bulan = int(hasilInput[0])
    tanggal = hasilInput[1]
    tahun = hasilInput[2]

    if len(inputTanggal) < 10 or len(inputTanggal) > 10:
        print('Format tanggal tidak sesuai') 
    else :
        if int(bulan)-1 > 12 or int(bulan)-1 < 0:
            bulan = 'Bulan tidak tersedia'
        else :
            bulan = namaBulan[bulan-1]
        
        print('The converted date is: {} {}, {}'.format(bulan, tanggal, tahun))

main()