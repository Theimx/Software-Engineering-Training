import random
import math

# ---------- - -    LES NOMBRES DE 1 A 20 DANS PLUSIEURS BASES : - - ---------------------------------------------------------------------------------------------------------
#Base 2 (Binaire) : 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 0001 0000, 0001 0001, 0001 0010, 0001 0011
#Base 10 (Décimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
#Base 16 (Héxadécimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Terminal spé NSI

# Epreuves Pratiques -BNS 2025- sujet n°42 
def nb_repetions(elt,tab):
    if tab :
        count = 0 
        for x in tab:   #Parcours séquentiel de la liste
            if elt == x:
                count += 1 
        return(count)
    return()

def binaire(a):
    """convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de charactères."""
    if a == 0:
        return '0'
    bin_a = ""
    while a > 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

# Epreuves Pratiques -BNS 2025- sujet n°13
def recherche(elt,tab):
    if tab : 
        for i in range(len(tab)):
            if tab[i] == elt:
                return(i)
    return()

def insert(tab,a):
    """ 
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le 
    nouveau tableau.
    """
    tab_a = [ a ] + tab #nouveau tableau contenant a suivi des éléments de tab

    i = 0
    while i < len(tab_a) and a > tab_a[i+1] :
        tab_a[i] = tab_a[i+1]
        tab_a[i+1] = a
        i = i + 1
    return tab_a

# Epreuves Pratiques -BNS 2025- sujet n°48
def recherche48(tab,n):
    for i in range((len(tab)-1),0,-1): # Parcourirs la liste depuis la fin a la recherche 
        print(i)                       # de notre  valeur et renvoier son indice.
        if n == tab[i]:
            return(i)

def distance_carre48(point1,point2):
    """ Calcule et renvoie la distance au carre entre 
        deux points."""
    return( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )

def point_le_plus_proche48(depart,tab):
    """ Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    
    min_point = tab[0]
    min_dist = distance_carre48(tab[0],depart)
    for i in range(1,len(tab)):
        if distance_carre48(tab[i],depart) < min_dist : 
            min_point = tab[i]
            min_dist = distance_carre48(tab[i],depart)

    return min_point

# Epreuves Pratiques -BNS 2025- sujet n°27
def verifie27(tab):
    for i in range(1,len(tab)-1,1):
        if tab[i-1] > tab[i]:
            return False
    return True

def puissance_rec(x,n): # Vas créer une pile de multiplication en attente qui
                        # se résoudront une fois le compteur n atteint en remontant
                        # la pile avec x * 1 puis x * x ect en valeur de retour
    if n == 0:
        return 1
    else : 
        return x * puissance_rec(x,n-1)

def puissance_rec_iterative(x,n): # complexité temporelle linéaire et 
    r = 1                         # complexité  spacial constante
    for i in range(n):
        r = r * x
    return r

def Iter(n):
    for i in range(1,n+1):
        print(i)

def rec(n):
    if n == 1 :
        print(1)
    else : 
        rec(n-1)
        print(n)

def factorielle_iter(n):
    res = 1
    for i in range(1,n+1):
        res = res *i
    return res

def factorielle_recu(n):
    if (n == 0) or (n == 1) :
        return(1)
    else : 
        return n * factorielle_recu(n-1)

def sumlist(tab):
    total = 0
    for i in tab:
        total += i
    return(total)

def extrsousliste(tab,a,b):
    if a < 0 : 
        a = 0
    if b > len(tab):
        b = len(tab)
    return [tab[i] for i in range(a,b)]
    # Liste par comp remplace :
    # tab = []
    # for i in range(a,b):
    #     tab.append(tab[i])
    # return tab

def recSumList(tab):
    if tab :
        return tab[0] + recSumList(extrsousliste(tab,1,len(tab)-1))
    return False

def recSumList2(tab):
    if tab : 
        temp = tab.copy
        x = temp.pop()
        return recSumList2(temp) + x
    return 0

def recFibonacci(n):

    if (n == 1) or (n ==0):
        return 1
    else : 
        return(recFibonacci(n-1) + recFibonacci(n-2))

