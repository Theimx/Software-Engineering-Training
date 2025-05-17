# Evalutaion de rattrapage de NSI du 15/05/2025
# Classe de 1 ere 
# Note : 20/20

#Exercice 1 : 

def nb_mot(_chaine): 
    if _chaine :
        total = 0 
        for i in _chaine:
            if i == " " or i == "'":
                total += 1 
        return(total)
    return(0)

#print(nb_mot(" J'aime la NSI")) # >>>  4

#Exercice 2 : 
def Minmax(tab):
    mini = tab[0]
    maxi = tab[0]
    for i in tab:
        if i >= maxi :
            maxi = i
        if i <= mini :
            mini = i
    return(mini,maxi,(maxi-mini))

#print(Minmax([1,4,6,8,19,4,2,0]))  # >>> (0, 19, 19)