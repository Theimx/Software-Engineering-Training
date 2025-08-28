from math import *
# from random import *
import matplotlib.pyplot as plt
# import numpy as np
# from scipy.stats import linregress

# Données de type 1
liste_x_1=[1,3,8,13]
liste_y_1=[28,27.2,37.6,40.7]

# Données de type 2
liste_x_2=[2,3,10,15]
liste_y_2=[30,26,39,35.5]

plt.axis([0,15, 0, 50]) # Attention [x1,x2,y1,y2]
plt.axis('equal')
plt.xlabel('Caractéristique 1')
plt.ylabel('Caractérstique 2')
plt.title('Représentation des deux types')
plt.grid()
plt.scatter(liste_x_1,liste_y_1, label='type 1')
plt.scatter(liste_x_2,liste_y_2, label='type 2')

plt.scatter(7,28.4, label='cible')
plt.legend()
plt.show()

table = [['t1',1,28], ['t1',3,27.2], ['t1',8,37.6], ['t1',13,40.7], ['t2',2,30], ['t2',3,26], ['t2',10,39], ['t2',15,35.5]]
cible = [7,28.4]
k=3


def k_plus_proches_voisins(table, cible, k) :
    """Revoie la liste des k plus proches voisins de la cible"""
    
    
    def distance_cible(donnee) :
        """ renvoie la distance entre la donnée et la cible, on choisit la distance de Manhattan"""
        
        distance = abs(donnee[1]-cible[0])+abs(donnee[2]-cible[1])
        
        return distance
    
    table_triee = sorted(table, key = distance_cible)
    
    proches_voisins = []
    
    for i in range(k) : 
        proches_voisins.append(table_triee[i])
        
    return proches_voisins

print("La liste des ",k," plus proches voisins de la cible : ",k_plus_proches_voisins(table,cible,k))
