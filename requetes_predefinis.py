#!/usr/bin/python3
from affichage_req import * 

def requete_predef(conn):
    """Menu secondaire pour que l'utilisateur ait du choix parmi les requetes prédéfinis, cette fonction agit comme main et menu

    :param conn: Connexion à la base de données
    """
    rep=0
    while rep < 1 or rep > 9:
        print("\033[1;35mChoisissez votre requete prédéfinis:")
        print("\033[1;36m1. Afficher toute une table")
        print("2. Afficher tous les parcours d'une reserve")
        print("3. Afficher les animaux d'une reserve")
        print("4. Afficher les plantes dans une reserve")
        print("5. Chercher un garde forestier")
        print("6. Chercher un animal avec ses caracteristiques et son lieu d'habitat")
        print("7. Chercher une plante avec ses caracteristiques et son lieu d'habitat")
        print("8. Afficher les réserves avec plus d'un certain nombre d'animaux protegés")
        print("9. Retour\n")
        rep = int(input("\033[1;37mchoix: "))
    match rep: #pour appeler les bonnes fonctions
        case 1:
            affiche_une_table(conn)
        case 2:
            parcours_dune_reserve(conn) #A tester
        case 3:
            animaux_de_la_reserve(conn)
        case 4:
            fleurs_de_la_reserve(conn)
        case 5:
            cherche_garde(conn)
        case 6:
            chercher_animal(conn) 
        case 7:
            chercher_fleur(conn)
        case 8:
            reserve_nb_min_animaux_prot(conn)
            

def animaux_de_la_reserve(conn):
    """Affiche la liste des animaux d'une reserve

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    reserve = str(input("\033[1;35mDonnez le nom de la reserve : \033[1;37m"))
    cur.execute("""
                SELECT nom_faune
                FROM Habite 
                WHERE nom_reserve = ?
                """,[reserve])
    rows = cur.fetchall()
    affichage_requete(rows)
        
def parcours_dune_reserve(conn):
    """Affiche la liste des parcours disponible dans une reserve

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    reserve = str(input("\033[1;35mDonnez le nom de la reserve : \033[1;37m"))
    cur.execute("""
                SELECT nom_parcours
                FROM Traverse
                WHERE nom_reserve = ?
                """,[reserve])
    rows = cur.fetchall()
    affichage_requete(rows)
        
def animaux_de_la_reserve(conn):
    """Affiche la liste des animaux d'une reserve

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    reserve = str(input("\033[1;35mDonnez le nom de la reserve : \033[1;37m"))
    cur.execute("""
                SELECT nom_faune
                FROM Habite 
                WHERE nom_reserve = ?
                """,[reserve])
    rows = cur.fetchall()
    affichage_requete(rows)
        
def fleurs_de_la_reserve(conn):
    """Affiche la liste des fleurs d'une reserve

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    reserve = str(input("\033[1;35mDonnez le nom de la reserve : \033[1;37m"))
    cur.execute("""
                SELECT nom_flore
                FROM PousseDans 
                WHERE nom_reserve = ?
                """,[reserve])
    rows = cur.fetchall()
    affichage_requete(rows)
        
def cherche_garde(conn):
    """Affiche la carte d'identité d'un garde

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    garde_nom = str(input("\033[1;35mDonnez le nom du garde : \033[1;37m"))
    garde_prenom = str(input("\033[1;35mDonnez le prenom du garde : \033[1;37m"))
    cur.execute("""
                SELECT *
                FROM GardesForestier
                WHERE nom_garde_forestier = ? AND prenom_garde_forestier = ?
                """,[garde_nom,garde_prenom])
    rows = cur.fetchall()
    affiche_attributs_table(conn,"GardesForestier",1)
    affichage_requete(rows)
        
def chercher_animal(conn):
    """Trouver la fiche d'identité d'un animal dans la base de donnée ainsi que les réserves où il est présent

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    animal = str(input("\033[1;35mDonnez le nom de l'animal : \033[1;37m"))
    cur.execute("""
                SELECT *
                FROM Faune 
                WHERE nom_faune = ?
                """,[animal])
    rows = cur.fetchall()
    affiche_attributs_table(conn,"Faune",1)
    affichage_requete(rows)
    
    print("\n\033[1;34mHabite dans les réserves:\033[1;37m")
    cur.execute("""
                SELECT nom_reserve
                FROM Habite 
                WHERE nom_faune = ?
                """,[animal])
    rows = cur.fetchall()
    affichage_requete(rows)
        
def chercher_fleur(conn):
    """Trouver la fiche d'identité d'une plante dans la base de donnée ainsi que les réserves où il est présent

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    plante = str(input("\033[1;35mDonnez le nom de la plante : \033[1;37m"))
    cur.execute("""
                SELECT *
                FROM Flore 
                WHERE nom_flore = ?
                """,[plante])
    rows = cur.fetchall()
    affiche_attributs_table(conn,"Flore",1)
    affichage_requete(rows)
    
    print("\n\033[1;34mPousse dans les réserves:\033[1;37m")
    cur.execute("""
                SELECT nom_reserve
                FROM PousseDans 
                WHERE nom_flore = ?
                """,[plante])
    rows = cur.fetchall()
    affichage_requete(rows)
        
        
def reserve_nb_min_animaux_prot(conn):
    """Affiche les réserves avec plus de n animaux

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    reserve = int(input("\033[1;35mDonnez le nombre d'animaux protegé minimal : \033[1;37m"))
    cur.execute("""
                SELECT nom_reserve
                FROM Reserves 
                WHERE nb_animaux_proteges_reserve >= ?
                """,[reserve])
    rows = cur.fetchall()
    affichage_requete(rows)
               
        
  