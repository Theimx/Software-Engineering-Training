import math,random

#Modifier les deux fichier pour mettre le nom de l'exo puis la solution *
#Les 44 exercices du niveau 2 a faire ici

#Liste des 44 exercices du Niveau 2 du site France-IOI 
#https://www.france-ioi.org/algo/chapters.php


#Exo 1 Chapitres 1, Découverte: Origami

#Exo 2 Chapitres 1, Découverte: Conversions de distances

#Exo 3 Chapitres 1, Entraînement: Comparatif de prix

#Exo 4 Chapitres 1, Entraînement: Moyenne des notes

#Exo 5 Chapitres 1, Découverte: Augmentation de la population

#Exo 6 Chapitres 1, Entraînement: Construction de maisons

#Exo 7 Chapitres 1, Découverte: Soirée orageuse

#Exo 8 Chapitres 1, Validation: Augmentation des taxes

actual_tax = float(input()) / 100
new_tax = float(input()) / 100
price_ttc = float(input())
price_ht = price_ttc / (1 + actual_tax)
new_price_ttc = price_ht * (1 + new_tax)
print(round(new_price_ttc, 2))

#Exo 9 Chapitres 1, Validation: Achat de livres

money = float(input())
book = float(input())
print(round((money//book)))

#or Exo 9 Chapitres 1, Validation: Achat de livres

print(round(float(input())//float(input())))

#Exo 10 Chapitres 1, Validation: Une belle récolte

nbPersonnes = int(input())
nbFruits = int(input())
if (nbFruits % nbPersonnes) == 0: 
    print("oui")
else : 
    print("non")

#Exo 11 Chapitres 1, Validation: La roue de la fortune

print((int(input())%24+24)%24)

#Exo 12 Chapitres 2, Découverte: Préparation de l'onguent
grammes = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
indexGramme = int(input())
print(grammes[indexGramme])

#Exo 13 Chapitres 2, Entraînement: Liste de courses

#Exo 14 Chapitres 2, Découverte: Grand inventaire

#Exo 15 Chapitres 2, Découverte: Étude de marché

#Exo 16 Chapitres 2, Entraînement: Répartition du poids

#Exo 17 Chapitres 2, Validation: Visite de la mine

#Exo 18 Chapitres 2, Découverte: Journée des cadeaux

#Exo 19 Chapitres 2, Entraînement: Course à trois jambes

#Exo 20 Chapitres 2, Validation: Banquet municipal

#Exo 21 Chapitres 2, Validation: Choix des emplacements

#Exo 22 Chapitres 3, Découverte: Petites fiches et gros travail

#Exo 23 Chapitres 3, Découverte: Priorité alphabétique

#Exo 24 Chapitres 3, Validation: Une ligne sur deux

#Exo 25 Chapitres 3, Découverte: Résumés de livres

#Exo 26 Chapitres 3, Validation: Lire ou ne pas lire, telle est la question

#Exo 27 Chapitres 3, Découverte: Fiches d’inscription

#Exo 28 Chapitres 3, Validation: Analyse de fréquence

#Exo 29 Chapitres 3, Découverte: Impression d’étiquettes

#Exo 30 Chapitres 3, Validation: Écriture en miroir

#Exo 31 Chapitres 3, Découverte: Inscription d’étudiants

#Exo 32 Chapitres 3, Entraînement: ngms sns vlls

#Exo 33 Chapitres 3, Validation: La bataille

#Exo 34 Chapitres 3, Validation: Analyse d’une langue

#Exo 35 Chapitres 3, Validation: Sans espaces