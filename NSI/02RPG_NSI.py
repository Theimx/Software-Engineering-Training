import random 
import os 
import time

#   Ressource : 
#   ❤️ 🖤 ⚔️  🗡️ 🛡️ 

# Créer un disctionnaire pour chaque joueur 
def generatePlayers():

    _rID = '1'
    for i in range(7): 
        _rID += str(random.randint(0,9))
    int(_rID)

    Stats = {'id': _rID, 'pv': 200, 'atk': 40, 'def': 25, 'cc': 5, 'dc': 120, 'spd': 10 }

    return Stats

#lis le dico et affiches les infos dans l'ordre 
def showStats(_stats):

    for cle in _stats.keys( ) :
        print ( cle, end= ' ' )
    print(" ")
    for cle in _stats.values( ) :
        print ( cle, end= ' ' )
    print(" ")

def setStatsPoints(_stats):
    _nbPoint = 6 
    while _nbPoint > 0 : 
        
        modStats = input("Entrez le nom de la stats a modifier (atk def cc dc spd ) :")
        
        if modStats == "atk" :
            _stats["atk"] += 1
            _nbPoint -= 1
            os.system("cls")
            print("1 point d'attaque ajouté ")
            print("il vous reste :" , _nbPoint)
            time.sleep(1)
            showStats(_stats)

        if modStats == "def" :
            _stats["def"] += 1
            _nbPoint -= 1
            os.system("cls")
            print("1 point de défense ajouté ")
            print("il vous reste :" , _nbPoint)
            time.sleep(1)
            showStats(_stats)

        if modStats == "spd" :
            _stats["spd"] += 1
            _nbPoint -= 1
            os.system("cls")
            print("1 point de vitesse ajouté ")
            print("il vous reste :" , _nbPoint)
            time.sleep(1)
            showStats(_stats)

        if modStats == "cc" :
            _stats["cc"] =  _stats["cc"] * 1 +(5/100)
            _nbPoint -= 1
            os.system("cls")
            print("5% point de coup critique ajouté ")
            print("il vous reste :" , _nbPoint)
            time.sleep(1)
            showStats(_stats)

        if modStats == "dc" :
            _stats["dc"] =  _stats["dc"] * 1 +(15/100)
            _nbPoint -= 1
            os.system("cls")
            print("15% point de dégats critique ajouté ")
            print("il vous reste :" , _nbPoint)
            time.sleep(1)
            showStats(_stats)

def Combat(J1,J2):

    while J1["pv"] > 0 or J2["pv"] > 0: 
        if (J1["spd"] > J2["spd"]) and (J1["spd"] != J2["spd"]):
            J2["pv"] -= (J1["atk"]* 1.08) - J2["def"]
            print(J2["def"])
    
joueur1 = generatePlayers()
joueur2 = generatePlayers()

print("J1 : Vos statistiques :" )
showStats(joueur1)
setStatsPoints(joueur1)
print("J1 : Vos statistiques Final:" )

print("J2 : Vos statistiques :" )
showStats(joueur2)
setStatsPoints(joueur2)
print("J2 : Vos statistiques Final:" )

Combat()