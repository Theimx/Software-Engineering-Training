
#Liste des exercices obligatoires du Niveau 1 sur le site France-IOI 
#https://www.france-ioi.org/algo/chapters.php

#Exo 1
def exo1():
   haut()
   haut()
   haut()
   droite()
   droite()
   bas()
   bas()
   droite()

#Exo 2
def exo2(): 
   for i in range(20):
      ramasser()
      for e in range(15):
         droite()
      deposer()
      for y in range(15):
         gauche()

#Exo 3
def exo3():

   steps = 1 

   for i in range(10):
      for i in range(steps): 
         droite()
      ramasser()
      for i in range(steps):
         gauche()
      deposer()
      steps += 1

#Exo 4 
def exo4():
   a = 17
   b = 0

   for i in range(9):
      b += a *a*a
      a -= 2

   print(b)

#Exo 5
def exo5():
   positiondepart = int(input())
   largeuremplacement = int(input())
   nbvendeur = int(input())

   for i in range(nbvendeur + 1):
      print(positiondepart)
      positiondepart += largeuremplacement 

#Exo 6
def exo6():
   a = int(input())
   b = int(input())
   result = 0

   while a != b-1 :
      result += a * a
      a -= 1
      
   print(result)

#Exo7
#lire 4 entiers : son poids, son âge, la longueur de ses cornes et la hauteur au garrot ;
#afficher sa note, sachant qu'elle s'obtient en multipliant la longueur des cornes par la hauteur au #garrot, valeur à laquelle on ajoute le poids.

def exo7():

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

def exo8():
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

def exo9():
   code = 64741
   goodresult = "Bon festin !"
   badresult = "Allez-vous en ! "

   reponse = int(input())
   if reponse != code:
      print(badresult)
   else :
      print(goodresult)

def exo10():
   position = int(input())
   nb_village = int(input())
   villages = []

   for i in range(nb_village):
      distance = abs(int(input()))
      if distance - position <= 50:
         villages.append(1)
      distance = 0
   print(len(villages))

def exo102():
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

def exo11():
   nbMarchands = int(input())
   prix = [int(input()) for _ in range(nbMarchands)]
   minim = min(prix)
   for i in range(nbMarchands - 1, -1, -1):
      if prix[i] == minim:
         print(i + 1)
         break

def exo12():

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