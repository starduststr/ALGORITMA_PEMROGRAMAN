def MenentukanNilai(data):
    nilai = float(data)
    if nilai >= 80.1:
        return "A"
    elif nilai >= 75.1:
        return "AB"
    elif nilai >= 70.1:
        return "B"
    elif nilai >= 65.1:
        return "BC"
    elif nilai >= 60.1:
        return "C"
    elif nilai >= 55.1:
        return "CD"
    elif nilai >= 50.1:
        return "D"
    elif nilai < 50.1:
        return "E"

def main():
    inputNilai = input("Masukan nilai : ")

    print("NILAI ANDA ADALAH : ",MenentukanNilai(inputNilai))

try:
    main()
except Exception as error:
    print("Terjadi kesalahan \n", error)