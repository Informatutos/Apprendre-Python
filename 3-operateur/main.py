#coding:utf-8

ballon = 12
chapeau = 255
achat = ballon + chapeau
achat = achat ** 2
print("le prix total est : ",achat)

x = 55
y = 5 
T = 55 / 5
N = 55 // 5 
print("La valeur numero 1 {} La valeur numero 2 {}".format(type(T), type(N)))

print("Result 1 est : {} et Result 2 est : {} ".format(T, N))

print("Bienvenue sur notre programme d'achat")

answer_chap = input("Entrer le prix de chapeau ")
answer_bal = input("Entrer le prix de votre ballon ")

Total = int(answer_chap) + int(answer_bal)

print("Le prix total de vos achats sont : {} $".format(Total))

modulo = Total % y


print(modulo)


