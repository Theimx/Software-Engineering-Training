#Une fonction qui permet de créer un numéro de sécurité social unique a partir d'information entré par l'utilisateur.
def carteVital():
    _sexe = int(input("entrez : 1 si vous êtes un Garçon ou 2  si vous êtes une fille : "))

    if _sexe == 1 or _sexe == 2 : 
        _annaissance = int(input("entrez les deux derniers chiffres de votre année de naissance (ex 07) : "))

        if _annaissance < 99 or _annaissance > 0:
            _moisnaissance = int(input("entrez votre mois de naissance (ex 05) : "))

            if _moisnaissance <= 12 or _moisnaissance >= 1:
                _departement = int(input("entrez le numero de votre departement de naissance ou 99 si vous êtes née a l'etranger : "))

                if _departement < 99 or _departement > 0:

                    _code1 = random.randint(100,999)
                    _code2 = random.randint(100,999)
                    if _annaissance <= 9 : 
                        _annaissance = '0' + str(_annaissance)
                    if _moisnaissance <= 9 : 
                        _moisnaissance = '0' + str(_moisnaissance)
                    if _departement <= 9 : 
                        _departement = '0' + str(_departement)

                    _securiteSocial = str(_sexe)  + str(_annaissance)  + str(_moisnaissance) + str(_departement)  + str(_code1) + str(_code2)
                    int(_securiteSocial)
                    print(_securiteSocial)

                    _securiteSocial = int(_securiteSocial)
                    return _securiteSocial
                else : 
                    cartevital()
            else : 
                cartevital()
        else : 
            cartevital()
    else : 
        cartevital()

#A refaire avec les boucles while, Refaire une version optimisé de celle du dessus et coder La fonction 
#inverse (A partir d'un numéro de carte, renvoyer une liste d'information deduis de celui ci.)
def carteVitalBoucle(): 
    _sexe = 0
    _annaissance = 1000

    while _sexe != 1 and _sexe !=2:
        _sexe = int(input("entrez : 1 si vous êtes un Garçon ou 2  si vous êtes une fille : "))
    
    while _annaissance > 99 and _annaissance < 0:
        _annaissance = int(input("entrez les deux derniers chiffres de votre année de naissance (ex 07) : "))

    _result = str(_sexe) + str(_annaissance)
    return _result


print(carteVitalBoucle())