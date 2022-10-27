import sqlite3

yok = sqlite3.connect("a.vt")
#bağlantı sağlanır.
cursor = yok.cursor()
#cursor veritabınında işlem yapmak için.

cursor.execute("kitap tablosu yoksa oluştur"
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayinevi TEXT,"
               "sayfa_sayi INT")
yok.commit()

yok.close()