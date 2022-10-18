def backPropogation(y1, y2 ,y3):
    hasil = []

    for x in range(len(y1)):
        nilai_prediksi = y1[x]
        nilai_yang_diharapkan = y2[x]

        Error = nilai_prediksi - nilai_yang_diharapkan

        hasil.append(Error)
        

    return hasil


def pemanggil(x1,x2,x3):
    
    return backPropogation(x1, x2, 0)

nilai_prediksi = [10,9,8,9,2,9,3,4]
nilai_yang_diharapkan = [8,9,2,5,4,2,3,4,8]

print(pemanggil(nilai_prediksi, nilai_yang_diharapkan, 0))