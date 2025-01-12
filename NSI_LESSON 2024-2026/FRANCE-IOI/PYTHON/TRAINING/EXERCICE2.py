import math

#Liste des exercices obligatoires du Niveau 2 sur le site France-IOI 
#https://www.france-ioi.org/algo/chapters.php

#exo 1

actual_tax = float(input()) / 100
new_tax = float(input()) / 100
price_ttc = float(input())
price_ht = price_ttc / (1 + actual_tax)
new_price_ttc = price_ht * (1 + new_tax)
print(round(new_price_ttc, 2))

#exo 2

money = float(input())
book = float(input())
print(round((money//book)))

#or 
print(round(float(input())//float(input())))