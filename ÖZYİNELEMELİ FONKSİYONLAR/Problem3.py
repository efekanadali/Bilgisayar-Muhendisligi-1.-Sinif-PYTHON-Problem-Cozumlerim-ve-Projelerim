#Bir sayının üssünü hesaplayan özyinemeli bir fonksiyon yazın

def ozUs(taban,us):
    if us == 0:
        return 1
    return taban * ozUs(taban,us-1)

print(ozUs(3,4))          # 3**4 şeklinde ilk sayı taban ikinci sayı üs 