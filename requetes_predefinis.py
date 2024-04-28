#!/usr/bin/python3
from affichage_req import * 

def requete_predef(conn):
    """Menu secondaire pour que l'utilisateur ait du choix, cette fonction agit comme main et menu"""
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
            chercher_animal(conn) #affichage a revoir
        case 7:
            chercher_fleur(conn) #affichage a revoir
            


        
def parcours_dune_reserve(conn):
    """affiche les parcours disponible dans une reserve"""
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
    """affiche les animaux d'une reserve"""
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
    """affiche les fleurs d'une reserve"""
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
    """affiche les gardes d'une reserve"""
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
    """permet de trouver la fiche d'identité d'un animal dans la bdd"""
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
    """permet de trouver la fiche d'identité d'une fleur dans la bdd"""
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
    """Permet d'inserer des donnees dans une table"""
    cur = conn.cursor()
    liste=[]
    verif=[]
    table = str(input("Donnez le nom de la Table ou il faut inserer des donnees : ")) #on recupere le nom d'une table
    verif = affiche_nom_table(conn,1) #permet de recuperer la liste des tables existantes
    if table not in verif: #permet la verification de l'existence d'une table avant d'inserer des donnees
        print("La table n'existe pas encore, veuillez la creer avant d'inserer des donnees")
        return

    taille = taille_table(conn,table) #permet d'avoir la longeur de la table
    chaine="?"
    for i in range(taille): #on ajoute autant de valeurs qu'il y a d'attributs dans la table
        liste.append(input(f"valeur numero {i+1} : "))
        if i != taille-1: #permet d'ajouter le bon nombre d'arguments dans la requete
            chaine+=",?"
    #execution de la requete
    cur.execute("""
                INSERT INTO """+table+""" VALUES ("""+ chaine +""")
                """,liste)
    print("\n")
    conn.commit() #pseudo-ecriture dans la bdd
        
def taille_table(conn,table):
    """renvoie la taille de la table passe en argument"""
    cur = conn.cursor()
    t = affiche_attributs_table(conn, table) #recupere la liste des attributs d'une table
    print("Ce que vous devez mettre:")
    print(t) #affiche le nom de attributs de la table, afin de guider l'utilisateur dans l'insertion de donnees
    return len(t)


def supprimer_dernier_caractere(chaine):
    """supprime le dernier caractere d'une chaine de caractere"""
    liste = chaine.split()
    liste.pop()
    return " ".join(liste)
    
    
def mettre_a_jour_des_donnees(conn):
    """Cette fonction permet de mettre a jour des donnees dans un table"""
    cur = conn.cursor()
    liste=[]
    table = str(input("Donnez le nom de la Table ou il faut modifier une donnee : ")) #recuperation de la table
    nbcolonne = int(input("Donnez le nombre de colonnes a modifier : ")) #permet la modification d'une ou plusieurs valeurs en meme temps
    requete = "UPDATE "+table+" SET " #debut de la requete (qu'on met a jour par la suite)
    for i in range(nbcolonne): #'modification' des valeurs choisies
        colonne = str(input(f"colonne a modifier n{i+1} : ")) #colonne ou modifier la valeur
        liste.append(str(input(f"nouvelle valeur n{i+1} : ")))#nouvelle valeur
        if i != nbcolonne-1: #suite de l'ecriture de la requete en fonction du nombre de donnees modifiee
            requete= requete+colonne+"= ? ,"
        else:
            requete= requete+colonne+"= ? WHERE "
    nbcondition = int(input("Donnez le nombre de conditions a ajouter : ")) #permet de trouver les anciennes valeurs a modifier
    if nbcondition > 1: #permet d'ajouter plusieurs valeurs/endroits a modifier, avec des and ou des or au choix
        andor=str(input("voulez vous que toutes les conditions soient respectees, ou l'une d'elles (and/or) ? :"))
    elif nbcondition == 0: #permet de pas causer une erreur si l'utilisateur ne choisit pas de rentrer les donnees a remplacer
        print("Une condition minimum est obligatoire ! Sinon on ne sait pas quels sont les donnees qu'il faut remplacer")
        return
    for i in range(nbcondition): #permet de rentrer les donnees a remplacer
        colonne = str(input(f"colonne n{i+1} : "))
        liste.append(str(input(f"valeur dans la condition n{i+1} : ")))
        if i != nbcondition-1: #ecriture de la requete, avec des and ou or au choix
            if andor == 'or': #permet de choisir entre or et and (and par defaut)
                requete= requete+colonne+"= ? OR "
            else:
                requete= requete+colonne+"= ? AND "
        else:
            requete= requete+colonne+"= ?"

    cur.execute(requete,liste) #execution de la requete
    print("\n")
    conn.commit() #pseudo-ecriture dans la bdd







