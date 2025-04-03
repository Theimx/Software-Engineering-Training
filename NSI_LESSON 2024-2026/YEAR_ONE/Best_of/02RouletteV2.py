import random

# Proposer une fonction pour le jeux de la roulette
# L’utilisateur possède 60 jetons, a chaque manche, il peut parier sur 1 a 3 cases. Chaque pari consomme un jeton.
# Si l’utilisateur gagne en ayant parié sur 1 case, il gagne 10 jetons.
# Si l’utilisateur gagne en ayant parié sur 2 cases, il gagne 6 jetons
# Si l’utilisateur gagne en ayant parié sur 3 case il gagne 4 jetons
# Si l’utilisateur choisie de parier sur 0 case, c’est qu’il souhaite s’arrêter.
# L’ordinateur doit générer un nombre aléatoire compris entre 1 et 25
# Le jeux continue tant que l’utilisateur le souhaite ou si ses jetons sont épuisées 
# Le logiciel ne faite pas de vérification sur le nombre de jeton pariés.
#25 cases

# https://www.quiziniere.com/diffusions/ZJXLPN/copie/PDM

def roulette():
    _banque = 60 
    _rejouer = True
    

    while _rejouer == True:

        _num = random.randint(1,25)
        _nbParis = int(input("entrez combien de pari vous souhaitez réalisez Maximum 3 (0 si vous ne souhaitez pas jouer): "))
        _banque -= 1
        print("Vous avez depensez 1 jetons pour réaliser votre paris")

        if _nbParis == 0 :
            print("Bonne continuation, score : ",_banque)
            break

        if _nbParis == 1 :
            print(_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))

            if _reponse == _num :
                _banque += 10
                print("Vous avez gagnez, 10 jetons ont été ajouter a votre Banque .")
                print(" ")

        elif _nbParis == 2 :
            print(_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))
            _reponse2 = int(input("entrez un second nombre entre 1 et 25 : "))

            if _reponse == _num or _reponse2 == _num:
                _banque += 6
                print("Vous avez gagnez, 6 jetons ont été ajouter a votre Banque .")
                print(" ")

        elif _nbParis == 3 :
            print("debug reponse (c'est pas un oublie je vous la laisse pour que vous testiez ): ",_num)
            _reponse = int(input("entrez un nombre entre 1 et 25 : "))
            _reponse2 = int(input("entrez un second nombre entre 1 et 25 : "))
            _reponse3 = int(input("entrez un troisième nombre entre 1 et 25 : "))

            if _reponse == _num or _reponse2 == _num or _reponse3 == _num:
                _banque += 4
                print("Vous avez gagnez, 4 jetons ont été ajouter a votre Banque .")
                print(" ")
