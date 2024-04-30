SELECT nom_faune,couleur_faune
FROM Faune;

SELECT nom_faune
FROM Faune
WHERE est_protege_faune="oui" AND taille_moyenne_faune>1.2;

SELECT nom_parcours
FROM Traverse
WHERE nom_reserve="Reserve Naturelle du Marais d'Yves";

SELECT DISTINCT nom_reserve
FROM PousseDans JOIN Flore USING(nom_flore)
WHERE type_flore="arbre";

--Nombre de garde dans les réserves en Isère

SELECT COUNT(matricule_garde_forestier) AS nb_garde
FROM GardesForestier JOIN Reserves ON (nom_reserve=reserve_de_travail_garde_forestier)
WHERE numero_departement_reserve=38;

SELECT nom_reserve,COUNT(matricule_garde_forestier) AS nb_garde
FROM GardesForestier JOIN Reserves ON (nom_reserve=reserve_de_travail_garde_forestier)
GROUP BY nom_reserve
UNION
SELECT nom_reserve,0
FROM Reserves 
WHERE nom_reserve NOT IN (SELECT reserve_de_travail_garde_forestier
						  FROM GardesForestier);
						  
SELECT type_flore,COUNT(nom_flore) AS nb_type_flore
FROM Flore
GROUP BY type_flore;


SELECT (strftime('%Y', 'now') - strftime('%Y', date_de_naissance_garde_forestier))- (strftime('%m-%d', 'now') < strftime('%m-%d', date_de_naissance_garde_forestier)) AS age_adherent
FROM GardesForestier;


/*

*/