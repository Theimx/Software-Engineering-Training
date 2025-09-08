# Epreuves Pratiques -BNS 2025- sujet n°1

# Epreuves Pratiques -BNS 2025- sujet n°2

# Epreuves Pratiques -BNS 2025- sujet n°3

# Epreuves Pratiques -BNS 2025- sujet n°4

# Epreuves Pratiques -BNS 2025- sujet n°5

# Epreuves Pratiques -BNS 2025- sujet n°6

# Epreuves Pratiques -BNS 2025- sujet n°7

# Epreuves Pratiques -BNS 2025- sujet n°8

# Epreuves Pratiques -BNS 2025- sujet n°9

# Epreuves Pratiques -BNS 2025- sujet n°10

# Epreuves Pratiques -BNS 2025- sujet n°11

# Epreuves Pratiques -BNS 2025- sujet n°12

# Epreuves Pratiques -BNS 2025- sujet n°13
def recherche13(elt : int,tab : list):
    if tab : 
        for i in range(len(tab)):
            if tab[i] == elt:
                return(i)
    return()

def insert13(tab,a):
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

# Epreuves Pratiques -BNS 2025- sujet n°14

# Epreuves Pratiques -BNS 2025- sujet n°15

# Epreuves Pratiques -BNS 2025- sujet n°16

# Epreuves Pratiques -BNS 2025- sujet n°17

# Epreuves Pratiques -BNS 2025- sujet n°18

# Epreuves Pratiques -BNS 2025- sujet n°19

# Epreuves Pratiques -BNS 2025- sujet n°20

# Epreuves Pratiques -BNS 2025- sujet n°21

# Epreuves Pratiques -BNS 2025- sujet n°22

# Epreuves Pratiques -BNS 2025- sujet n°23

# Epreuves Pratiques -BNS 2025- sujet n°24

# Epreuves Pratiques -BNS 2025- sujet n°25

# Epreuves Pratiques -BNS 2025- sujet n°26

# Epreuves Pratiques -BNS 2025- sujet n°27

# Epreuves Pratiques -BNS 2025- sujet n°28

# Epreuves Pratiques -BNS 2025- sujet n°29

# Epreuves Pratiques -BNS 2025- sujet n°30

# Epreuves Pratiques -BNS 2025- sujet n°31

# Epreuves Pratiques -BNS 2025- sujet n°32

# Epreuves Pratiques -BNS 2025- sujet n°33

# Epreuves Pratiques -BNS 2025- sujet n°34

# Epreuves Pratiques -BNS 2025- sujet n°35

# Epreuves Pratiques -BNS 2025- sujet n°36

# Epreuves Pratiques -BNS 2025- sujet n°37

# Epreuves Pratiques -BNS 2025- sujet n°38

# Epreuves Pratiques -BNS 2025- sujet n°39

# Epreuves Pratiques -BNS 2025- sujet n°40

# Epreuves Pratiques -BNS 2025- sujet n°41

# Epreuves Pratiques -BNS 2025- sujet n°42 
def nb_repetions42(elt,tab):
    if tab :
        count = 0 
        for x in tab:   #Parcours séquentiel de la liste
            if elt == x:
                count += 1 
        return(count)
    return()

def binaire42(a):
    """convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de charactères."""
    if a == 0:
        return '0'
    bin_a = ""
    while a > 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

# Epreuves Pratiques -BNS 2025- sujet n°43 

# Epreuves Pratiques -BNS 2025- sujet n°44

# Epreuves Pratiques -BNS 2025- sujet n°45

# Epreuves Pratiques -BNS 2025- sujet n°46

# Epreuves Pratiques -BNS 2025- sujet n°47

# Epreuves Pratiques -BNS 2025- sujet n°48
def recherche48(tab,n):
    for i in range(0,(len(tab)-1),-1): # Parcourirs la liste depuis la fin a la recherche 
        print(i)                       # de notre  valeur et renvoier son indice.
        if n == tab[i]:
            return(i)
print(recherche48([5,3,3],3))