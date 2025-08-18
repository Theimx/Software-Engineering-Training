import math
import random

#lagomorphes

#Liste des 44 exercices du Niveau 2 du site France-IOI en Python.
#https://www.france-ioi.org/algo/chapters.php

#Ce fichier n'a pas pour but d'être excecuté.
#Exercices validé France-IOI : 29
#Exercices validé : 12/44

#Exo 1 Chapitres 1, Découverte: Origami

#Exo 2 Chapitres 1, Découverte: Conversions de distances

#Exo 3 Chapitres 1, Entraînement: Comparatif de prix

#Exo 4 Chapitres 1, Entraînement: Moyenne des notes

#Exo 5 Chapitres 1, Découverte: Augmentation de la population

#Exo 6 Chapitres 1, Entraînement: Construction de maisons

#Exo 7 Chapitres 1, Découverte: Soirée orageuse

def exo7chap1(): 
    decalage = float(input())
    decalage = (decalage * 340.29)/1000
    print(round(decalage))

#Exo 8 Chapitres 1, Validation: Augmentation des taxes

def exo8chap1(): 
    actual_tax = float(input()) / 100
    new_tax = float(input()) / 100
    price_ttc = float(input())
    price_ht = price_ttc / (1 + actual_tax)
    new_price_ttc = price_ht * (1 + new_tax)
    print(round(new_price_ttc, 2))

#Exo 9 Chapitres 1, Validation: Achat de livres

def exo9chap1(): 
    money = float(input())
    book = float(input())
    print(round((money//book)))

#or Exo 9 Chapitres 1, Validation: Achat de livres

def exo9_2chap1(): 
    print(round(float(input())//float(input())))

#Exo 10 Chapitres 1, Validation: Une belle récolte

def exo10chap1(): 
    nbPersonnes = int(input())
    nbFruits = int(input())
    if (nbFruits % nbPersonnes) == 0: 
        print("oui")
    else : 
        print("non")

#Exo 11 Chapitres 1, Validation: La roue de la fortune

def exo11chap1(): 
    print((int(input())%24+24)%24)

#Exo 12 Chapitres 2, Découverte: Préparation de l'onguent

def exo12chap2(): 
    grammes = [500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
    indexGramme = int(input())
    print(grammes[indexGramme])

#Exo 13 Chapitres 2, Entraînement: Liste de courses

def exo13chap2(): 
    poids = []
    prix = [9, 5, 12, 15, 7, 42, 13, 10, 1 , 20]

    for i in range(10):
        poids.append((int(input())*prix[i]))

    print(sum(poids))

#Exo 14 Chapitres 2, Découverte: Grand inventaire

def exo14chap2(): 
    nbOP = int(input())
    LivreDeComptes = [0,0,0,0,0,0,0,0,0,0]

    for i in range(nbOP):
        indexLigne = (int(input()) -1)
        LivreDeComptes[indexLigne] = (int(input()) + LivreDeComptes[indexLigne] )
    for i in LivreDeComptes :
        print(i)
        
#Exo 15 Chapitres 2, Découverte: Étude de marché

def exo15chap2(): 
    nbProduits = int(input())
    nbPersonnes = int(input())

    tableau = [0] * nbProduits
    
    for i in range(nbPersonnes):
        numProd = int(input())
        
        tableau[numProd] = tableau[numProd] + 1
        
    for j in range(nbProduits):
        print(tableau[j])

#Exo 16 Chapitres 2, Entraînement: Répartition du poids

def exo16chap2(): 
    nbCharrettes = int(input())
    poids_list = []

    for _ in range(nbCharrettes):
        poids = float(input())
        poids_list.append(poids)

    poids_moyen = sum(poids_list) / nbCharrettes

    for poids in poids_list:
        print(poids_moyen - poids)

#Exo 17 Chapitres 2, Validation: Visite de la mine

def exo17chap2(): 
    nbDeplacements = int(input())
    deplac = []

    for _ in range(nbDeplacements):
        deplac.append(int(input()))

    for move in reversed(deplac):
        if move == 1:
            print(2)
        elif move == 2:
            print(1)
        elif move == 4:
            print(5)
        elif move == 5:
            print(4)
        elif move == 3:
            print(3)

#Exo 18 Chapitres 2, Découverte: Journée des cadeaux

def exo18chap2(): 
    nbpeople = int(input())
    town = []

    for _ in range(nbpeople):
        town.append(int(input()))

    town.sort()

    if nbpeople % 2 == 1:

        median = town[nbpeople // 2]
    else:
        median = (town[nbpeople // 2 - 1] + town[nbpeople // 2]) / 2
    print(median)

#Exo 19 Chapitres 2, Entraînement: Course à trois jambes

def exo19chap2(): 
    
    nbParticipants = int(input())
    listeP = []
    for i in range(nbParticipants):
        listeP.append(int(input()))

    listeP.sort()
    for i in range(nbParticipants // 2):
        print(listeP[i], listeP[-(i + 1)])

#Exo 20 Chapitres 2, Validation: Banquet municipal

def exo20chap2():
    nbPosition = int(input())
    nbChange = int(input())

    guest = []
    for i in range(nbPosition):
        guest.append(int(input()))
    for i in range(nbChange):
        a = int(input())
        b = int(input())
        c = guest[a]
        guest[a] = guest[b]
        guest[b] = c
    
    for i in guest:
        print(i)

#Exo 21 Chapitres 2, Validation: Choix des emplacements

def exo21chap2():
    nbEmplacements = int(input())
    marchands = []

    for i in range(nbEmplacements):
        marchands.append(int(input()))

    cur = 0
    for i in marchands:
        print(marchands.index(cur))
        cur += 1


#Exo 22 Chapitres 3, Découverte: Petites fiches et gros travail

#Exo 23 Chapitres 3, Découverte: Priorité alphabétique

#Exo 24 Chapitres 3, Validation: Une ligne sur deux

def exo24chap3():
    nbLigne = int(input())
    for i in range(nbLigne):
        ligne = input()
        if i % 2 == 0:
            print(ligne)
            
#Exo 25 Chapitres 3, Découverte: Résumés de livres

def exo25chap3():
    for i in range(6):
        name = input()
        print(input())
        print(name)
        
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

#Exo 36 Chapitres 4, Découverte: Code secret deux fois

#Exo 37 Chapitres 4, Découverte: Deux codes secrets

#Exo 38 Chapitres 4, Entraînement: Dentelle

#Exo 39 Chapitres 4, Entraînement: Motif rectangulaire

#Exo 40 Chapitres 4, Découverte: Le plus petit de deux entiers

#Exo 41 Chapitres 4, Entraînement: Phénomène numérique

#Exo 42 Chapitres 4, Entraînement: Distance euclidienne

#Exo 43 Chapitres 4, Validation: Formes creuses

#Exo 44 Chapitres 4, Validation: Convertisseur d'unités