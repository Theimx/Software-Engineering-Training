def CreateArray(n, name):
    tableau = {name: []}  # Initialise la liste principale avec un nom donné
    for _ in range(n):
        nouvelle_liste = []  # Crée une nouvelle liste vide
        tableau[name].append(nouvelle_liste)  # Ajoute la nouvelle liste à 'tableau'
    return tableau

def ajout(element, indice_liste, tableau_name, tableau):
    if tableau_name in tableau:
        if indice_liste < len(tableau[tableau_name]):
            tableau[tableau_name][indice_liste].append(element)
            print(f"L'élément '{element}' a été ajouté à la liste {indice_liste} de '{tableau_name}'.")
        else:
            print(f"L'indice de liste spécifié est hors de la plage de '{tableau_name}'.")
    else:
        print(f"Le nom '{tableau_name}' n'existe pas dans le tableau.")

# Exemple d'utilisation :
nom_tableau = input("Entrez un nom pour le tableau : ")
nombre_de_listes = int(input("Entrez le nombre de listes : "))
resultat = CreateArray(nombre_de_listes, nom_tableau)
print(resultat)

element_a_ajouter = input("Entrez l'élément à ajouter : ")
indice_liste_a_modifier = int(input("Entrez l'indice de la liste où ajouter l'élément : "))

ajout(element_a_ajouter, indice_liste_a_modifier, nom_tableau, resultat)
print(resultat)