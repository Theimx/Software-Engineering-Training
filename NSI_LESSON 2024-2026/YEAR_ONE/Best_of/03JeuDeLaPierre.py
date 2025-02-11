# Proposer une fonction qui réalise le jeux de la pierre.
# Le jeu du Pierre, est un jeux ou les joueurs retirent des pierres d'un ensemble et 
# celui qui retire la dernière pierre gagne. Le tas de pierre est fixé a 25.
# Les joueurs retirent à tour de rôle un nombre de pierres entre 1 et 3. Le joueur ne doit
#  pas pouvoir retirer plus de 3 pierre et moins d’une pierre.
# Le joueur qui prend la dernière pierre gagne.
# Le programme doit vérifier après chaque tour si un joueur a gagné et il 
# vérifie que les joueurs entre un nombre de pierre correcte.


def pierre():
    _nbCailloux = 25 
    print(""" Chaque joueur vas devoir a tour de role, retirer entre 1 et 3 pierre du tat de 25 au départs
             Celui qui retireras la dernière pierre du paquets gagne la partie .
    
    """)
    _player1 = 0
    _player2 = 0
    _win = False 
    while _win != True :

        print("Le joueur 1 doit entrez combien de pierre il veut retirer (entre 1 et 3): ")
        _player1 = int(input("Combien ? :  "))

        if _player1 == 1 or _player1 == 2 or _player1 == 3:
            _nbCailloux -= _player1 
            print("Il reste ",_nbCailloux," dans le tat.")
            if _nbCailloux <= 0 :
                print("Le joueur 1 gagne la partie .")
                break
        else : 

            print("Mauvaise entrez, au joueur suivant .")
        _player1 = 0

        print("Le joueur 2 doit entrez combien de pierre il veut retirer (entre 1 et 3): ")
        _player2 = int(input("Combien ? :  "))

        if _player2 == 1 or _player2 == 2 or _player2 == 3:
            _nbCailloux -= _player2 
            print("Il reste ",_nbCailloux," dans le tat.")
            if _nbCailloux <= 0 :
                print("Le joueur 2 gagne la partie .")
                break
        else : 
            print("Mauvaise entrez, au joueur suivant .")
        _player2 = 0
