import math as mt

class Main:
    def start():
        menu = ['acos(x)','asin(x)','atan(x)','atan2(y,x)',
            'cos(x)','hypot(x)','sin(x)','tan(x)',
            'degress(x)','radians(x)'
            ]
        i = 1
        print("==========Trigonometry Calculator==========\n")
        for data in menu:
            print("{}. {}".format(i,data))
            i+=1
        print('0. Help')
        option = eval(input("Pilih : "))
        
        if menu[option-1] == "atan2(y,x)":
            try:
                y,x = input("Masukan nilai y,x : ").split(',')
                print("\n{} = {}".format(menu[option-1],Calc.atan2(int(y),int(x))))
            except:
                print("Oops! nilai yang dimasukan salah")
                print("Contoh : 1,2")
        elif option < 0  and option <= len(menu):
            x = eval(input("Masukan nilai x : "))
            
            try :
                if option == 1:
                    hasil = Calc.acos(x)
                    
                elif option == 2:
                    hasil = Calc.asin(x)
                    
                elif option == 3:
                    hasil = Calc.atan(x)
                    
                elif option == 5:
                    hasil = Calc.cos(x)

                elif option == 6:
                    hasil = Calc.hypot(x)

                elif option == 7:
                    hasil = Calc.sin(x)

                elif option == 8:
                    hasil = Calc.tan(x)

                elif option == 9:
                    hasil = Calc.degress(x)

                elif option == 9:
                    hasil = Calc.radians(x)
                    
                print("\n{} = {}".format(menu[option-1],hasil))

                    
            except Exception as error:
                print("Opps! Nilai yang dimasukan salah")
                print(error)
        
        elif option == 0 :
            while True:
                i = 1
                print("-------------------HELP-------------------")
                for data in menu:
                    print("{}. {}".format(i,data))
                    i+=1
                print("------------------------------------------")
                option = eval(input("Pilih : "))
                
                try:
                    print("\n",Calc.help(menu[option-1]))
                except:
                    print("Oppss! Pilihan tidak ada")
                
                q = input("\nAkhiri sesi ini? (y/n) : ")
                
                if q == "y" or q == "Y":
                    break
            
        else :
            print("Oopss! nilai yang anda masukan salah")
        
    
    
    
class Calc:
    def acos(x):
        result = mt.acos(x)
        return result

    def asin(x):
        result = mt.asin(x)
        return result

    def atan(x):
        result = mt.atan(x)
        return result

    def atan2(x,y):
        result = mt.atan2(y,x)
        return result

    def cos(x):
        result = mt.cos(x)
        return result

    def hypot(x):
        result = mt.hypot(x)
        return result

    def sin(x):
        result = mt.sin(x)
        return result
    
    def tan(x):
        result = mt.tan(x)
        return result
    
    def degress(x):
        result = mt.degress(x)
        return result
    
    def radians(x):
        result = mt.radians(x)
        return result

    def help(option):
        data = {
            'acos(x)' : 'Fungsi acos(x) digunakan untuk menampilkan nilai arc cosinus dari sebuah bilangan x. Dimana x adalah bilangan antara -1 sampai dengan 1.',
            'asin(x)' : 'Fungsi asin(x) digunakan untuk menampilkan nilai arc sinus dari sebuah bilangan x. Dimana x adalah bilangan antara -1 sampai dengan 1.',
            'atan(x)' : ' Fungsi atan(x) digunakan untuk menampilkan nilai arc tangen dari sebuah bilangan x. Dimana x adalah bilangan antara -1 sampai dengan 1.',
            'atan2(y,x)' : 'Fungsi atan2(y,x) akan menghasilkan nilai atan y/x dalam radian.',
            'cos(x)' : 'Fungsi cos(x) digunakan untuk menampilkan nilai cosinus dari sebuah bilangan x. Dimana hasilnya adalah antara -1 sampai dengan 1.',
            'hypot(x)' : 'Fungsi hypot(x,y) akan menghasil bentuk Ecludean, akar dari x*x + y*y.',
            'sin(x)' : ' Fungsi sin(x) digunakan untuk menampilkan nilai sinus dari sebuah bilangan x. Hasilnya adalah bilangan antara -1 sampai dengan 1.',
            'tan(x)' : ' Fungsi tan(x) digunakan untuk menampilkan nilai tangen dari sebuah bilangan x. Hasilnya adalah bilangan antara -1 sampai dengan 1.',
            'degress(x)' : ' Fungsi ini akan mengkonversi dari radian x menjadi degrees.',
            'radians(x)' : ' Fungsi ini akan mengkonversi dari degrees menjadi radian.'
        }
        return data[option]

Main.start()