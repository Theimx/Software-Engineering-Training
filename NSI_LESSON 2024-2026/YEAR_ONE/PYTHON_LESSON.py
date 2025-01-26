#Conversion Binaire :

#Note : ob = Base Binaire 
#Note : od = Base décimal 
#Note : ox = Base Héxadécimal 

#lagomorphes,myxomatose

#Exo I : 

def moyenne_Bac(_note1,_note2,_note3,_coef1,_coef2,_coef3,):

    _moyenneG = 0
    _coefG = 0 
    _moyenneG = _moyenneG + _note1 * _coef1
    _coefG += _coef1
    _moyenneG = _moyenneG + _note2 * _coef2 
    _coefG += coef2 
    _moyenneG = _moyenneG + _note3 * _coef3 
    _coefG += coef3 

    _bac = _moyenneG /_coefG

    return _bac

def moyenne_math2(_note1,_note2,_note3,_note4,_note5):
    _math = (((_note1+_note2+_note3) / 3) + ((_note4+_note4+_note5+_note5)) / 4) /2

    return _math

def TVA(_prix,_tva):
    _newPrice = float(prix) * (1 + _tva/100)

    return _newPrice

def bach(_note):
    _Bac = float(note)

    if _Bac <= 7.99:
        print("Refusé")
    elif _Bac >= 8 and _Bac <= 9.99 : 
        print("Ratrapage")
    elif _Bac >= 10 and _Bac <= 11.99:
        print("Bac sans mention")
    elif _Bac >= 12 and _Bac <= 13.99:
        print("Mention Assez bien")
    elif _Bac >= 14 and _Bac <= 15.99:
        print("Bien ")
    elif _Bac >= 16 and _Bac <= 17.99:
        print("Très bien")
    elif _Bac >= 18 and _Bac <= 21:
        print("Felicitation")

    else : 
        print("non")

#Exo II : 

def alcool():

    enceinte = 0
    age = int(input("entrez votre age: "))

    sexe_femme = input("si vous êtes une femme entrez : oui : ")
    if sexe_femme == "oui":
        sexe_femme = True

    if sexe_femme == True:
        enceinte = input("si vous êtes enceinte écrivez : oui: ")
    if enceinte == "oui":
        enceinte = True


    if age <= 17.99 : 
        print("non trop petit")

    if sexe_femme == True and enceinte == True:
        print("non pas bon pour le bébé")
    if age >= 18 and enceinte != "oui" :
        print("oui c'est bon")
        
#Exo III: 

def maison():
    _prix_base = 206000
    _nb_années = 15
    _inflations = 1 + (3/100)

    for i in range (_nb_années):
        print(_prix_base * _inflations)   
        _prix_base = _prix_base * _inflations
    return _prix_base

#exo IV : 

def taille_chaine(_chaine):
    return int(len(str(_chaine)))

#exo cours 28/11

def hundred():
    for i in range(101):
        print(i)

def hour():
    for b in range(24):
        for a in range(60):
            for i in range(60):
                print("h",b,"m",a,"s",i)

def week():
    for a in range(4):
        for i in range(7):
            if i == 0:
                print("jour", i+1, "semaine" ,a+1, "donc Samedi")
            if i == 1:
                print("jour", i+1, "semaine" ,a+1,"donc Dimanche")
            if i == 2:
                print("jour", i+1, "semaine" ,a+1,"donc Lundi")
            if i == 3:
                print("jour", i+1, "semaine" ,a+1,"donc Mardi")
            if i == 4:
                print("jour", i+1, "semaine" ,a+1,"donc Mercredi")
            if i == 5:
                print("jour", i+1, "semaine" ,a+1,"donc Jeudi")
            if i == 6:
                print("jour", i+1, "semaine" ,a+1,"donc Vendredi")

#Exo cours 4/12 : Boucle Borné et non Borné

def voyelledansmot(_mots):

    for i in _mots:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
            print("voyelle :" + i )
        else : 
            print("autres : " + i )

    #faut parcourir des choses avec les boucles for

def tablemultiplication():
    _reponse = 0
    _chiffre1 = 5
    _chiffre2 = 6
    while _reponse != _chiffre1 * _chiffre2 : 
        _reponse = int(input("combien fond 5 fois 6 ?"))
    print("gg")


