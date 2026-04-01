from models import Personnage
from utils import charger_personnages, obtenir_classement, enregistrer_resultat
from game import gestion_combat

def choisir_equipe():
    dispo = charger_personnages()
    equipe = []
    print("\n--- SELECTIONNEZ 3 HEROS ---")
    while len(equipe) < 3:
        for i, p in enumerate(dispo):
            print(f"[{i+1}] {p['nom']} (ATK:{p['atk']} DEF:{p['def']} PV:{p['pv']})")
        
        try:
            choix = int(input(f"Numero du heros {len(equipe)+1} : "))
            index = choix - 1
            if 0 <= index < len(dispo):
                equipe.append(Personnage(dispo.pop(index)))
                print("Ajoute !")
            else:
                print("Numero invalide.")
        except ValueError:
            print("Entrez un chiffre.")
    return equipe

def main():
    while True:
        print("\n1. Nouvelle Partie | 2. Scores | 3. Quitter")
        action = input("Votre choix : ")

        if action == "1":
            pseudo = input("Votre Pseudo : ") or "Joueur"
            equipe = choisir_equipe()
            score = gestion_combat(equipe)
            enregistrer_resultat(pseudo, score)
            print(f"\nScore Final : {score} vagues !")
        elif action == "2":
            for s in obtenir_classement():
                print(f"{s['pseudo']} : {s['vagues']} vagues")
        elif action == "3":
            break

if __name__ == "__main__":
    main() 