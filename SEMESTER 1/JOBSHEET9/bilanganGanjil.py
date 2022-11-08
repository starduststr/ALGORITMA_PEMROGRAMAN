def main():
    n = eval(input("Masukan angka : "))

    for x in range(n):
        bilangan = x%2
        if bilangan != 0:
            print(x)

main()