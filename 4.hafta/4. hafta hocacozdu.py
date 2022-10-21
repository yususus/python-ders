"""
soru:
kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerinde bu toplamdan çıkaran ve geri döndüren fonksiyon
"""



def polinDram(*dram):
    toplam =  0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam



print(polinDram(10, 101, 55, 40, 9009))