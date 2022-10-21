dosya = open("metin2.txt", 'w')
print("print('efsane baldo pirinc')", file=dosya)
dosya.close()

dosya = open("metin2.txt", 'r')
satir=dosya.readline()
eval(satir)