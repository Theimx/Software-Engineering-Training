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

ad_cell(element_a_ajouter, indice_liste_a_modifier, indice_objet_a_modifier, nom_tableau, resultat)
print("\nTableau après ajout:")
afficher_tableau(resultat)


indice_liste_a_recuperer = int(input("Entrez l'indice de la liste à récupérer : "))
liste_recuperee = get_row(indice_liste_a_recuperer, nom_tableau, resultat)
print(f"\nListe récupérée de '{nom_tableau}[{indice_liste_a_recuperer}]':")
print(liste_recuperee)

indice_liste_a_recupererbis = int(input("Entrez l'indice de la liste à récupérer : "))
liste_recupereebis = get_row(indice_liste_a_recupererbis, nom_tableau, resultat,exclude_empty=True)
print(f"\nListe récupérée de '{nom_tableau}[{indice_liste_a_recupererbis}]':")
print(liste_recupereebis)

indice_liste_a_lire = int(input("Entrez l'indice de la liste à lire : "))
indice_objet_a_lire = int(input("Entrez l'indice de l'objet à lire : "))

valeur_lue = get_cells(nom_tableau, indice_liste_a_lire, indice_objet_a_lire, resultat)
print(valeur_lue)

coll_test1 = int(input("Entrez l'indice de la liste à lire : "))
coll_test = get_coll(nom_tableau,coll_test1, resultat)
print(coll_test)

indice_liste_a_vider = int(input("Entrez l'indice de la liste à vider : "))

del_row(indice_liste_a_vider, nom_tableau, resultat)
print("\nTableau après suppression de la liste spécifiée :")
afficher_tableau(resultat)
