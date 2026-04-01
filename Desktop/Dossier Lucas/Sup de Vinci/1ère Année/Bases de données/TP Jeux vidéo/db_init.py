import pymongo

def initialiser():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["jeu_video_db"]
        
        db.personnages.drop()
        db.monstres.drop()

        # Liste des 10 heros 
        persos = [
            {"nom": "Guerrier", "attaque": 35, "defense": 45, "PV": 100},
            {"nom": "Mage", "attaque": 65, "defense": 20, "PV": 80},
            {"nom": "Archer", "attaque": 50, "defense": 30, "PV": 70},
            {"nom": "Voleur", "attaque": 55, "defense": 25, "PV": 80},
            {"nom": "Paladin", "attaque": 30, "defense": 40, "PV": 120},
            {"nom": "Sorcier", "attaque": 70, "defense": 15, "PV": 110},
            {"nom": "Chevalier", "attaque": 40, "defense": 50, "PV": 90},
            {"nom": "Moine", "attaque": 45, "defense": 40, "PV": 120},
            {"nom": "Berserker", "attaque": 55, "defense": 20, "PV": 90},
            {"nom": "Chasseur", "attaque": 52, "defense": 35, "PV": 145}
        ]
        
        # Liste des 1 monstres
        monstres = [
            {"nom": "Gobelin", "attaque": 40, "defense": 30, "PV": 60},
        ]
        
        db.personnages.insert_many(persos)
        db.monstres.insert_many(monstres)
        
        print("--- BASE INITIALISEE : Stats equilibrees pour le tour par tour ---")

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    initialiser()
    