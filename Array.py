class EmptyCell:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value is None:
            return "#"
        else:
            return str(self.value)

def CreateArray(n, name, nb_line):
    tableau = {name: []}  # Initialise la liste principale avec un nom donné
    for _ in range(n):
        nouvelle_liste = [EmptyCell() for _ in range(nb_line)]  # Crée une liste avec des objets EmptyCell
        tableau[name].append(nouvelle_liste)  # Ajoute la nouvelle liste à 'tableau'
    return tableau

def ajout(element, indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = element
                print(f"L'élément '{element}' a été ajouté à la case {indice_objet} de la liste {indice_liste} de '{tableau_name}'.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

def del_cells(indice_liste, indice_objet, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            if indice_objet < len(tableau[tableau_name][indice_liste]):
                tableau[tableau_name][indice_liste][indice_objet].value = None
                print(f"La case {indice_objet} de la liste {indice_liste} de '{tableau_name}' a été vidée.")
            else:
                print(f"L'indice d'objet spécifié est hors de la plage de '{tableau_name}[{indice_liste}]'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

# Fonction pour afficher le tableau avec un espacement égal pour tous les éléments
def afficher_tableau(tableau):
    max_length = 0  # Longueur maximale des éléments dans le tableau
    for key, value in tableau.items():
        for liste in value:
            for cellule in liste:
                cellule_length = len(str(cellule))
                if cellule_length > max_length:
                    max_length = cellule_length

    for key, value in tableau.items():
        print(f"{key}:")
        for liste in value:
            for cellule in liste:
                cellule_str = str(cellule)
                espacement = " " * ((max_length - len(cellule_str)) // 2)
                print(f"{espacement}{cellule_str}{espacement}", end=" ")
            print()
        print()

# Exemple d'utilisation :
nom_tableau = input("Entrez un nom pour le tableau : ")
nombre_de_listes = int(input("Entrez le nombre de listes : "))
nombre_d_objets = int(input("Entrez le nombre d'objets à ajouter dans chaque liste : "))
resultat = CreateArray(nombre_de_listes, nom_tableau, nombre_d_objets)
print("Tableau initial:")
afficher_tableau(resultat)

element_a_ajouter = input("Entrez l'élément à ajouter : ")
indice_liste_a_modifier = int(input("Entrez l'indice de la liste où ajouter l'élément : "))
indice_objet_a_modifier = int(input("Entrez l'indice de l'objet où ajouter l'élément : "))

ajout(element_a_ajouter, indice_liste_a_modifier, indice_objet_a_modifier, nom_tableau, resultat)
print("\nTableau après ajout:")
afficher_tableau(resultat)

indice_liste_a_vider = int(input("Entrez l'indice de la liste à vider : "))
indice_objet_a_vider = int(input("Entrez l'indice de l'objet à vider : "))

del_cells(indice_liste_a_vider, indice_objet_a_vider, nom_tableau, resultat)
print("\nTableau après suppression de la cellule spécifiée :")
afficher_tableau(resultat)
