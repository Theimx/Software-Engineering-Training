import math
import random

#Liste des 70 exercices du Niveau 1 du site France-IOI en Python.
#https://www.france-ioi.org/algo/chapters.php

#Ce fichier n'a pas pour but d'être excecuté.
#Exercices validé France-IOI : 29
#Exercices validé : 23/70

#Exo 1 Chapitres 1, Découverte: Hello world!

def exo1chap1(): 
   print("Hello world!")

#Exo 2 Chapitres 1, Entraînement: Présentation

def exo2chap1(): 
   print("Coucou !")
   print("Je m'appelle Camthalion")
   print("Ma devise est 'Parler peu mais parler bien'.")

#Exo 3 Chapitres 1, Découverte: Plan de la montagne

def exo3chap1(): 
   print("""
   Tout droit tu grimperas,
   La clé tu trouveras,
   Habile tu seras,
   Quand tu les porteras,
   Et avec le chef tu reviendras !
   """)

#Exo 4 Chapitres 1, Validation: Dans le fourré

def exo4chap1(): 
   #from robot import *
   haut()
   haut()
   haut()
   droite()
   droite()
   bas()
   bas()
   droite()

#Exo 5 Chapitres 1, Challenge: Empilement de cylindres

def exo5chap1(): 
   #from robot import *
   deplacer(1, 2)  
   deplacer(1, 3)  
   deplacer(2, 3)  
   deplacer(1, 2)  
   deplacer(3, 1)  
   deplacer(3, 2)  
   deplacer(1, 2)  

   deplacer(1, 3)  
   deplacer(2, 1)

   deplacer(2, 3)  
   deplacer(1, 2)  
   deplacer(3, 1) 

   deplacer(2, 1)  
   deplacer(2, 3)  
   deplacer(1, 2)  
   deplacer(1, 3)  
   deplacer(2, 3)  

#Exo 6 Chapitres 1, Challenge: Recette secrète

def exo6chap1(): 
   #from robot import *

   remplir(5)
   transferer(5, 3)
   vider(3)
   transferer(5, 3)
   remplir(5)
   transferer(5, 3)

#Exo 7 Chapitres 2, Découverte: Punition

def exo7chap2(): 
   for i in range(135):
      print("Je dois respecter le Grand Sorcier.")

#Exo 8 Chapitres 2, Entraînement: Mathématiques de base

def exo8chap2(): 
   for loop in range(13):
      print("9 * 8 = 72")

#Exo 9 Chapitres 2, Entraînement: Transport d'eau

def exo9chap2(): 
   #from robot import *

   gauche()
   gauche()
   print("Bonjour, laissez-moi vous aider")
   ramasser()
   for i in range(32):
      droite()
   deposer()

#Exo 10 Chapitres 2, Découverte: Le secret du Goma

#Exo 11 Chapitres 2, Entraînement: Sisyphe

#Exo 12 Chapitres 2, Découverte: Page d'écriture

#Exo 13 Chapitres 2, Découverte: Jeu de dames

#Exo 14 Chapitres 2, Entraînement: Mont Kailash

#Exo 15 Chapitres 2, Validation: Vendanges

def exo15chap2(): 
   #from robot import * 

   for i in range(20):
      ramasser()
      for e in range(15):
         droite()
      deposer()
      for y in range(15):
         gauche()

#Exo 16 Chapitres 2, Challenge: Le Grand Événement

#Exo 17 Chapitres 3, Découverte: Réponds !

#Exo 18 Chapitres 3, Découverte: L'éclipse

#Exo 19 Chapitres 3, Entraînement: Bonbons pour tout le monde !

#Exo 20 Chapitres 3, Découverte: L'algoréathlon

#Exo 21 Chapitres 3, Entraînement: Cour de récréation

#Exo 22 Chapitres 3, Découverte: Une partie de cache-cache

#Exo 23 Chapitres 3, Entraînement: Progresser par l'erreur

#Exo 24 Chapitres 3, Entraînement: Décollage de fusée

#Exo 25 Chapitres 3, Entraînement: Invasion de batraciens

#Exo 26 Chapitres 3, Entraînement: Kermesse

#Exo 27 Chapitres 3, Validation: Course avec les enfants

