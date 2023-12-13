import random

# ---------------------------------------------------------------------------------------|

class Mage:
    def __init__(self, name):
        self.__nom = name
        self.__pv = 20
        self.__manaMax = 20
        self.__manaActuel = 20
        self.__main = ["-"]*10
        self.__deffausse = ["-"]*50
        self.__zone = ["-"]*5

    def getPV(self):
        return self.__pv
    def getManaActuel(self):
        return self.__manaActuel
    def getManaMax(self):
        return self.__manaMax
    def getZone(self):
        print(self.__zone)

    def jouerCarte(self, slot, carte):
        self.__zone[slot] = carte
        print(self.__zone)
    def manaAugment(self, valeur):
        self.__manaMax += valeur
        print(f"{self.__nom} gagne {valeur} de mana max.")
    def manaCost(self, valeur):
        self.__manaActuel -= valeur
        print(f"{self.__nom} utilise {valeur} de mana.")
    def perdPv(self, valeur):
        self.__pv -= valeur
        print(f"{self.__nom} perd {valeur} points de vie.")

# ---------------------------------------------------------------------------------------|

class Carte:
    def __init__(self, name, mana, descritpion):
        self.__nom = name
        self.__cost = mana
        self.__description = descritpion

    def getCost(self):
        return self.__cost
    
    def info(self):
        print(f"{self.__nom} - {self.__cost} mana. {self.__description}.")


class Cristal(Carte):
    def __init__(self, name, mana, descritpion):
        Carte.__init__(self, name, mana, descritpion)
        self.__valeur = 4

    def utilisation(self):
        return self.__valeur

class Blast(Carte):
    def __init__(self, name, mana, descritpion):
        Carte.__init__(self, name, mana, descritpion)
        self.__valeur = 4

    def utilisation(self):
        return self.__valeur

class Creature(Carte):
    def __init__(self, name, mana, descritpion):
        Carte.__init__(self, name, mana, descritpion)
        self.__atk = 5
        self.__pv = 10

    def attaque(self):
        return self.__atk

    def utilisation(self):
        return self.__valeur







# ---------------------------------------------------------------------------------------|

Mage1 = Mage("Jhon")
Blast1 = Blast("Blast!", 2, "Emet un choc magique sur l'adversaire")
Cristal1 = Cristal("Cristal.", 2, "Invoque un cristal qui genere du mana")

# ---------------------------------------------------------------------------------------|

print(Mage1.getPV(),"pv.")
Blast1.info()
Mage1.perdPv(Blast1.utilisation())
print(Mage1.getPV(),"pv.")


print(Mage1.getManaActuel(),"mana")
print(Mage1.getManaMax(),"mana max.")

print(Mage1.getZone())
print(Cristal1.info())
Mage1.manaCost(Cristal1.getCost())
slotChoice = int(input("Choisi l'emplacement.\n")) -1
Mage1.jouerCarte(slotChoice, "Cristal")
Mage1.manaAugment(Cristal1.utilisation())

print(Mage1.getManaActuel(),"mana")
print(Mage1.getManaMax(),"mana max.")
