# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3

from utils import db
import sqlite3
from affichage_req import * 
from requetes_exemples import * 
from requetes_predefinis import * 
from requetes_modification_db import * 

def informations(conn):
    """
    Permet de guider l'utilisateur dans les informations qu'il cherche (comme dans le main)
    
    :param conn: Connexion à la base de données
    """
    info = demander_info()
    match info:
        case 1:
            affiche_nom_table(conn,1)
        case 2:
            table=choix_table(conn)
            if table==None:
                return
            lst = affiche_attributs_table(conn,table)
            affichage_requete([lst])
        case 3:
            affiche_une_table(conn)
    return

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
    


def main():
    # Nom de la BD à créer
    print("\033[2J\033[H", end="")
    db_file = "data/reserves_naturelles.db"
    
    # print("\033[46m")
    
    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    # conn.set_trace_callback(print) #Affichage des commandes pour débug

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
