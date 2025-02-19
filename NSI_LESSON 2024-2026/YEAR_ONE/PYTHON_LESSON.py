import random
import math

#envoyer cadeau Cassie 

# ------------    LES NOMBRES DE 1 A 20 DANS PLUSIEURS BASES : ---------------------------------------------------------------------------------------------------------
#Base 2 (Binaire) : 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 0001 0000, 0001 0001, 0001 0010, 0001 0011
#Base 10 (Décimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
#Base 16 (Héxadécimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13

#Table des matières : 

#---------------------- 0 - Introduction : ---------------------------------------------------------------------------------------------------------------------------------------

#COURS : 
#Histoires de l'informatique : 
#Augusta Ada King, comtesse de Lovelace (1815-1852)/ Alan Mathison Turing (1912-1954)/ John Von Neumann (1903-1957)
#conçoit le premier langage informatique pour la machine à différences de Babbage/ 1936 construit mathématiquement la première machine universelle/ 1944 Architecture de von Neumann 
#«Informatique», mot-valise né de la contraction des mots «Information» et «Automatique».

#---------------------- I - Architecture materiel : ------------------------------------------------------------------------------------------------------------------------------
def COURS_Architecture_Materiel_I():

    chapitre_I_HISTOIRE_DES_ORDINATEURS = 0
    # -I- HISTOIRE DES ORDINATEURS : --------------------------

    #Machines à programmes externes : Machines électroniques

    #Tubes à vide 1942 Premier ordinateur électro mécanique (non achevé),
    #utilisation de tubes à vide bien plus rapides que les machines électromécanique.

    #Colossus 1944 est une série de calculateurs électroniques fondés sur le système binaire. Le premier,
    #Colossus Mark 1, est construit en l’espace de onze mois et 
    #opérationnel en décembre 1943 constitué de 1 500, puis 2 400 tubes à vide,
    #il accomplissait 5 000 opérations par seconde. 
    #Il était utilisé pendant la Seconde Guerre mondiale pour la cryptanalyse du code Lorenz.

    #Machines à programmes enregistrés : 

    #ENIAC 1945 effectue descalculs balistiques à l’aide de ses 18000 tubes à vides.

    chapitre_II_ARCHITECTURE_DE_VON_NEUMAN = 0 
    # -II- ARCHITECTURE DE VON NEUMAN : -----------------------

    #Les structures principales :
    #le CPU / La Mémoire / Les Bus (fils reliant les composant ) /Input Output

    #Un programme est enregistré dans la mémoire.
    #Les échanges entre la mémoire et les registres du CPU se font via des bus, 
    # selon une chronologie organisée par le contrôleur mémoire, en fonction du type d’échange 
    # (données ou adresses).

    #Le compteur de programme (CP) stocke l’adresse de l’instruction en cours, 
    # tandis que le registre d’instruction (RI) contient sa valeur. 
    # Les données du programme sont stockées dans les registres du banc de registres avant utilisation.

    #L’UAL (ou ALU) réalise les opérations arithmétiques et logiques en traitant 
    # les signaux électriques issus de ses circuits combinatoires.

    chapitre_III_MEMOIRE_ET_LANGUAGE_MACHINE = 0
    # -III- MEMOIRE ET LANGUAGE MACHINE : ---------------------

    #L’organisation de la mémoire : 
    #Les types de mémoire : 
    #Les registres : 
    #Mémoires centrales et mémoire cache : 
    #Jeu d’instructions:
    #Nature des instructions : 
    #Assembleur : 

    chapitre_IV_SYSTEME_D_EXPLOITATION = 0
    # -IV- SYSTEME D'EXPLOITATION : ---------------------------

    #Le système Linux : 
    #Le Bash : 
    return 0
#---------------------- II - Language de Programmation : --------------------------------------------------------------------------------------------------------------------------
def COURS_Language_de_Programmation_II():

    return 0
#---------------------- III - Representation des Données : ------------------------------------------------------------------------------------------------------------------------
def COURS_Representation_des_Données_III():
    #Conversion Binaire :

    #Note : ob = Base Binaire 
    #Note : od = Base décimal 
    #Note : ox = Base Héxadécimal 
    
    #ASCII : American Standard Code for Information Interchange : créer en 1961. coder sur 7 bits 
    #Unicode : codé sur 21 bits : +135 000 caractères différeznts 

    return 0
#----------- Programmes de cours et exercices : --------------------------------------------------------------------------------------------------------------------------
#----------- Nombre d'exercices : 17          : --------------------------------------------------------------------------------------------------------------------------

#Une fonction pour calculer une moyenne Général avec plusieurs coeficients 
def moyenne_Bac(_note1,_note2,_note3,_coef1,_coef2,_coef3):

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

