def pemanggil(x1=0, x2=0, x3=0):
    # nilai_prediksi = [10,9,8,9,2,9,3,4]
    # nilai_yang_diharapkan = [8,9,2,5,4,2,3,4,8]

    nilai_prediksi = x1
    nilai_yang_diharapkan = x2

    return nilai_prediksi, nilai_yang_diharapkan

def backPropogation(y1=0, y2=0 ,y3=0):
    nilai_prediksi, nilai_yang_diharapkan = pemanggil([4,4,5,6,4,3,2,8], [4,5,6,7,8,9,10,11])

    hasil = []
    balance = 0

    for x in range(len(nilai_prediksi)):
    
        Error = nilai_prediksi[x] - nilai_yang_diharapkan[x]
        
        hasil.append(Error)
    for data in range(len(hasil)):
        balance -= hasil[data]
    
    t = """Hasil nilai prediksi - nilai yang diharapkan : {}
Balance : {}""".format(hasil, balance)

    fileOut = open('output.txt', 'w')
    fileOut.write(str(t))
    return balance

backPropogation()