def pemanggil(x1=0, x2=0, x3=0):
    nilai_prediksi = x1
    nilai_yang_diharapkan = x2

    return nilai_prediksi, nilai_yang_diharapkan

def backPropogation(y1=0, y2=0 ,y3=0):
    nilai_prediksi, nilai_yang_diharapkan = pemanggil([10,9,8,9,2,9,3,4], [10,9,8,9,2,9,3,4])

    hasil = []

    for x in range(len(nilai_prediksi)):
    
        Error = nilai_prediksi[x] - nilai_yang_diharapkan[x]

        hasil.append(Error)
    
    fileOut = open('output.txt', 'w')
    fileOut.write(str(hasil))
    return hasil

backPropogation()