#Une fonction pour calculer une moyenne de maths avec deux coeficients prédéfinis
def moyenne_math2(_note1,_note2,_note3,_note4,_note5):
    _math = (((_note1+_note2+_note3) / 3) + ((_note4+_note4+_note5+_note5)) / 4) /2

    return _math

#Une fonction pour appliquer la TVA sur un produit à partir du prix de base et du % de la TVA
def TVA(_prix,_tva):
    _newPrice = float(prix) * (1 + _tva/100)

    return _newPrice

#Une fonction pour connaitre son appréciation au Bac 
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

#Une fonction qui permet de determiner si l'utilisateur peut consommer de l'alcool grâce au structures conditionelles 
def alcool():

    _enceinte = 0
    _age = int(input("entrez votre age: "))

    _sexe_femme = input("si vous êtes une femme entrez : oui : ")
    if _agesexe_femme == "oui":
        _sexe_femme = True

    if _sexe_femme == True:
        _enceinte = input("si vous êtes enceinte écrivez : oui: ")
    if _enceinte == "oui":
        _enceinte = True


    if _age <= 17.99 : 
        print("non trop petit")

    if _sexe_femme == True and _enceinte == True:
        print("non pas bon pour le bébé")
    if _age >= 18 and _enceinte != "oui" :
        print("oui c'est bon")
        
#Une fonction pour calculer l'évolution de la valeur d'une maison sur 15 ans
def InflationMaison15():
    _prix_base = 206000
    _nb_années = 15
    _inflations = 1 + (3/100)

    for i in range (_nb_années):
        print(_prix_base * _inflations)   
        _prix_base = _prix_base * _inflations
    return _prix_base

#Une fonction pour calculer l'évolution de la valeur d'une maison après un certains nombre d'années
def InflationMaison(_valeur, _année):
    _prix_base = _valeur
    _nb_années = _année
    _inflations = 1 + (3/100)

    for i in range (_nb_années):
        print(_prix_base * _inflations)   
        _prix_base = _prix_base * _inflations
    return _prix_base

#Une fonction qui retourne la longueur d'une chaine de caractère donnée
def lenght(_chaine):
    _chaine = str(_chaine)
    _lenght = 0
    for i in _chaine:
        _lenght += 1

    return(_lenght)

#exo cours 28/11/2024
#Une fonction pour afficher tout les chiffres de 1 a 100
def hundred():
    for i in range(101):
        print(i)

#Une fonction pour afficher toute les secondes,minutes et heures d'une journée
def hour():
    for b in range(24):
        for a in range(60):
            for i in range(60):
                print("h",b,"m",a,"s",i)

#Une fonction qui permet d'afficher tout les jours de la semaine sur une durée de 4 semaines
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

#Exo cours 4/12/2024 : Boucle Borné et non Borné
#Une fonction qui permet de detecter toute les voyelles d'une chaine de caractère fournis
def voyelleDansMot(_mots):

    for i in _mots:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "Y":
            print("voyelle :" + i )
        else : 
            print("autres : " + i )

    #faut parcourir des choses avec les boucles for

#Une fonction qui permet de demander a un utilisateur de resoudre le calcul 5 fois 6 (exercice de cours)
def tableMultiplication():
    _reponse = 0
    _chiffre1 = 5
    _chiffre2 = 6
    while _reponse != _chiffre1 * _chiffre2 : 
        _reponse = int(input("combien fond 5 fois 6 ?"))
    print("gg")

#Une fonction qui permet de se tester sur ses tables de multiplications
def tableMultiplicationRandom():
    _rejouer = "oui"

    while _rejouer == "oui":
        _reponse = 0
        _chiffre1 = random.randint(1,9)
        _chiffre2 = random.randint(1,9)
        _question = "combien fond " + str(_chiffre1) + " fois " + str(_chiffre2) + " ?  "
        while _reponse != _chiffre1 * _chiffre2 : 

            _reponse = int(input(_question))
        print("Bravo")
        _rejouer = input("Ecrivez oui si vous voulez rejouer : ")

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
    _result = 0
    return _result

#Cette fonction devra permettre a partir d'un numéro de carte vital, d'en obtenir des informations
def carteVitalAnalyse(_num):
    _num = int(_num)
    return 0

#A faire : 

#Ajouer une section pour les convention d'écriture vu en cours:
# les _underscore pour les variables interne au fonctions 
# LaManièreDeNommerLesVariables

#Ajouter une section qui liste chaque fonction du fichier (a la fin de celui ci)
#avec des renseignements comme : Nom, paramètres, utilité, nombre de ligne dans la fonction.
