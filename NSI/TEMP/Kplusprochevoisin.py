import math

data = [ [65.75, 112.99], [71.52, 136.49], [69.40, 153.03], [68.22, 142.34],
         [67.79, 144.30], [68.70, 123.30], [69.80, 141.49], [70.01, 136.46],
         [67.90, 112.37], [66.49, 127.45] ]

def knn(donnees, point, k):
    distances_voisins = [ ]
    for index, sample in enumerate(donnees) :
        #On calcule toutes les distances entre les données et le point
        distance = distance_euclidienne(sample, point)
        #On stocke la distnce et l'index des voisins
        distances_voisins.append((distance, index))
    #on trie la liste selon la distance
    distances_voisins = sorted(distances_voisins)
    #On garde les k plus proches
    indices_des_k_voisins = [ index for distance, index in distances_voisins[:k]]
    #A partir des indices on retourne les k plus proches points des données
    return indices_des_k_voisins

def distance_euclidienne(point1, point2) :
    distance_carre = 0
    for i in range(len(point1)):
        distance_carre += (point1[i] - point2[i])**2
    return math.sqrt(distance_carre)


cible = [70, 140]
trois_plus_proches_voisins = knn(data, cible, 3)
print(trois_plus_proches_voisins)

for i in trois_plus_proches_voisins :
    print(data[i])


point_A = [1, 2.5, 3]
point_B = [0, -2, 6.3]
print(distance_euclidienne(point_A , point_B))

