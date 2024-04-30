#!/usr/bin/python3
from affichage_req import * 


def requete_exemple(conn):
    """
    Affiche la liste de toutes les reserves.

    :param conn: Connexion à la base de données
    """
    rep=0
    while rep < 1 or rep > 14:
        print("\033[1;35mChoisissez une des requetes d'exemple:")
        print("\033[1;36m1. Affiche toutes les réserves")
        print("2. Affiche tous animaux avec leurs couleur")
        print("3. Affiche tous les animaux proteges qui font plus grand que 1.2m en moyenne")
        print("4. Affiche tous les parcours qui passe par la réserve 'Reserve Naturelle du Marais d'Yves'")
        print("5. Affiche le nom des réserves qui contienne une plante de type arbre")
        print("6. Affiche le nombre de garde dans les réserves en Isère (38)")
        print("7. Affiche le nombre de garde pour chaque réserve")
        print("8. Affiche le nombre de flore différente suivante son type")
        print("9. Affiche tous les gardes de plus de 50 ans")
        print("10. Affiche tous les animaux protegés par une Maude qui sont accessible par le GR20")
        print("11. Affiche toutes les réserves que l'ont peut atteindre si on part du département 29")
        print("12. Affiche tous les animaux qui ne sont pas noir")
        print("13. Affiche toutes les reserves qui contienne des fleurs et qui ont plus de 1000 animaux de grande/moyenne taille (plus de 50cm)")
        print("14. Retour\n")
        rep = int(input("\033[1;37mchoix: "))
        print("")
    match rep:
        case 1:
            select_toutes_les_reserves(conn)
        case 2:
            select_animaux_color(conn) 
        case 3:
            select_animaux_proteges_taille(conn)
        case 4:
            select_parcours_marais(conn)
        case 5:
            select_reserves_arbre(conn)
        case 6:
            select_nb_garde_isere(conn) 
        case 7:
            select_nb_garde_global(conn)
        case 8:
            select_group_type_flore(conn)
        case 9:
            select_garde_agee(conn)
        case 10:
            select_faune_maude_prot_gr20(conn)
        case 11:
            select_reserve_dep_29(conn) 
        case 12:
            select_faune_non_noir(conn)
        case 13:
            select_reserve_1000_anim_grand(conn) 


def select_toutes_les_reserves(conn):
    """
    Affiche la liste de toutes les reserves.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Reserves
                """)
    rows = cur.fetchall()
    affichage_requete(rows)


def select_animaux_color(conn):
    """
    Affiche la liste de tous les animaux avec leurs couleur.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_faune,couleur_faune
                FROM Faune;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)


def select_animaux_proteges_taille(conn):
    """
    Affiche la liste de tous les animaux proteges.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_faune
                FROM Faune
                WHERE est_protege_faune="oui" AND taille_moyenne_faune>1.2;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
        
        
def select_parcours_marais(conn):
    """
    Affiche la liste des parcours qui passe par la réserve 'Reserve Naturelle du Marais d'Yves'

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_parcours
                FROM Traverse
                WHERE nom_reserve="Reserve Naturelle du Marais d'Yves";
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
        
                
def select_reserves_arbre(conn):
    """
    Affiche la liste des noms des réserves qui contienne une plante de type arbre

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT DISTINCT nom_reserve
                FROM PousseDans JOIN Flore USING(nom_flore)
                WHERE type_flore="arbre";
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
            
                
def select_nb_garde_isere(conn):
    """
    Affiche le nombre de garde dans les réserves en Isère (38)

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT COUNT(matricule_garde_forestier) AS nb_garde
                FROM GardesForestier JOIN Reserves ON (nom_reserve=reserve_de_travail_garde_forestier)
                WHERE numero_departement_reserve=38;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
                
                
def select_nb_garde_global(conn):
    """
    Affiche le nombre de garde pour chaque réserve

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_reserve,COUNT(matricule_garde_forestier) AS nb_garde
                FROM GardesForestier JOIN Reserves ON (nom_reserve=reserve_de_travail_garde_forestier)
                GROUP BY nom_reserve
                UNION
                SELECT nom_reserve,0
                FROM Reserves 
                WHERE nom_reserve NOT IN (SELECT reserve_de_travail_garde_forestier
                                        FROM GardesForestier);
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
                  
                
def select_group_type_flore(conn):
    """
    Affiche le nombre de flore différente suivante son type

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT type_flore,COUNT(nom_flore) AS nb_type_flore
                FROM Flore
                GROUP BY type_flore;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    
                    
def select_garde_agee(conn):
    """
    Affiche tous les gardes de plus de 50 ans

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                WITH garde_age_tab AS (SELECT matricule_garde_forestier,(strftime('%Y', 'now') - strftime('%Y', date_de_naissance_garde_forestier))- 
                (strftime('%m-%d', 'now') < strftime('%m-%d', date_de_naissance_garde_forestier)) AS age_garde
                FROM GardesForestier)
                SELECT matricule_garde_forestier, prenom_garde_forestier, nom_garde_forestier
                FROM garde_age_tab JOIN GardesForestier USING (matricule_garde_forestier)
                WHERE age_garde>50;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    
    
def select_faune_maude_prot_gr20(conn):
    """
    Affiche la liste de tous les animaux protegés par une Maude qui sont accessible par le GR20

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT DISTINCT nom_faune
                FROM Traverse JOIN Reserves USING (nom_reserve)
                            JOIN GardesForestier ON (nom_reserve=reserve_de_travail_garde_forestier)
                            JOIN Habite USING (nom_reserve)
                            JOIN Faune USING (nom_faune)
                WHERE prenom_garde_forestier="Maude" AND est_protege_faune="oui" AND nom_parcours="GR20";
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    

def select_reserve_dep_29(conn):
    """
    Affiche la liste toutes les réserves que l'ont peut atteindre si on part du département 29

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_reserve
                FROM Reserves
                WHERE numero_departement_reserve=29
                UNION 
                SELECT nom_reserve
                FROM Traverse JOIN Parcours USING (nom_parcours)
                WHERE departement_depart_parcours=29 OR departement_arrivee_parcours=29;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    
    
def select_faune_non_noir(conn):
    """
    Affiche la liste de tous les animaux qui ne sont pas noir

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_faune
                FROM Faune
                EXCEPT 
                SELECT nom_faune
                FROM Faune
                WHERE couleur_faune="noir"; 
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    
    
def select_reserve_1000_anim_grand(conn):
    """
    Affiche la liste de toutes les reserves qui contienne des fleurs 
    et qui ont plus de 1000 animaux de grande/moyenne taille (plus de 50cm)

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT nom_reserve
                FROM PousseDans JOIN Flore USING(nom_flore)
                WHERE type_flore="arbre"
                INTERSECT
                SELECT nom_reserve
                FROM Habite JOIN Faune USING (nom_faune)
                WHERE taille_moyenne_faune>0.5
                GROUP BY nom_reserve
                HAVING SUM(nb_individus_habite) >1000;
                """)
    rows = cur.fetchall()
    affichage_requete(rows)
    
