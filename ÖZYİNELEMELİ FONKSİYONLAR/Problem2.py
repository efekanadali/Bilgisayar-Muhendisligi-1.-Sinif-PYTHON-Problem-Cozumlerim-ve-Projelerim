#Asal Sayı Kontrolü Fonksiyonu:* Bir sayının asal olup olmadığını kontrol eden özyinemeli bir fonksiyon yazın.

def Asalozyineleme(sayi,index):
    if index == 2:
        return True
    
    if sayi % (index-1) == 0 :
        return False
    return Asalozyineleme(sayi,index-1)

print(Asalozyineleme(11,11))       #fonksiyonun kullanımında iki değişkende de aynı sayıyı kullanmak gereklidir
