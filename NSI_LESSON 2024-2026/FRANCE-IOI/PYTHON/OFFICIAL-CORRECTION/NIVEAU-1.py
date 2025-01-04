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