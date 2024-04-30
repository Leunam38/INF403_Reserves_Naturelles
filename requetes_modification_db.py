#!/usr/bin/python3
from utils import db
import sqlite3
from affichage_req import * 

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

      
        
def inserer_des_donnees(conn):
    """Permet d'inserer des donnees dans une table
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    liste=[]
    table=choix_table(conn)
    if table==None: #Si la table n'a pas été trouvé
        return

    print("\033[1;35mRemplissez les différents information:")
    tab = affiche_attributs_table(conn, table) #recupere la liste des attributs d'une table
    taille = len(tab) #permet d'avoir la longeur de la table
    chaine="?"
    for i in range(taille): #on ajoute autant de valeurs qu'il y a d'attributs dans la table
        liste.append(input(f"\033[1;36m{tab[i]} : \033[1;37m"))
        if i != taille-1: #permet d'ajouter le bon nombre d'arguments dans la requete
            chaine+=",?"
    #execution de la requete
    cur.execute("""
                INSERT INTO """+table+""" VALUES ("""+ chaine +""")
                """,liste)
    print("")
    conn.commit() #pseudo-ecriture dans la bdd


def supprimer_dernier_caractere(chaine):
    """supprime le dernier caractere d'une chaine de caractere"""
    liste = chaine.split()
    liste.pop()
    return " ".join(liste)
    
    
def mettre_a_jour_des_donnees(conn):
    """Met à jour des données dans un table
    
    :param conn: Connexion à la base de données
    """
    
    cur = conn.cursor()
    liste=[]
    table=choix_table(conn) #recuperation de la table
    
    nbcolonne = int(input("Donnez le nombre de colonnes a modifier : ")) #permet la modification d'une ou plusieurs valeurs en meme temps
    requete = "UPDATE "+table+" SET " #debut de la requete (qu'on met a jour par la suite)
    attributs = affiche_attributs_table(conn,table,1) #Récup toute la liste des colonnes
    
    for i in range(nbcolonne): #'modification' des valeurs choisies
        colonne = str(input(f"Nom colonne a modifier n{i+1} : ")) #colonne ou modifier la valeur
        if colonne not in attributs: 
            print("La colonne n'exite pas")
            return
        liste.append(str(input(f"Nouvelle valeur n{i+1} : ")))#nouvelle valeur
        
        requete= requete+colonne+"= ? "
        if i != nbcolonne-1: #suite de l'ecriture de la requete en fonction du nombre de donnees modifiee
            requete= requete+","
            
            
    nbcondition = int(input("Donnez le nombre de conditions a ajouter : ")) #permet de trouver les anciennes valeurs a modifier
    if nbcondition > 1: #permet d'ajouter plusieurs valeurs/endroits a modifier, avec des and ou des or au choix
        requete= requete+"WHERE "
        andor=str(input("voulez vous que toutes les conditions soient respectees, ou l'une d'elles (and/or) ? :"))
    
    for i in range(nbcondition): #permet de rentrer les donnees a remplacer
        colonne = str(input(f"colonne n{i+1} : "))
        liste.append(str(input(f"valeur dans la condition n{i+1} : ")))
        if colonne not in attributs: 
            print("La colonne n'exite pas")
            return
        if i != nbcondition-1: #ecriture de la requete, avec des and ou or au choix
            if andor == 'or': #permet de choisir entre or et and (and par defaut)
                requete= requete+colonne+"= ? OR "
            else:
                requete= requete+colonne+"= ? AND "
        else:
            requete= requete+colonne+"= ?"

    cur.execute(requete,liste) #execution de la requete
    conn.commit() 





