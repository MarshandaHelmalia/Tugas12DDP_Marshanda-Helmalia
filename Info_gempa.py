from Gempa import *

gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)

gempa1.cetak()
print('Dampak gempa :', gempa1.dampak())
gempa2.cetak()
print('Dampak gempa :', gempa2.dampak())
gempa3.cetak()
print('Dampak gempa :', gempa3.dampak())
gempa4.cetak()
print('Dampak gempa :', gempa4.dampak())
gempa5.cetak()
print('Dampak gempa :', gempa5.dampak())