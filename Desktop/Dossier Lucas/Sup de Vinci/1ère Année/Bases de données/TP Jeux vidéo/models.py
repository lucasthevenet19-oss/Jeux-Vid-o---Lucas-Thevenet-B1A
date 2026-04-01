class Entite:
    def __init__(self, nom, atk, defense, pv):
        self.nom = nom
        self.atk = atk
        self.defense = defense
        self.pv = pv
        self.pv_max = pv

    def est_en_vie(self):
        return self.pv > 0

    def encaisser_degats(self, points_atk):
        degats = max(0, points_atk - self.defense)
        self.pv -= degats
        return degats

class Personnage(Entite):
    def __init__(self, data):
        super().__init__(data['nom'], data['atk'], data['def'], data['pv'])

class Monstre(Entite):
    def __init__(self, data):
        super().__init__(data['nom'], data['atk'], data['def'], data['pv'])