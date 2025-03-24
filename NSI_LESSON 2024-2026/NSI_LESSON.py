import random
import math

# ---------- - -    LES NOMBRES DE 1 A 20 DANS PLUSIEURS BASES : - - ---------------------------------------------------------------------------------------------------------
#Base 2 (Binaire) : 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111, 0001 0000, 0001 0001, 0001 0010, 0001 0011
#Base 10 (Décimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
#Base 16 (Héxadécimal) : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def COURS_Introduction():

    # Histoire de l'informatique : 

    # - 1. Augusta Ada King, comtesse de Lovelace (1815-1852): a conçu le premier algorithme 
    #      destiné à être exécuté par une machine, en 1842-1843, dans ses notes sur la machine 
    #      analytique de Charles Babbage.
    # 
    # - 2. Alan Mathison Turing (1912-1954): 1936 construit mathématiquement la première machine universelle
    # - 3. John Von Neumann (1903-1957): 1944 Architecture de von Neumann 

    # - «Informatique», mot-valise né de la contraction des mots «Information» et «Automatique».
    # - 1971 : microprocesseur 4004 d'Intel,il développe des performanceséquivalents à celle de l'ENIAC (1946),
    #   qui occupait toute une pièce.


    #------------------ - -   Architecture de Von Neuman   - - ---------------------------------------------------------------------------------------------------------------

    # - 1. l'unité arithmétique et logique (UAL) ou unité de traitement, qui effectue les opérations de base.
    # - 2. l'unité de contrôle, qui est chargée du séquençage des opérations.
    # - 3. la mémoire, qui contient à la fois les données et le programme qui indique à l'unité de contrôle quels
    #      calculs faire sur ces données. La mémoire se divise en mémoire vive (programmes et données en cours de
    #      fonctionnement) et mémoire de masse (programmes et données de base de la machine).
    # - 4. les dispositifs d'entrée-sortie, qui permettent de communiquer avec le monde extérieur.

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    return 0

def COURS_Architecture_Materiel_I():

    #I. Les composants de base d’un ordinateur :

    # - 1. Le processeur (ou microprocesseur) :
    #      Il execute les programmes, il est fait de milliards de Transitors et est cadencé par une horloge.  
    #      Frequence : s'exprime en Hertz (Hz) Taille des données : 32 ou 64 bits
    # - 2. La mémoire vive :
    #      Elle est constituée de plusieurs milliards de circuits mémoires,Ces circuits sont regroupés en agrégats de 8, 16, 32, 64
    #      bits (ou davantage) que l’on appelle des cases mémoires.Elles ont des adresses.
    #      RAM = Random Acces Memory car On peut accéder directement à une donnée stockée dans une case mémoire à l’aide de son adresse.
    # - 3. Le bus:
    #      Le processeur, la mémoire et les périphériques sont reliés un canal appelé bus de communication.
    #      le bus de données qui permet l’échanger des données entre le processeur et la mémoire.
    #      le bus d’adresses qui permet d’accéder à une case mémoire. La carte mère joue le rôle de bus.      

    #II. Jeu d’instruction et programmes :

    # - 1. Le processeur d’un ordinateur possède une unité de contrôle et une unité de calcul.
    #      L’unité de contrôle est chargée de lire les programmes enregistrés dans la mémoire et de fournir à l’unité de
    #      calcul la séquence d’instructions à exécuter. Le processeur et la mémoire sont reliés par un bus d’adresses et
    #      un bus de données.
    #      La mémoire peut contenir des milliards de cases mémoire. Elle contient les données et les programmes.
    #      Le processeur possède un très petit nombre de cases mémoires à accès très rapide, appelées registres. Ces
    #      registres peuvent contenir des données ou des adresses.
    # - 2. Un processeur est associé à un jeu d’instructions,une instruction possède un code et un paramètre,
    #      occupe un nombre fixe de cases mémoire, il doit permettre par exemple d’effectuer les tâches suivantes :
    #      - Charger une donnée dans un registre.
    #      - Écrire dans une certaine case mémoire une donnée située dans un registre.
    #      - Faire un calcul (logique ou arithmétique) avec les données contenues dans les registres
    #      - Aller à une instruction située à une certaine adresse (branchement).
    #      - Aller à une instruction située à une certaine adresse si A contient zéro ou passer à l’instruction suivante dans le cas contraire (branchement conditionnel).
    return 0

#Glossaire : 
# - ROM = Read Only Memory
# - RAM = Random Acces Memory
# - BIOS = Basic Input/Ouput System : qui est le premier programme exécuté au démarrage de l’ordinateur.