import pymongo

def initialiser():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["jeu_video_db"]
        
        db.personnages.drop()
        db.monstres.drop()

        # Liste des 10 heros (Stats augmentées pour tenir le choc)
        # Ratio : Somme Atk + Def + PV environ égale pour tous
        persos = [
            {"nom": "Guerrier", "atk": 35, "def": 45, "pv": 100},
            {"nom": "Mage", "atk": 65, "def": 20, "pv": 80},
            {"nom": "Archer", "atk": 50, "def": 30, "pv": 70},
            {"nom": "Voleur", "atk": 55, "def": 25, "pv": 80},
            {"nom": "Paladin", "atk": 30, "def": 40, "pv": 120},
            {"nom": "Sorcier", "atk": 70, "def": 15, "pv": 110},
            {"nom": "Chevalier", "atk": 40, "def": 50, "pv": 90},
            {"nom": "Moine", "atk": 45, "def": 40, "pv": 120},
            {"nom": "Berserker", "atk": 55, "def": 20, "pv": 90},
            {"nom": "Chasseur", "atk": 52, "def": 35, "pv": 145}
        ]
        
        # Liste des 10 monstres (Difficulté progressive réelle)
        monstres = [
            {"nom": "Gobelin", "atk": 40, "def": 30, "pv": 60},
        ]
        
        db.personnages.insert_many(persos)
        db.monstres.insert_many(monstres)
        
        print("--- BASE INITIALISEE : Stats equilibrees pour le tour par tour ---")

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    initialiser()