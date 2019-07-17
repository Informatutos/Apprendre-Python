#coding:utf-8

nombre = 0
while nombre < 10 :
    nombre += 1
    print(nombre)
    if nombre == 2 :
        continue
    

for i in  range(10) :

    print(i)
    if i == 5 :
        print("je suis à cette niveau ")
        continue
    
AgeJoueur = 18
while AgeJoueur :
    getAge = int(input('Entrer votre Age '))
    if getAge >= AgeJoueur :
        print("vous etes majeur ! ")
        break
    else :
        continue


