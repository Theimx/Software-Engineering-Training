import math

def rect(_longueur,_largeur,_hauteur):
    return _hauteur * (_largeur * _longueur)

def carre(_cote,_hauteur):
    return _hauteur * (_cote * _cote)

def cercle(_diametre):
    return 2 * math.pi * (_diametre/2)

def prestation(_shape):
    _price = 0
    