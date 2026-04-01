import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jeu_video_db"]

def charger_personnages():
    return list(db.personnages.find())

def charger_monstres():
    return list(db.monstres.find())

def enregistrer_resultat(pseudo, score):
    db.scores.insert_one({"pseudo": pseudo, "vagues": score})

def obtenir_classement():
    return list(db.scores.find().sort("vagues", -1).limit(3))

def afficher_barre_vie(entite):
    return f"[{entite.pv}/{entite.pv_max} PV]"