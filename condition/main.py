#coding:utf-8
'''
    La notion de condition en Python !

'''

valeur1 = 10
valeur2 = 25
valeur3 = 25
valeur4 = 155
if valeur1 < valeur2 :

    if valeur3 == valeur2:

        print("La valeur3 est égale à la valeur 2")

        if valeur4 != valeur1 :

            print('La valeur 4 est != de la valeur 1')

    print("La valeur1 est inférieur  à la valeur2")

elif valeur1 > valeur2:

    print("La valeur1 est inferieur à la valeur2 ")
else :
    print("Aucune réponse valide")

nomJoueur = input("Entrer votre nom : ")
ageJoueur = int(input("Entrer votre age : "))
tailJoueur = int(input("Entrer votre tail : "))
if ageJoueur >= 18 :

    if tailJoueur == 1:

        print(nomJoueur, "Bravo vous pouvez jouer le jeux")
    else :
        print("Vous n'avez pas la tail pour jouer à ce jeux ")

    print("Bon joueur !")

elif ageJoueur < 18 :

    print("Attention le jeux n'est pas reservé à vous !")

    if tailJoueur == 1 :

        print('Votre age vous pose problème pour jouer à ce jeux !')

    else : 

        print("Dommage mais vous ne pouvez pas jouer !")
else :
    print("Le programme ne peut calculer votre age ! ")
