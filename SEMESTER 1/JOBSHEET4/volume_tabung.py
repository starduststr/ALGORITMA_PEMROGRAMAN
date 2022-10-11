from math import pi

""" MEMBUAT PROGRAM MENGHITUNG VOLUME KUBUS """
print("""----------------------------------------------------------------\n
        MENGHITUNG VOLUME KUBUS\n
-----------------------------------------------------------------""")

def volumeKubus(r = 0, t = 0):
    #menghitung volume kubus
    hasil = pi*r*r*t

    return "Volume tabung adalah : {} cm3".format(round(hasil, 3))

#jari jari
r = float(input("Silahkan masukan nilai jari-jari alas (r) : "))

#tingi
t = float(input("Silahkan masukan nilai t atau tinggai : "))

print(volumeKubus(r,t))