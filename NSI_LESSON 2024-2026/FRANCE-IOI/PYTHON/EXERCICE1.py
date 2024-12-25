from robot import *

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