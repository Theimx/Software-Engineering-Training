def exo1():
    from robot import *
    haut()
    haut()
    haut()
    droite()
    droite()
    bas()
    bas()
    droite()

def exo2():
    from robot import *
    for loop in range(20):
        ramasser()
    for loop in range(15):
      droite()
    deposer()
    for loop in range(15):
      gauche()

def exo3():
    from robot import *
    anneau = 1
    for loop in range(10):
        for loop in range(anneau):
            droite()
        ramasser()
        for loop in range(anneau):
            gauche()  
        deposer()
        anneau = anneau + 1

def exo4():
    nbCubes = 0
    largeurArête = 1
    for loop in range(9):
        nbCubes = nbCubes + largeurArête * largeurArête * largeurArête
        largeurArête = largeurArête + 2
    print(nbCubes)

def exo5():
    positionDépart = int(input())
    largeurEmplacement = int(input())
    nbVendeurs = int(input())

    position = positionDépart
    for iVendeur in range(nbVendeurs + 1):
        print(position)
        position = position + largeurEmplacement

def exo6():
    largeurBas = int(input())
    largeurHaut = int(input())
    
    volume = 0
    largeur = largeurHaut
    for loop in range(largeurBas - largeurHaut + 1):
        volume = volume + largeur * largeur
        largeur = largeur + 1
        
    print(volume)

def exo7():
    nbKarvas = int(input())
    for loop in range(nbKarvas):
        poids = int(input())
        âge = int(input())
        longueurCornes = int(input())
        hauteurAuGarrot = int(input())
        print(longueurCornes * hauteurAuGarrot + poids)