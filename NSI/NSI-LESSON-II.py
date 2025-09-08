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