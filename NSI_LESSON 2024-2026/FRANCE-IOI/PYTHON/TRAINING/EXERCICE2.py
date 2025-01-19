import math

#Modifier les deux fichier pour mettre le nom de l'exo puis la solution *

#Liste des exercices obligatoires du Niveau 2 sur le site France-IOI 
#https://www.france-ioi.org/algo/chapters.php

#exo 1

actual_tax = float(input()) / 100
new_tax = float(input()) / 100
price_ttc = float(input())
price_ht = price_ttc / (1 + actual_tax)
new_price_ttc = price_ht * (1 + new_tax)
print(round(new_price_ttc, 2))

#exo 2

money = float(input())
book = float(input())
print(round((money//book)))

#or 
print(round(float(input())//float(input())))

#exo 3

nbPersonnes = int(input())
nbFruits = int(input())
if (nbFruits % nbPersonnes) == 0: 
    print("oui")
else : 
    print("non")

#exo 4
print((int(input())%24+24)%24)

#Préparation de l'onguent
grammes = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
indexGramme = int(input())
print(grammes[indexGramme])
