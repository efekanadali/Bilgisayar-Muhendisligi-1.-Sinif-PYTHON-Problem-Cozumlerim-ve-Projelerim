#Dizi Elemanlarını Ters Çevirme Fonksiyonu:* Bir dizinin elemanlarını ters çeviren özyinemeli bir fonksiyon yazın.

def OzTersCevir(liste,index):
    if index == -(len(liste)-1):
        return liste
    return OzTersCevir(liste,index-1),
    

print(OzTersCevir([1,2,3,4,5],0))

#hatalı çözüm tekrar incele