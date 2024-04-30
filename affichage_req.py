#!/usr/bin/python3

def affichage_requete(rep):
    """
    Rend propre l'affichage de requetes
    
    :param rep: Liste du résultat renvoyer par une requete
    """
    if (len(rep)==0): #Si il n'y a pas donnee renvoyer
        print("Aucune donnee selectionnee")
        return 
    
    taille_argu=len(rep[0])
    taille_rep=len(rep)
    #Parcours de la liste
    for i in range (taille_rep):
        print(rep[i][0], end = '')
        for j in range (1,taille_argu):
            print(f", {rep[i][j]}", end = '')
        print("")


def demander_info():
    """
    Demande a l'utilisateur ce qu'il veut comme informations sur la bdd (identique au menu)
    """
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


def affiche_nom_table(conn,debug=0):
    """
    Affiche le nom de toute les tables
    
    :param conn: Connexion à la base de données
    :param debug=0: Option de débug pour afficher la table ou la renvoyer
    """
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    # Affichage des noms des tables
    if debug == 1: #permet l'affichage
        affichage_requete(tables)
    else: #permet d'avoir la liste des noms des tables
        lst=[]
        for table in tables:
            lst.append(table[0])
        return lst

def choix_table(conn):
    cur = conn.cursor()
    verif=[]
    verif = affiche_nom_table(conn,0) #permet de recuperer la liste des tables existantes
    print("\033[1;35mChoisissez parmi les tables suivantes:\033[1;31m")
    for tab in verif:
        print(f"{tab}", end=' ')
        
    table = str(input("\n\033[1;37mDonnez le nom de la Table que vous voulez séléctionnner : ")) #on recupere le nom d'une table
    if table not in verif: #permet la verification de l'existence d'une table avant d'inserer des donnees
        print("La table n'existe pas encore, veuillez la creer avant ")
        return 
    return table

def affiche_une_table(conn):
    """affiche une table"""
    cur = conn.cursor()
    
    table=choix_table(conn)
    if table==None:
        return
    lst = affiche_attributs_table(conn,table)
    affichage_requete([lst])
    print("")
    
    cur.execute("""
                SELECT *
                FROM
                """+table)

    rows = cur.fetchall()
    affichage_requete(rows)

def affiche_attributs_table(conn,table,debug=0):
    """affiche le nom des attributs d'une table"""
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    lst=[]
    # Récupérez toutes les lignes résultantes
    rows = cur.fetchall()
    # Affichez les noms des colonnes
    for row in rows:
       lst.append(row[1]) # row[1] contient le nom de la colonne
       if debug==1:
           print(f"{row[1]}", end=' ') #affiche le nom de attributs de la table, afin de guider l'utilisateur dans l'insertion de donnees
    if debug==1:
        print("")
    return lst