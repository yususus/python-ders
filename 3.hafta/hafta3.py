"""
klavyeden girilen 5 tane sayıyı bir listeye atarak bunların
karelerinden 20 çıktığında ortaya çıkan sonuca göre sıralayan ve
listeyi buna göre yazdıran programı yazınız.
"""


list = []
for i in range(0, 5): #range sıralama için kullanıyor
    list.append(int(input()))

def sirala_fonk(a):
    return a*a-20

list.sort(key=sirala_fonk)
print(list)