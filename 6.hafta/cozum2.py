import os
import sqlite3
import zipfile
import pandas as pd
import glob



if not os.path.exists("veri"):
    os.mkdir("veri")

    depo = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    depo.extractall("veri/")

    tum_dosyalar = os.listdir("veri")
    pandas_csv_listesi = []
    for csv_dosya in tum_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]
        veri["parite"] = csv_dosya.split("_")[0]
        pandas_csv_listesi.append(veri)

    birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
    birlesmis_csv_ler.to_csv('hepsi.csv', index=False)

baglanti = sqlite3.connect("kripton.vt")
cursor = baglanti.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS parite("
               +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
               +" otime DATETIME, open FLOAT, "
               +"high FLOAT, low FLOAT, close FLOAT);")

cursor.execute("INSERT INTO parite("
               "parite(otime,open,high,low,close)"
               "'2022-01-01 03:00:00',"
               ""
               )

kayitlar = pd.read_csv("hepsi.csv")



