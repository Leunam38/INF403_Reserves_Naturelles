#!/usr/bin/python3
from affichage_req import * 


def requete_exemple(conn):
    rep=0
    while rep < 1 or rep > 8:
        print("\033[1;35mChoisissez une des requetes:")
        print("\033[1;36m1. affiche toutes les réserves")
        print("2. affiche tous les animaux proteges tous les parcours d'une reserve")
        # print("3. afficher les animaux d'une reserve")
        # print("4. afficher les plantes dans une reserve")
        # print("5. chercher un garde forestier")
        # print("6. chercher un animal avec ses caracteristiques et son lieu d'habitat")
        # print("7. chercher une plante avec ses caracteristiques et son lieu d'habitat")
        print("8. Retour\n")
        rep = int(input("\033[1;37mchoix: "))
    match rep:
        case 1:
            select_tous_les_reserves(conn)
        case 2:
            select_animaux_proteges(conn) #A tester
        # case 3:
        #     animaux_de_la_reserve(conn)
        # case 4:
        #     fleurs_de_la_reserve(conn)
        # case 5:
        #     cherche_garde(conn)
        # case 6:
        #     chercher_animal(conn) #affichage a revoir
        # case 7:
        #     chercher_fleur(conn) #affichage a revoir

def select_tous_les_reserves(conn):
    """
    Affiche la liste de toutes les reserves.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Parcours
                """)

    rows = cur.fetchall()
    affichage_requete(rows)


def select_animaux_proteges(conn):
    """
    Affiche la liste de tous les animaux proteges.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_faune
                FROM Faune
                WHERE est_protege_faune='oui'
                """)

    rows = cur.fetchall()
    affichage_requete(rows)
        