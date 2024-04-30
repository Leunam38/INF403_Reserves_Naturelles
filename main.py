# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

from utils import db
import sqlite3
from requetes_predefinis import * 
from requetes_exemples import * 
from affichage_req import * 

def menu():
    """
    Permet l'affichage du menu et guide l'utilisateur en fonction de ses choix
    
    :param conn: Connexion à la base de données
    """
    rep=0
    while rep < 1 or rep > 10:
        print("\n\033[1;35mMenu")
        print("\033[1;34m1. Informations base de donnee")
        print("2. Requete a la main")
        print("3. Exemple de requête")
        print("4. Requête prédéfini")
        print("5. Inserer des donnees")
        print("6. Mettre a jour des donnees")
        print("7. Supprimer une/plusieurs valeurs")
        print("8. Créer une table")
        print("9. Supprimer une table")
        print("10. Quitter\033[1;37m")
        rep = int(input("Choix : "))
        print("")
    return rep


def requete_main(conn):
    """
    Permet d'ecrire une requete a la main
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    requete = str(input("Donnez votre requete:")) #ecriture de la requete
    cur.execute(requete) #execution de la requete
    rows = cur.fetchall() #mise en place du resultat dans une liste
    affichage_requete(rows) #affichage de la requete
    
def suppression_tables(conn):
    """
    Supprime toutes les tables
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    tables = affiche_nom_table(conn,0)
    if tables != None:            
        for table_nom in tables:
            cur.execute(f"DROP TABLE '{table_nom}';")
            print(f"La table {table_nom} a été supprimée.")
    
    
def reset_donnes(conn):
    """
    Demande a l'utilisateur si il veut reinitialiser la base de donnees ou non
    
    :param conn: Connexion à la base de données
    """
    c=""
    while (c != "oui" and c != "non" and c != "o" and c != "n"):
        print("\033[1;35mVoulez-vous reinitialiser la base de donnée (oui/non) ?\033[1;37m")
        c = str(input())
    if (c == 'oui' or c=="o"): #reset la bdd a partir d'ici
        print("On initialise la base de donnée avec des premières valeurs.")
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_drop_all.sql")
        suppression_tables(conn)
        
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_creation.sql")
        db.mise_a_jour_bd(conn, "data/reserves_naturelles_insert.sql") 


def main():
    # Nom de la BD à créer
    print("\033[2J\033[H", end="")
    db_file = "data/reserves_naturelles.db"
    
    # print("\033[46m")
    
    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    conn.set_trace_callback(print)

    # Réinitialisation possible des bases de données
    reset_donnes(conn)

    # Lancement du menu
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
