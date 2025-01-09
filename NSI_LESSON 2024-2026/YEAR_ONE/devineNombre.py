import random

def choixNiveau():
    _choix = int(input("Choisi un niveau entre 1 et 3 : "))
    if _choix == 1:
        _nombreMax = 100
    elif _choix == 2:
        _nombreMax = 1000
    elif _choix == 3:
        _nombreMax = 10000
    else :
        print("incorrect")
        choixNiveau()
    nombreAleatoire = random.randint(1,_nombreMax)
    return nombreAleatoire

#Nombre de joueur ensuite pour chaque joueur faire une partie chacun 
#et pour chacun lancer une partie avec le même nombre 

def DevineNombre(nombreAleatoire):
    _nbPlayer = int(input("entrez le nombre de joueur : "))
    
    for i in range(_nbPlayer):
        _goal = nombreAleatoire
        _nbTry = 6
        _rep = 0

        while _rep != _goal:
            _rep = int(input("entrez un nombre "))

DevineNombre(choixNiveau())