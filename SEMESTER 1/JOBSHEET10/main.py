def main():
    fileNilai = open("nilai.txt", "r")

    n = 0
    i = 1
    rata_rata = 0
    print("Daftar rata-rata nilai mata kuliah algoritma dan pemrograman: ")
    for nilai in fileNilai.readlines():
        
        data = nilai.split(',')
        # print(type(data))
        for x in data:
            # print(x)
            n += 1
        
        while i < n:
            rata_rata+= int(data[i])
            i+=1
        bagi = n-1
        print("{} : {}".format(data[0],rata_rata//bagi))
        rata_rata = 0
        n = 0
        i = 1

        
    
           
main()