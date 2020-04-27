#coding:utf-8
import re
chaine = "Programmation en language Python pour apprendre les expressions régulières en python"

regex = r'p'

regexX = re.subn(regex, 'Cpyhton', chaine, re.IGNORECASE)
print(regexX)

#En object on aura :: je l'avais oublié dans la vidéo ): !

regexO = 'p'
reO = re.compile(regexO)
regexXO = reO.subn('Cpyhton', chaine, re.IGNORECASE)
print(regexXO)