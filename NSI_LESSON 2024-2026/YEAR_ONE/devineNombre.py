import random

def choixNiveau():
    _choix = int(input("Choisi un niveau de difficulté entre 1 et 3 : "))
    if _choix == 1:
        nombreMax = 100
    elif _choix == 2:
        nombreMax = 1000
    elif _choix == 3:
        nombreMax = 10000
    else :
        print("Incorrect")
        choixNiveau()
    
    return nombreMax

#Nombre de joueur ensuite pour chaque joueur faire une partie chacun 
#et pour chacun lancer une partie avec le même nombre 

def DevineNombre(nombreMax):
    _nbPlayer = int(input("entrez le nombre de joueur : "))
    _current = 0

    for i in range(_nbPlayer):
        _current +=1
        _goal = random.randint(1,nombreMax)
        _nbTry = 6
        _rep = 0
        _win = False
        print("Chaque joueur a un chiffre différent a deviner ")
        while _win == False or _nbTry < 0:
            print("Joueur " , _current ," : ")
            print("a retirer, reponse : " , _goal)
            _rep = int(input("Entrez un nombre entre 1 et "+ str(nombreMax)))

            if _rep == _goal :
                print("Joueur ", _current," a gagner")
                _win = True
            elif _rep > _goal:
                print("Viser plus petit")
                _nbTry -= 1 
                print("Tentative restante : ",_nbTry)              
            elif _rep < _goal:
                print("Viser plus grand")
                _nbTry -= 1 
                print("Tentative restante : ",_nbTry)
        _nbTry = 6

DevineNombre(choixNiveau())