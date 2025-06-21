#les listes : partie 3

#debug : 
def prtlist(L):
    result = []
    for i in L:
        result.append(i)
    return result

#Exercice 1 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, 
#détermine le nombre maximum d’occurrences consécutives strictement supérieures à 10. 
#Proposer deux versions de ce programme l'une avec une gestion des index et une autre sans.

def exercice1(L): #exercice valider
    best_score = 0
    current_best_score = 0

    for i in range(len(L)):
        if i > 10: 
            current_best_score += 1

        if current_best_score >= best_score:
            best_score = current_best_score     

    return best_score

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,3,10,11,12,12,12,18]
num2 = [4,5,7]
print(exercice1(num))
print(exercice1(num2))

#Exercice 2 : Ecrire une fonction qui à partir d'une liste de nombres entiers, 
#détermine l'écart maximum entre deux valeurs consécutives. Proposer deux versions de ce programme 
#l'une avec une gestion des index et une autre sans.

def exercice2(L):
    ecarts = 0
    max_ecarts = 0

    return max_ecarts

#Exercice 3 : Ecrire une fonction, qui à partir d'une liste de nombres entiers,
#décale les éléments de cette liste d'un élément vers la droite (décalage circulaire, 
#le dernier élément se retrouve alors en premier)

#Exercice 4 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, 
#décale les éléments de cette liste d'un élément vers la gauche (décalage circulaire, 
#le premier élément se retrouve alors en dernier)

#Exercice 5 : Ecrire une fonction, qui à partir d'une liste de nombres entiers d'une valeur x et d'un index i,
#insére la valeur x à l'index i sans utiliser la méthode insert().

#Exercice 6 : Ecrire une fonction, qui à partir d'une liste de nombres entiers,
#détermine si la liste est croissante. La fonction retourne un booléen.

#Exercice 7 : Ecrire une fonction, qui à partir d'une liste de nombres entiers, 
#détermine la plus longue succession ininterrompue de valeurs rangées dans l’ordre croissant

#Exercice 8 : Ecrire une fonction,qui à partir de deux listes croissantes de taille quelconque,
#construit une liste croissante.

#Exercice 9 : Ecrire une fonction qui construit une liste de 8 éléments contenant 
#aléatoirement les valeurs de 1 à 8, chaque valeur devant etre unique.

#Exercice 10 : Ecrire une fonction, qui à partir de deux listes de nombres entiers,
#détermine le nombre d'éléments présents dans les deux listes. Proposer deux versions, 
#l'une avec l'opérateur in et l'autre sans.

#Exercice 11 : Écrire une fonction, qui à partir d'une matrice contenant des nombres entiers 
#implémentée par une liste de listes, ajoute une dernière colonne contenant la moyenne de chaque ligne 
#(attention les sous listes peuvent avoir des tailles variables)

#Exercice 12 : Écrire une fonction, qui à partir d'une matrice contenant des nombres entiers implémentée 
#par une liste de listes, ajoute une dernière ligne contenant le nombre de valeurs paires de chaque colonne.

#Exercice 13 : Ecrire une fonction, qui à partir d'une matrice 3x4 implémentée par une liste de listes, 
#construit une liste de 12 élements contenant successivement les éléments de la matrice, ligne par ligne.

#Exercice 14 : Ecrire une fonction, qui à partir d'une matrice 3x4 implémentée par une liste de listes, 
#construit une liste de 12 élements contenant successivement les éléments de la matrice, colonne par colonne.

#Exercice 15 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, 
#vérifie qu'il existe au moins une ligne où tous les éléments ont la meme valeur.

#Exercice 16 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, 
#vérifie qu'il existe au moins une colonne où tous les éléments ont la meme valeur.

#Exercice 17 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, 
#vérifie que tous les éléments ont des valeurs différentes.

#Exercice 18 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, 
#met à 0 tous les éléments d'une ligne si la somme de ces éléments est un multiple de 5.

#Exercice 19 : Ecrire une fonction, qui à partir d'une matrice 3x3 implémentée par une liste de listes, 
#met à 0 tous les éléments d'une colonne si la somme de ces éléments un multiple de 5.

#Exercice 20 : Ecrire une fonction, qui à partir d'une matrice 3x5 implémentée par une liste de listes, 
#permutent les lignes et les colonnes pour ainsi obtenir une matrice 5x3.
