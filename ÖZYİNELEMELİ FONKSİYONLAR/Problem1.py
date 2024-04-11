#Bir dizinin eleman sayısını hesaplayan özyinemeli bir fonksiyon yazın

def ozDiziElemanSayısı(liste):
    if liste == []:
        return 0
    return  1 + ozDiziElemanSayısı(liste[1:])

liste = [1,2,3,4,5,6]
print(ozDiziElemanSayısı(liste))
