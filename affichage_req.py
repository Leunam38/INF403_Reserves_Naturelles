#!/usr/bin/python3

def affichage_requete(rep):
    """
    Rend propre l'affichage de requetes
    
    :param rep: Liste du résultat renvoyer par une requete
    """
    if (len(rep)==0): #Si il n'y a pas donnee renvoyer
        print("Aucune donnee selectionnée")
        return 
    
    taille_argu=len(rep[0])
    taille_rep=len(rep)
    #Parcours de la liste
    for i in range (taille_rep):
        print(rep[i][0], end = '')
        for j in range (1,taille_argu):
            print(f", {rep[i][j]}", end = '')
        print("")

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




def affiche_nom_table(conn,debug=0):
    """
    Affiche le nom de toute les tables
    
    :param conn: Connexion à la base de données
    :param debug=0: Option de débug pour afficher la table (1) ou la renvoyer (0)
    """
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' OR  type='view';")
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
    """
    Propose un choix parmi les tables et vérifie sa véridicité
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    verif=[] 
    verif = affiche_nom_table(conn,0) #tableau permettant de recuperer la liste des tables existantes
    print("\033[1;35mChoisissez parmi les tables suivantes:\033[1;31m")
    for tab in verif:
        print(f"{tab}", end=' ')
        
    table = str(input("\n\033[1;35mDonnez le nom de la Table que vous voulez séléctionnner : \033[1;37m")) #on recupere le nom d'une table
    if table not in verif: #permet la verification de l'existence d'une table 
        print("La table n'existe pas encore, veuillez la creer avant ")
        return 
    return table

def affiche_une_table(conn):
    """
    Affiche une table
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    
    table=choix_table(conn)
    if table==None:
        return
    lst = affiche_attributs_table(conn,table,1)
    print("")
    
    cur.execute("""
                SELECT *
                FROM """+table)

    rows = cur.fetchall()
    
    affichage_requete(rows)
    

def affiche_attributs_table(conn,table,debug=0):
    """
    Affiche la liste des noms des attributs d'une table
    
    :param conn: Connexion à la base de données
    :param table: nom de la table
    :param debug=0: Option de débug pour afficher les attributs (1) ou rien d'afficher (0)
    """
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    lst=[]
    # Récupérez toutes les lignes résultantes
    rows = cur.fetchall()
    # Affichez les noms des colonnes
    for row in rows:
       lst.append(row[1]) # row[1] contient le nom de la colonne
       if debug==1:
           print(f"\033[1;92m{row[1]}", end=' ') #affiche le nom de attributs de la table, afin de guider l'utilisateur dans l'insertion de donnees
    if debug==1:
        print("\033[1;37m")
    return lst