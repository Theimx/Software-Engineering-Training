import random

def tablemultiplication():
    _rejouer = "oui"

    while _rejouer == "oui":
        _reponse = 0
        _chiffre1 = random.randint(1,9)
        _chiffre2 = random.randint(1,9)
        _question = "combien fond " + str(_chiffre1) + " fois " + str(_chiffre2) + " ?  "
        while _reponse != _chiffre1 * _chiffre2 : 

            _reponse = int(input(_question))
        print("gg")
        _rejouer = input("Ecrivez oui si vous voulez rejouer : ")

def cartevital():
    _sexe = int(input("entrez : 1 si vous êtes un Garçon ou 2  si vous êtes une fille : "))

    if _sexe == 1 or _sexe == 2 : 
        _annaissance = int(input("entrez les deux derniers chiffres de votre année de naissance (ex 07) : "))

        if _annaissance < 99 or _annaissance > 0:
            _moisnaissance = int(input("entrez votre mois de naissance (ex 05) : "))

            if _moisnaissance <= 12 or _moisnaissance >= 1:
                _departement = int(input("entrez le numero de votre departement de naissance ou 99 si vous êtes née a l'etranger : "))

                if _departement < 99 or _departement > 0:
                    _code1 = random.randint(0,999)
                    _code2 = random.randint(0,999)
                    _securiteSocial = str(_sexe)  + str(_annaissance)  + str(_moisnaissance) + str(_departement)  + str(_code1) + str(_code2)
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


cartevital()
