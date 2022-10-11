def getNama(nama):
    return nama

def getUsia(usia):
    return usia

def getAnak(jml):
    return jml

def getAlamat(alamat):
    return alamat

def main():

    nama = getNama(input("Masukan nama : "))
    usia = getUsia(input("Masukan usia : "))
    jml = getAnak(input("Masukan jumlah anak : "))
    alamat = getAlamat(input("Alamat tinggal : "))

    #Create file output

    outFile = open('output.txt', 'w')
    text = """Ahlan wa sahlan {}
Usia kamu adalah {} tahun
Jumlah anak kamu adalah {}
Alamat tinggal kamu adalah {}""".format(nama, usia, jml, alamat)

    print(text)
    outFile.write(text)

main()