def supprimer_valeur(conn):
    """permet de supprimer une valeur dans une table, si celles-ci existent"""
    cur = conn.cursor()
    table = str(input("Donnez le nom de la Table ou il faut supprimer une/toute donnee : "))
    colonne = str(input("Donnez la colonne ou il faut supprimer une donnee : "))
    valeur = input("Donnez la valeur de cette colonne a supprimer : ")
    requete = "DELETE FROM "+table+" WHERE "+colonne+" = ?"
    cur.execute(requete,[valeur])
    print("\n")
    conn.commit()






def creer_table(conn):
    """permet de creer une table"""
    cur = conn.cursor()
    liste=[]
    requete = "CREATE TABLE IF NOT EXISTS " #debut de la requete
    table = str(input("Donnez le nom de la Table a creer : "))
    requete = requete + table + " ( "
    nbattributs = int(input("Donnez le nombre d'attributs : ")) #permet de creer une table avec le nombre d'attributs qu'on souhaite
    for i in range(nbattributs):
        colonne = str(input(f"colonne n{i+1} : "))
        type = str(input("Donnez le type de l'attribut (INTEGER/TEXT/DATE/REAL/...) : ")) #permet d'associer un type a chaque attribut
        requete = requete +" "+ colonne+" "+type + " NOT NULL ," #ecriture de la requete

    pk = str(input("Ajouter une primary key ? (o/n) : ")) #l'utilisateur peut rajouter une primary key si il le souhaite
    if pk == "o":
        nom = str(input("nom de la primary key : "))
        requete = requete + "CONSTRAINT pk_"+nom+" PRIMARY KEY ("+nom+") ," #ecriture de la primary key
    nbfk = int(input("Combien de foreign key ? : ")) #l'utilisateur choisit combien de foreign key il veut ajouter (il peut mettre 0)
    for i in range(nbfk): #construction des lignes de foreign key
        fk = str(input("nom de la foreign key/attribut a lier : "))
        fk2 = str(input("nom de la table a lier : "))
        fk3 = str(input("nom de l'attribut a lier dans l'autre table : "))
        requete = requete + "CONSTRAINT fk_"+fk +" FOREIGN KEY ("+fk+") REFERENCES "+fk2+"("+fk3+") ," #ecriture des foreign key
    nbc = int(input("Combien de check ? : ")) #l'utilisateur peut ajouter des check si il veut
    for i in range(nbc):#permet l'ecriture des check
        ck = str(input("nom de la colonne a check : "))
        cond = str(input("condition (attribut = condition) : "))
        op = str(input("operande (=/</>/!=/<=/>=) : "))
        requete = requete+"CONSTRAINT ck_"+ck+" CHECK ("+ck+" "+op+" "+cond+") ," #ecriture du check
    requete = supprimer_dernier_caractere(requete) #permet de supprimer la derniere virgule dans la requete (cette methode permet d'optimiser un peu la fonction)
    requete+=')'
    cur.execute(requete) #execution de la requete
    print("\n")
    conn.commit()#pseudo-ecriture de la nouvelle table dans la bdd





def supprimer_table(conn):
    """permet de supprimer une table, si celle-ci existe"""
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
    table = str(input("Donnez le nom de la Table a supprimer : "))
    cur.execute("DROP TABLE IF EXISTS "+table)
    print("\n")
    conn.commit()
