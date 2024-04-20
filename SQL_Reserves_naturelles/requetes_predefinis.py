#!/usr/bin/python3
from affichage_req import * 

def requete_predef(conn):
    rep=0
    while rep < 1 or rep > 8:
        print("\033[1;35mChoisissez votre mode de requete:")
        print("\033[1;36m1. afficher toute une table")
        print("2. afficher tous les parcours d'une reserve")
        print("3. afficher les animaux d'une reserve")
        print("4. afficher les plantes dans une reserve")
        print("5. chercher un garde forestier")
        print("6. chercher un animal avec ses caracteristiques et son lieu d'habitat")
        print("7. chercher une plante avec ses caracteristiques et son lieu d'habitat")
        print("8. Retour\n")
        rep = int(input("\033[1;37mchoix: "))
    match rep:
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
            chercher_animal(conn) #affichage a revoir
        case 7:
            chercher_fleur(conn) #affichage a revoir
            

def affiche_une_table(conn):
    cur = conn.cursor()
    table = str(input("Donnez le nom de la table a afficher: "))
    cur.execute("""
                SELECT *
                FROM
                """+table)

    rows = cur.fetchall()
    affichage_requete(rows)
        
def parcours_dune_reserve(conn):
    cur = conn.cursor()
    reserve = str(input("Donnez le nom de la reserve : "))
    cur.execute("""
                SELECT *
                FROM Parcours JOIN Traverse USING (nom_parcours)
                              JOIN Reserves_base USING (nom_reserve)
                WHERE Reserves_base.nom_parcours = ?
                """,[reserve])

    rows = cur.fetchall()
    print("\n")
    affichage_requete(rows)
        
def animaux_de_la_reserve(conn):
    cur = conn.cursor()
    reserve = str(input("Donnez le nom de la reserve : "))
    cur.execute("""
                SELECT nom_faune
                FROM Faune JOIN Habite USING (nom_faune)
                WHERE Habite.nom_reserve = ?
                """,[reserve])
    print("\n")
    rows = cur.fetchall()
    affichage_requete(rows)
        
def fleurs_de_la_reserve(conn):
    cur = conn.cursor()
    reserve = str(input("Donnez le nom de la reserve : "))
    cur.execute("""
                SELECT nom_flore
                FROM Flore JOIN PousseDans USING (nom_flore)
                           JOIN Reserves_base USING (nom_reserve)
                WHERE Reserves_base.nom_reserve = ?
                """,[reserve])
    print("\n")
    rows = cur.fetchall()
    affichage_requete(rows)
        
def cherche_garde(conn):
    cur = conn.cursor()
    garde = str(input("Donnez le nom du garde : "))
    garde2 = str(input("Donnez le prenom du garde : "))
    cur.execute("""
                SELECT *
                FROM GardesForestier
                WHERE nom_garde_forestier = ? AND prenom_garde_forestier = ?
                """,[garde,garde2])
    print("\n")
    rows = cur.fetchall()
    affichage_requete(rows)
        
def chercher_animal(conn):
    cur = conn.cursor()
    animal = str(input("Donnez le nom de l'animal : "))
    cur.execute("""
                SELECT *
                FROM Faune JOIN Habite USING (nom_faune)
                WHERE nom_faune = ?
                """,[animal])
    print("\n")
    rows = cur.fetchall()
    affichage_requete(rows)
        
def chercher_fleur(conn):
    cur = conn.cursor()
    plante = str(input("Donnez le nom de la plante : "))
    cur.execute("""
                SELECT *
                FROM Flore JOIN PousseDans USING (nom_flore)
                WHERE nom_flore = ?
                """,[plante])
    print("\n")
    rows = cur.fetchall()
    affichage_requete(rows)
        
def inserer_des_donnees(conn):
    cur = conn.cursor()
    liste=[]
    table = str(input("Donnez le nom de la Table ou il faut inserer des donnees : "))
    taille = taille_table(conn,table)
    chaine="?"
    for i in range(taille):
        liste.append(input(f"valeur numero {i+1} : "))
        if i != taille-1:
            chaine+=",?"
    
    cur.execute("""
                INSERT INTO """+table+""" VALUES ("""+ chaine +""")
                """,liste)
    print("\n")
    conn.commit()
        
def taille_table(conn,table):
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)
    rows = cur.fetchall()
    for row in rows:
        print("Exemple des arguments que vous devez mettre:")
        print(row)
        return len(row)
    
def nom_colonnes_table(conn):  
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)
    rows = cur.fetchall()
    print(rows)
    return rows 
    
    
def mettre_a_jour_des_donnees(conn):
    cur = conn.cursor()
    liste=[]
    table = str(input("Donnez le nom de la Table ou il faut modifier une donnee : "))
    nbcolonne = int(input("Donnez le nombre de colonnes a modifier : "))
    requete = "UPDATE "+table+" SET "
    for i in range(nbcolonne):
        colonne = str(input(f"colonne n{i+1} : "))
        liste.append(str(input(f"nouvelle valeur n{i+1} : ")))
        if i != nbcolonne-1:
            requete= requete+colonne+"= ? ,"
        else:
            requete= requete+colonne+"= ? WHERE "
    nbcondition = int(input("Donnez le nombre de conditions a ajouter : "))
    if nbcondition > 1:
        andor=str(input("voulez vous que toutes les conditions soient respectees, ou l'une d'elles (and/or) ? :"))
    
    for i in range(nbcondition):
        colonne = str(input(f"colonne n{i+1} : "))
        liste.append(str(input(f"valeur dans la condition n{i+1} : ")))
        if i != nbcondition-1:
            if andor == 'or':
                requete= requete+colonne+"= ? OR "
            else:
                requete= requete+colonne+"= ? AND "
        else:
            requete= requete+colonne+"= ?"

    cur.execute(requete,liste)
    print("\n")
    conn.commit()
    
def supprimer_valeur(conn):
    print("cette fonction n'est pas encore finie, veuillez repasser + tard : )")
    
def creer_table(conn):
    print("cette fonction n'est pas encore finie, veuillez repasser + tard : )")
    
def supprimer_table(conn):
    print("cette fonction n'est pas encore finie, veuillez repasser + tard : )")