def supprimer_valeur(conn):
    """Supprime une valeur dans une table, si celles-ci existent
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    print("Faite attention, donnez le nom de la Table ou il faut supprimer une/toute donnee")
    table=choix_table(conn) #recuperation de la table
    if table == None:
        return
    
    attributs = affiche_attributs_table(conn,table,1) #Récup toute la liste des colonnes
    
    colonne = str(input("Donnez la colonne ou il faut supprimer une donnee : "))
    if colonne not in attributs: 
            print("La colonne n'existe pas")
            return
    valeur = input("Donnez la valeur de cette colonne a supprimer : ")
    requete = "DELETE FROM "+table+" WHERE "+colonne+" = ?"
    cur.execute(requete,[valeur])
    conn.commit()


def creer_table(conn):
    """Creer une table
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    liste=[]
    requete = "CREATE TABLE IF NOT EXISTS " #debut de la requete
    table = str(input("Donnez le nom de la Table a creer : "))
    
    verif = affiche_nom_table(conn,0)
    if table in verif:
        print(f"La table {table} existe déjà.")
        return
    
    requete = requete + table + " ( "
    nbattributs = int(input("Donnez le nombre d'attributs : ")) #permet de creer une table avec le nombre d'attributs qu'on souhaite
    attributs=[]
    
    for i in range(nbattributs):
        colonne = str(input(f"colonne n{i+1} : "))
        attributs.append(colonne)
        type_att = str(input("Donnez le type de l'attribut (INTEGER/TEXT/DATE/REAL/...) : ")) #permet d'associer un type a chaque attribut
        requete = requete +" "+ colonne+" "+type_att + " NOT NULL ," #ecriture de la requete

    pk = str(input("Ajouter une primary key ? (o/n) : ")) #l'utilisateur peut rajouter une primary key si il le souhaite
    if pk == "o":
        nom = str(input("nom de l'attribut qui sera la primary key : "))
        if nom not in attributs:
            print("Mauvais nom d'attribut inexistant")
            return
        requete = requete + "\nCONSTRAINT pk_"+nom+" PRIMARY KEY ("+nom+") ," #ecriture de la primary key
        
    nbfk = int(input("Combien de foreign key ? : ")) #l'utilisateur choisit combien de foreign key il veut ajouter (il peut mettre 0)
    for i in range(nbfk): #construction des lignes de foreign key
        fk = str(input(f"nom de la foreign key/attribut a lier numéro {i+1}: "))
        if fk not in attributs:
            print("Mauvais nom d'attribut inexistant")
            return
        fk2 = str(input("nom de la table a lier : "))
        if fk2 not in verif:
            print(f"La table {fk2} existe pas.")
            return
    
        attributs_relie = affiche_attributs_table(conn,fk2,1) #Récup toute la liste des colonnes
        fk3 = str(input("nom de l'attribut a lier dans l'autre table : "))
        if fk3 not in attributs_relie: 
                print("La colonne n'exite pas")
                return
                    
        requete = requete + "CONSTRAINT fk_"+fk+"_"+i+" FOREIGN KEY ("+fk+") REFERENCES "+fk2+"("+fk3+") ," #ecriture des foreign key
    
    nbc = int(input("Combien de check ? : ")) #l'utilisateur peut ajouter des check si il veut
    for i in range(nbc):#permet l'ecriture des check
        ck = str(input("nom de la colonne a check : "))
        if ck not in attributs:
            print("Mauvais nom d'attribut inexistant")
            return
        cond = str(input("condition (attribut = condition) : "))
        op = str(input("operande (=/</>/!=/<=/>=) : "))
        requete = requete+"CONSTRAINT ck_"+ck+"_"+i+" CHECK ("+ck+" "+op+" "+cond+") ," #ecriture du check
        
    liste_split = requete.split()
    liste_split.pop()
    requete = " ".join(liste_split)+')'
    
    cur.execute(requete) #execution de la requete
    conn.commit()





def supprimer_table(conn):
    """permet de supprimer une table, si celle-ci existe
    
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    #avertissement a l'utilisateur, lui disant qu'une table ne peut etre supprimee suivant un certain ordre (pour ne pas exploser toute la bdd)
    warn = str(input("/!\ Attention, supprimer les tables se fait dans un ordre précis, voulez-vous voir la liste des tables supprimable DANS L'ORDRE ? (o/n) : "))
    if warn == "o": #liste des tables supprimable dans l'ordre, C.A.D ne pas supprimer une table en bas de liste des le debut
        print("- tables personnalisées")
        print("- Traverse")
        print("- PousseDans")
        print("- Habite")
        print("- GardesForestier")
        print("- Parcours")
        print("- Flore")
        print("- Faune")
        print("- Reserves_base")
        print("- Reserves")
        
    table= choix_table(conn)
    if table != None:
        cur.execute("DROP TABLE IF EXISTS "+table)
        print("\n")
        conn.commit()