def exo27chap3(): 
   #from robot import *

   steps = 1 

   for i in range(10):
      for i in range(steps): 
         droite()
      ramasser()
      for i in range(steps):
         gauche()
      deposer()
      steps += 1

#Exo 28 Chapitres 3, Validation: Construction d'une pyramide

def exo28chap3(): 
   a = 17
   b = 0

   for i in range(9):
      b += a *a*a
      a -= 2

   print(b)

#Exo 29 Chapitres 3, Challenge: Table de multiplication

#Exo 30 Chapitres 4, Découverte: Récoltes

#Exo 31 Chapitres 4, Entraînement: Retraite spirituelle

#Exo 32 Chapitres 4, Entraînement: Âge des petits-enfants

#Exo 33 Chapitres 4, Entraînement: Encore des punitions

#Exo 34 Chapitres 4, Entraînement: Graduation de thermomètres

#Exo 35 Chapitres 4, Entraînement: Jeu de calcul mental

#Exo 36 Chapitres 4, Validation: La Grande Braderie

def exo36chap4(): 
   positiondepart = int(input())
   largeuremplacement = int(input())
   nbvendeur = int(input())

   for i in range(nbvendeur + 1):
      print(positiondepart)
      positiondepart += largeuremplacement 

#Exo 37 Chapitres 4, Entraînement: Bétail

#Exo 38 Chapitres 4, Validation: Socles pour statues

def exo38chap4(): 
   a = int(input())
   b = int(input())
   result = 0

   while a != b-1 :
      result += a * a
      a -= 1
   print(result)

#Exo 39 Chapitres 4, Validation: Le plus beau Karva

def exo39chap4(): 
   nbkarva = int(input())
   p= 0
   a = 0
   l = 0
   g = 0

   score = 0
   for i in range(nbkarva):
      p =int(input())
      a =int(input())
      l =int(input())
      g =int(input())
      score = l*g + p
      print(score)
      p= 0
      a = 0
      l = 0
      g = 0

#Exo 40 Chapitres 5, Découverte: Transport des bagages

#Exo 41 Chapitres 5, Entraînement: Bornes kilométriques

#Exo 42 Chapitres 5, Entraînement: Tarifs dégressifs

#Exo 43 Chapitres 5, Entraînement: Bagarre générale

#Exo 44 Chapitres 5, Découverte: Tarif du bateau

#Exo 45 Chapitres 5, Entraînement: Traversée du pont

#Exo 46 Chapitres 5, Validation: Concours de tir à la corde

def exo46chap5(): 
   nbperson = int(input())

   equipone = []
   equiptwo = []
   count = 0

   for i in range(nbperson * 2):
      n = int(input())
      count += 1
      
      if count%2 == 0:
         equiptwo.append(n)
      
      elif count%2 != 0:
         equipone.append(n)

   a = sum(equipone)
   b = sum(equiptwo)
   x = 0
   if a > b:
      x = "1"
   else :
      x = "2" 

   print("L'équipe ",x," a un avantage")

   print("Poids total pour l'équipe 1 : " + str(a) )
   print("Poids total pour l'équipe 2 : " + str(b) )

#Exo 47 Chapitres 5, Validation: Mot de passe du village

def exo47chap5(): 
   code = 64741
   goodresult = "Bon festin !"
   badresult = "Allez-vous en ! "

   reponse = int(input())
   if reponse != code:
      print(badresult)
   else :
      print(goodresult)

#Exo 48 Chapitres 6, Entraînement: Villes et villages

#Exo 49 Chapitres 6, Validation: Planning de la journée

def exo49chap6(): 
   position = int(input())
   nb_village = int(input())
   villages = []

   for i in range(nb_village):
      distance = abs(int(input()))
      if distance - position <= 50:
         villages.append(1)
      distance = 0
   print(len(villages))

#or 
def exo49_2chap6(): 
   print(*(sum(abs(n-int(input()))<51 for _ in range(int(input())))for n in[int(input())]))

#or 
def exo49_3chap6(): 
   posActuelle = int(input())
   nbVillages = int(input())
   nbAccessibles = 0
   for loop in range(nbVillages):
      posVillage = int(input())
      ecart = posActuelle - posVillage
      if ecart < 0:
         ecart = -ecart
      if ecart <= 50:
         nbAccessibles = nbAccessibles + 1
   print(nbAccessibles)

