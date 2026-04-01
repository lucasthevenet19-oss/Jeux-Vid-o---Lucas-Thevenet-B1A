class Entite:
    def __init__(self, nom, attaque, defense, pv):
        self.nom = nom
        self.atk = attaque
        self.defense = defense
        self.pv = pv
        self.pv_max = pv

    def est_en_vie(self):
        return self.pv > 0

    def encaisser_degats(self, points_atk):
        degats = max(0, points_atk - self.defense)
        # Toujours infliger au moins 1 point si l'attaque est positive,
        # pour éviter les combats infinis contre des cibles très défensives.
        if points_atk > 0 and degats == 0:
            degats = 1
        self.pv -= degats
        if self.pv < 0:
            self.pv = 0
        return degats

class Personnage(Entite):
    def __init__(self, data):
        super().__init__(data['nom'], data['atk'], data['def'], data['pv'])

class Monstre(Entite):
    def __init__(self, data):
        super().__init__(data['nom'], data['atk'], data['def'], data['pv'])