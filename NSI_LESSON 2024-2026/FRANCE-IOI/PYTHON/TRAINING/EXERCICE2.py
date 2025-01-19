import math

#Modifier les deux fichier pour mettre le nom de l'exo puis la solution *
#Les 44 exercices du niveau 2 a faire ici

#Liste des exercices obligatoires du Niveau 2 sur le site France-IOI 
#https://www.france-ioi.org/algo/chapters.php


#Exo 1 Chapitres 2, Découverte: Origami

#Exo 2 Chapitres 2, Découverte: Conversions de distances

#Exo 3 Chapitres 2, Entraînement: Comparatif de prix

#Exo 4 Chapitres 2, Entraînement: Moyenne des notes

#Exo 5 Chapitres 2, Découverte: Augmentation de la population

#Exo 6 Chapitres 2, Entraînement: Construction de maisons

#Exo 7 Chapitres 2, Découverte: Soirée orageuse

#Exo 8 Chapitres 2, Validation: Augmentation des taxes

actual_tax = float(input()) / 100
new_tax = float(input()) / 100
price_ttc = float(input())
price_ht = price_ttc / (1 + actual_tax)
new_price_ttc = price_ht * (1 + new_tax)
print(round(new_price_ttc, 2))

#Exo 9 Chapitres 2, Validation: Achat de livres

money = float(input())
book = float(input())
print(round((money//book)))

#or Exo 9 Chapitres 2, Validation: Achat de livres

print(round(float(input())//float(input())))

#Exo 10 Chapitres 2, Validation: Une belle récolte

nbPersonnes = int(input())
nbFruits = int(input())
if (nbFruits % nbPersonnes) == 0: 
    print("oui")
else : 
    print("non")

#Exo 11 Chapitres 2, Validation: La roue de la fortune

print((int(input())%24+24)%24)

#Exo 12 Chapitres 2, Découverte: Préparation de l'onguent
grammes = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
indexGramme = int(input())
print(grammes[indexGramme])

#Exo 13 Chapitres 2, Entraînement: Liste de courses