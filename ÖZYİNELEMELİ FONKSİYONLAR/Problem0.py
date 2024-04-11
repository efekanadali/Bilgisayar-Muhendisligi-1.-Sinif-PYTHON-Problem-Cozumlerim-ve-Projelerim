# Bir dizinin elemanlarını toplamak için özyinemeli bir fonksiyon yazın.

def listeElemanTop(liste,index):
    if index == len(liste):
        return 0
    return liste[index] + listeElemanTop(liste,index+1)

liste = [1,2,3,4,5]
print(listeElemanTop(liste,0))
