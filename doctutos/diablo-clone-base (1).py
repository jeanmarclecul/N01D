import random

class Personnage:
    def __init__(self, nom, classe, pv, force):
        self.nom = nom
        self.classe = classe
        self.pv = pv
        self.force = force
        self.niveau = 1
        self.experience = 0

    def attaquer(self, cible):
        degats = random.randint(1, self.force)
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts!")

    def gagner_experience(self, montant):
        self.experience += montant
        if self.experience >= 100:
            self.niveau += 1
            self.experience -= 100
            print(f"{self.nom} passe au niveau {self.niveau}!")

class Monstre:
    def __init__(self, nom, pv, force):
        self.nom = nom
        self.pv = pv
        self.force = force

    def attaquer(self, cible):
        degats = random.randint(1, self.force)
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} points de dégâts!")

def combat(joueur, monstre):
    print(f"Un combat commence entre {joueur.nom} et {monstre.nom}!")
    while joueur.pv > 0 and monstre.pv > 0:
        joueur.attaquer(monstre)
        if monstre.pv <= 0:
            print(f"{monstre.nom} a été vaincu!")
            joueur.gagner_experience(50)
            break
        monstre.attaquer(joueur)
        if joueur.pv <= 0:
            print(f"{joueur.nom} a été vaincu!")
            break

# Exemple d'utilisation
joueur = Personnage("Héros", "Barbare", 100, 15)
monstre = Monstre("Gobelin", 50, 10)

combat(joueur, monstre)
