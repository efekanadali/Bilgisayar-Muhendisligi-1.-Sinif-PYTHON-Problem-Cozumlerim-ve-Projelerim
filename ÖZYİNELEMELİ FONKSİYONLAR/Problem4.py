#En Büyük Ortak Bölen Hesaplama Fonksiyonu:* İki sayının en büyük ortak bölenini hesaplayan özyinemeli bir fonksiyon yazın.

def OBEB(x,y):
    if x == 0:
        return y
    if y == 0:
        return x 
    if x > y:
        return OBEB(x%y,y)
    if y > x:
        return OBEB(y%x,x)
print(OBEB(36,81))
