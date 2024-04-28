# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

from utils import db
import sqlite3
from requetes_predefinis import * 
from requetes_exemples import * 
from affichage_req import * 

def menu():
    """Permet l'affichage du menu et guide l'utilisateur en fonction de ses choix"""
    rep=0
    while rep < 1 or rep > 10:
        print("\n\033[1;35mMenu")
        print("\033[1;34m1. Informations base de donnee")
        print("2. Requete a la main")
        print("3. Exemple de requête")
        print("4. Requête prédéfini")
        print("5. inserer des donnees")
        print("6. mettre a jour des donnees")
        print("7. supprimer une/plusieurs valeurs")
        print("8. creer une table")
        print("9. supprimer une table")
        print("10. Quitter\033[1;37m")
        rep = int(input("Choix : "))
    return rep

    
    


def requete_main(conn):
    """Permet d'ecrire une requete a la main"""
    cur = conn.cursor()
    requete = str(input("donnez votre requete:")) #ecriture de la requete
    cur.execute(requete) #execution de la requete
    rows = cur.fetchall() #mise en place du resultat dans une liste
    affichage_requete(rows) #affichage de la requete
    
def reset_donnes(conn):
    """demande a l'utilisateur si il veut reinitialiser la base de donnees ou non"""
    c=""
    while (c != "oui" and c != "non" and c != "o" and c != "n"):
        print("voulez-vous reinitialiser la base de donnée (oui/non) ?")
        c = str(input())
    if (c == 'oui' or c=="o"): #reset la bdd a partir d'ici
        print("On initialise la base de donnée avec des premières valeurs.")
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_drop_all.sql")
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_creation.sql")
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_insert.sql") 











def main():
    # Nom de la BD à créer
    db_file = "data/reserves_naturelles.db"
    print("\033[1;43m")
    
    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    reset_donnes(conn)

    # Lire la BD    
    selection=menu() #choix de l'utilisateur pour naviguer dans le menu
    while selection != 10: #pour quitter
        match selection: #permet d'appeler les bonnes fonctions en fonction du choix de l'utilisateur
            case 1:
                informations(conn)
            case 2:
                requete_main(conn)
            case 3:
                requete_exemple(conn)
            case 4:
                requete_predef(conn)
            case 5:
                inserer_des_donnees(conn)
            case 6:
                mettre_a_jour_des_donnees(conn)
            case 7:
                supprimer_valeur(conn)
            case 8:
                creer_table(conn)
            case 9:
                supprimer_table(conn)

        selection=menu()

if __name__ == "__main__":
    main()
