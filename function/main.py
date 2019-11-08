#coding:utf-8 
def maSomme() :
    x = 50
    y = 25
    print("La somme est : " , x + y)


def maSomme2() :
    maSomme()
    print("je suis la deuxiemme somme ")


multip = lambda x : x * 2
print(multip(6))
