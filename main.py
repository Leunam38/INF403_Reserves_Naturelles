# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

from utils import db
import sqlite3
from requetes_predefinis import * 
from requetes_exemples import * 
from affichage_req import * 

def menu():
    rep=0
    while rep < 1 or rep > 9:
        print("\n\033[1;35mMenu")
        print("\033[1;34m1. Requete a la main")
        print("2. Exemple de requête")
        print("3. Requête prédéfini")
        print("4. inserer des donnees")
        print("7. Quitter\033[1;37m")
        rep = int(input())
    return rep

    
    


def requete_main(conn):
    cur = conn.cursor()
    requete = str(input("donnez votre requete:"))
    cur.execute(requete)
    rows = cur.fetchall()
    affichage_requete(rows)
    
def reset_donnes(conn): 
    c=""
    while (c != "oui" and c != "non" and c != "o" and c != "n"):
        print("voulez-vous reinitialiser la base de donnée (oui/non) ?")
        c = str(input())
    if (c == 'oui' or c=="o"):
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
    selection=menu()
    while selection != 7:
        match selection:
            case 1:
                requete_main(conn)
            case 2:
                requete_exemple(conn)
            case 3:
                requete_predef(conn)
            case 4:
                inserer_des_donnees(conn)

        selection=menu()

if __name__ == "__main__":
    main()
