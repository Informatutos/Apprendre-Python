#coding:utf-8
liste1 = ['paris','youtube','facebook','twitter','snaptchat']
liste2 = ['paris','youtube1', 'snaptchat','messenger', 'discord']
liste5 = [45, 78, 20, 76,5, 0]

"""for elem in liste1:
    if elem not in liste2:
        print([elem])
print('------------------------------')
elem1 = [elem for elem in liste1 if elem not in liste2]

for elem in liste1 :
    if elem not in elem1 :
        print(elem)"""
print(liste1,'\n-------------------------------------')
liste1.append('tokyo')
print(liste1)
print('\n-------------------------------------')
liste1.pop(2)
print(liste1)
print('\n-------------------------------------')
liste5.sort()
print(liste5)
liste5.remove(45)
print(liste5)
print(liste5.index(20))
print('\n-------------------------------------')
print(len(liste2))
print('\n-------------------------------------')
for i in range(len(liste2)) :
    print(i, liste2[i])

print('\n-------------------------------------')

for i,a in enumerate(liste2):
    print(i,a)
print('\n-------------------------------------')

