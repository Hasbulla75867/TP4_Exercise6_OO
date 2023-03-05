"""
Programme fait par Raul Mic Nicolas
TP4 : Introduction à la programmation OO
Copier la classe écrite à l'exercice #4 et ajouter un attribut basé sur la dataclasse écrite à l'exercice #5.

"""

from dataclasses import dataclass
import random


def rouler_de(nombre_des, nombre_cotes):
    """
    Rouler un nombre de dés avec un nombre de côtes et ajouter les valeurs obtenues
    Exemple 2d10 : rouler 2 dés avec 10 côtes et ajouter les valeurs obtenues
    """
    somme_des = 0

    # rouler les dés et ajouter les valeurs obtenues
    for i in range(nombre_des):
        somme_des = somme_des + random.randint(1, nombre_cotes)

    return somme_des


@dataclass
class HeroStats:
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class Hero:
    """
     Classe Hero
        - attributs nombre_points_vie, force_attaque, force_defense, nom
        - méthodes faire_attaque, recois_dommages, est_vivant
    """
    def __init__(self, nom):
        self.nombre_points_vie = rouler_de(2, 10)       # "2d10"
        self.force_attaque = rouler_de(1, 6)            # "1d6"
        self.force_defense = rouler_de(1, 6)            # "1d6"
        self.nom = nom
        # Stats héro
        self.stats = HeroStats()

    def faire_attaque(self):
        self.nombre_points_vie = rouler_de(1, 6) + self.force_attaque
        return self.nombre_points_vie

    def recois_dommages(self, nombre_dommages):
        self.nombre_points_vie -= nombre_dommages - self.force_defense
        return self.nombre_points_vie

    def est_vivant(self):
        if self.nombre_points_vie > 0:
            return True
        else:
            return False


hero = Hero("Captain America")
print("*****************************************")
print(f"La force de {hero.nom} est de {hero.stats.force} points")
print(f"La dextérité de {hero.nom} est de {hero.stats.dexterite} points")
print(f"La constitution de {hero.nom} est de {hero.stats.constitution} points")
print(f"L'intelligence de {hero.nom} est de {hero.stats.intelligence} points")
print(f"La sagesse de {hero.nom} est de {hero.stats.sagesse} points")
print(f"Le charisme de {hero.nom} est de {hero.stats.charisme} points")
print("*****************************************")
print(f"Nombre points de vie : {hero.nombre_points_vie}")
print(f"Sa force d'attaque   : {hero.force_attaque}")
print(f"Sa force de défense  : {hero.force_defense}")
print("*****************************************")
# héro attaque
points_vie_hero = hero.faire_attaque()
print(f"Après l'attaque, l'héro {hero.nom} a {points_vie_hero} points de vie")
# héro recoit dommages
points_dommage = int(input("Entrez le nombre de points de dommage : "))
points_vie_hero = hero.recois_dommages(points_dommage)  # héro recois points_dommage points de dommage
print(f"Après {points_dommage} points de dommages, héro {hero.nom} a {points_vie_hero} points de vie")
if hero.est_vivant():
    print(f"L'héro {hero.nom} est vivant. Il a {hero.nombre_points_vie} nombre points de vie")
else:
    print(f"L'héro {hero.nom} est mort")