#Exo 50 Chapitres 6, Découverte: Étape la plus longue

#Exo 51 Chapitres 6, Entraînement: Calcul des dénivelées

#Exo 52 Chapitres 6, Entraînement: Type d'arbres

#Exo 53 Chapitres 6, Entraînement: Tarifs de l'auberge

#Exo 54 Chapitres 6, Entraînement: Protection du village

#Exo 55 Chapitres 6, Validation: Le juste prix

def exo55chap6(): 
   nbMarchands = int(input())
   prix = [int(input()) for _ in range(nbMarchands)]
   minim = min(prix)
   for i in range(nbMarchands - 1, -1, -1):
      if prix[i] == minim:
         print(i + 1)
         break

#Exo 56 Chapitres 7, Découverte: Espion étranger

#Exo 57 Chapitres 7, Entraînement: Maison de l'espion

#Exo 58 Chapitres 7, Entraînement: Nombre de jours dans le mois

#Exo 59 Chapitres 7, Entraînement: Amitié entre gardes

#Exo 60 Chapitres 7, Entraînement: Nombre de personnes à la fête

#Exo 61 Chapitres 7, Validation: Casernes de pompiers

def exo61chap7(): 
   nbPaires = int(input())
   for loop in range(nbPaires):
      xMin1 = int(input())
      xMax1 = int(input())
      yMin1 = int(input())
      yMax1 = int(input())
      xMin2 = int(input())
      xMax2 = int(input())
      yMin2 = int(input())
      yMax2 = int(input())
      if ( (xMax2 <= xMin1) or (xMax1 <= xMin2) ) or ( (yMax2 <= yMin1) or (yMax1 <= yMin2) ):
         print("NON")
      else:
         print("OUI")

#Exo 62 Chapitres 7, Découverte: Personne disparue

#Exo 63 Chapitres 7, Découverte: La grande fête

#Exo 64 Chapitres 7, Entraînement: L'espion est démasqué !

#Exo 65 Chapitres 7, Validation: Zones de couleurs

def exo65chap7(): 
   nb_jeton = int(input())
   result = "Dans une zone jaune"

   for i in range(nb_jeton):
      x = int(input())
      y = int(input())
      result = "Dans une zone jaune"

      if x >= 10 and x <= 85: #toute la zone bleus 
         if y >= 10 and y <= 55:
            result = "Dans une zone bleue"
            if x > 25 and x < 50: #la petite partie jaune dans le bleus
               if y > 20 and  y < 45 :
                  result = "Dans une zone jaune"

      if x >= 15 and x <= 45 :
         if y >= 60 and y <= 70:
            result = "Dans une zone rouge" 
      if x >= 60 and x <= 85 :
         if y >= 60 and y <= 70:
            result = "Dans une zone rouge" 

      if x < 0 or x > 90:   #en dehirs de la feuille 
         result = "En dehors de la feuille"
      if y < 0 or y > 70:
         result = "En dehors de la feuille"
      print(result)

#Exo 66 Chapitres 8, Découverte: Département de médecine : contrôle d'une épidémie

#Exo 67 Chapitres 8, Entraînement: Administration : comptes annuels

#Exo 68 Chapitres 8, Entraînement: Département de pédagogie : le « c'est plus, c'est moins »

#Exo 69 Chapitres 8, Validation: Département d'architecture : construction d'une pyramide

def exo69chap8(): 
   nbPierreMax=int(input())
   nbPierre=0
   etage=1
   while (nbPierre+(etage*etage))<=nbPierreMax:
      nbPierre+=(etage*etage)
      etage=etage+1
   print(etage-1)
   print(nbPierre)

#Exo 70 Chapitres 8, Validation: Département de chimie : mélange explosif

def exo70chap8(): 
   nb_test = int(input())
   t_min = int(input())
   t_max = int(input())
   
   for i in range(nb_test):
      t_test = int(input())
      if t_min <= t_test <= t_max:
         print("Rien à signaler")
      else:
         print("Alerte !!")
         break
