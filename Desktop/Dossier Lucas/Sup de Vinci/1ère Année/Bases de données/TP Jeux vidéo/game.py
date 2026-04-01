import random
import time
from models import Monstre
from utils import charger_monstres, afficher_barre_vie

def gestion_combat(equipe):
    tous_les_monstres = charger_monstres()
    nb_monstres = len(tous_les_monstres)
    vagues_reussies = 0

    while any(p.est_en_vie() for p in equipe):
        index = vagues_reussies % nb_monstres
        m = Monstre(tous_les_monstres[index])
        
        print(f"\n>>> MONDE {vagues_reussies + 1} : Territoire du {m.nom} <<<")
        time.sleep(1)

        tour_perso = 0
        while m.est_en_vie() and any(p.est_en_vie() for p in equipe):
            print("\n--- Tour de l'equipe ---")
            
            # Liste des personnages encore en vie avec leur PV 
            vivants = []
            for p in equipe:
                if p.est_en_vie():
                    vivants.append(p)
            
            # Le personnage chosit attaque le monstre
            if len(vivants) > 0 and m.est_en_vie():
                index_perso = tour_perso % len(vivants)
                attaquant = vivants[index_perso]
                d = m.encaisser_degats(attaquant.atk)
                print(f"{attaquant.nom} frappe {m.nom} (-{d} PV)")
                tour_perso += 1

            # Le monstre riposte sur un personnage au hasard
            if m.est_en_vie():
                vivants_pour_riposte = []
                for p in equipe:
                    if p.est_en_vie():
                        vivants_pour_riposte.append(p)
                index_cible = random.randint(0, len(vivants_pour_riposte) - 1)
                cible = vivants_pour_riposte[index_cible]
                d_m = cible.encaisser_degats(m.atk)
                print(f"\nLe {m.nom} riposte sur {cible.nom} (-{d_m} PV)")
            
            # Affichage de l'état de l'équipe
            print("\nEtat de l'equipe :")
            for p in equipe:
                if p.est_en_vie():
                    status = afficher_barre_vie(p)
                else:
                    status = "K.O."
                print(f"  {p.nom} : {status}")
            time.sleep(1.2)

        if not m.est_en_vie():
            print(f"\nVictoire ! Le {m.nom} est vaincu.")
            vagues_reussies += 1
            time.sleep(1)
        else:
            print("\nDefaite... Fin de l'aventure.")
            break
            
    return vagues_reussies