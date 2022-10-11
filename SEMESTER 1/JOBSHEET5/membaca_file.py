def main():
    fileName = 'infile.txt'

    with open(fileName, 'r') as data:
        for hasil in data:
            print(hasil)
            
            fileOut = open('outfile.txt', 'a')
            fileOut.write(hasil)
        data.close()
        fileOut.close()

main()