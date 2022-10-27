import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())
print('*******************************')
print(veri.columns)
print('*******************************')
print(veri[6:10])
print('*******************************')
print(veri.sort_values(by="sepal_length"))
print('*******************************')
veri = veri.sort_values(by="sepal_length")
print(veri.head())
""" head olunca ilk beş tanesini gösterip bırakıyor"""
print('*******************************')
ortanca_veri = veri["sepal_length"].median()
toplam_veri = veri["sepal_length"].sum()
ortalamaları_veri = veri["sepal_length"].mean()
print("Ortanca: ", ortanca_veri,
      "\nToplam", toplam_veri,
      "\nOrtalamaları: ", ortalamaları_veri)
print('****************************************')