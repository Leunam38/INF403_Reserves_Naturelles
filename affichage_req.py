#!/usr/bin/python3

def affichage_requete(rep):
    """rend propre l'affichage de requetes"""
    if (len(rep)==0):
        print("Aucune donnee selectionnee")
        return 
    
    taille_argu=len(rep[0])
    taille_rep=len(rep)
    for i in range (taille_rep):
        print(rep[i][0], end = ' ')
        for j in range (1,taille_argu):
            print(f",{rep[i][j]}", end = ' ')
        print("")

def demander_info():
    """demande a l'utilisateur ce qu'il veut comme informations sur la bdd (identique au menu)"""
    choix=0
    while choix < 1 or choix > 4:
        print("\n\033[1;35mInformations")
        print("\033[1;34m1. Tables disponibles")
        print("2. Noms des attributs d'une table")
        print("3. Donnees d'une table")
        print("4. Retour au menu\033[1;37m")
        choix = int(input("Choix : "))
    return choix

def informations(conn):
    """permet de guider l'utilisateur dans les informations qu'il cherche (comme dans le main)"""
    info = demander_info()
    match info:
        case 1:
            affiche_nom_table(conn,0)
        case 2:
            table = str(input("Donnez le nom d'une table valide : "))
            lst = affiche_attributs_table(conn,table)
            print(lst)
        case 3:
            affiche_une_table(conn)
    return


def affiche_nom_table(conn,setting):
    """affiche le nom de toute les tables"""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Affichage des noms des tables
    if setting == 0: #permet l'affichage
        for table in tables:
            print(table[0])
    else: #permet d'avoir la liste des noms des tables
        lst=[]
        for table in tables:
            lst.append(table[0])
            return lst

def affiche_une_table(conn):
    """affiche une table"""
    cur = conn.cursor()
    table = str(input("Donnez le nom de la table a afficher: "))
    cur.execute("""
                SELECT *
                FROM
                """+table)

    rows = cur.fetchall()
    affichage_requete(rows)

def affiche_attributs_table(conn,table):
    """affiche le nom des attributs d'une table"""
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    lst=[]
    # Récupérez toutes les lignes résultantes
    rows = cur.fetchall()
    # Affichez les noms des colonnes
    for row in rows:
       lst.append(row[1]) # row[1] contient le nom de la colonne
    #print(lst)
    return lst