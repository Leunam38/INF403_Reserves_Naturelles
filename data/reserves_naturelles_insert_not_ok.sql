-- Jeux de données NOK (ne doit pas marcher àprès avoir éxécuté le jeux de données normal)

--Erreur : superficie nulle ou négative, il ne peut pas exister une reserve naturelle qui n'a pas d'espace
INSERT INTO Reserves_base VALUES ("Réserve Naturelle de la Grotte de Belville","FR3600047",0,'10/09/1980',01);
--Erreur : Reserve existante
INSERT INTO Reserves_base VALUES ("Reserve Naturelle du Cirque du grand lac des Estaris","FR3699915",111.00,'15/05/1934',19);
--Erreur : Code de reserve existante
INSERT INTO Reserves_base VALUES ("Reserve naturelle du Cirque de Scandola","FR9400063",340.00,'11/12/1973',72);
--Erreur : Departement inexistant (departement > 96, il n'existe pas de departement numero 99 en France)
INSERT INTO Reserves_base VALUES ("Réserve Naturelle d'Iroise","FR3600047",10.22,'10/09/1980',99); 
--Erreur : Date de création invalide (date inexistante)
INSERT INTO Reserves_base VALUES ("Reserve naturelle de la baie de Monaco","FR5355555",20.00,'60/14/2019',27);

--Erreur : Taille moyenne nulle ou inexistante 
INSERT INTO Faune VALUES ("Faucon pelerin",0,"marron","herbivore","oui");
--Erreur : Regime alimentaire autres que  insectivore, carnivore, herbivore, omnivore 
INSERT INTO Faune VALUES ("Faucon pelerin",2.1,"marron","vegetarien","oui"); 
--Erreur : Type de protection autres que "oui" ou "non"
INSERT INTO Faune VALUES ("Faucon pelerin",0.65,"marron","herbivore","peut-etre"); 
--Erreur : Animal existant
INSERT INTO Faune VALUES ("Lievre",0.79,"marron","omnivore","non");



--Erreur : Type de flore autres que arbre, arbuste, plante, fleur, champignon
INSERT INTO Flore VALUES ("Rhododendron","Éricacées","tige","non"); 
--Erreur : Type de protection autres que "oui" ou "non"
INSERT INTO Flore VALUES ("Sapin","Pinaceae","arbre","eventuellement");
--Erreur : Plante existante
INSERT INTO Flore VALUES ("Houx","Brassicaceae","champignon","non");

--Erreur : Departement de depart inexistant
INSERT INTO Parcours VALUES ("GR93",00,29,'06:10:00',"GR"); 
--Erreur : Departement d'arrivee inexistant
INSERT INTO Parcours VALUES ("Les Trois Becs",1,99,'05:20:00',"sentier"); 
--Erreur : Temps de parcours nulle ou négatif
INSERT INTO Parcours VALUES ("Roche Colombe depuis Saou",26,26,'00:00:00',"chemin");
--Erreur : Type de parcours autres que route, chemin, snetier, GR
INSERT INTO Parcours VALUES ("D398",49,75,'19:13:00',"terre"); 
--Erreur : Chemin de randonnee existant
INSERT INTO Parcours VALUES ("GR13",65,45,'09:52:00',"GR");


--Erreur : matricule du garde existant
INSERT INTO GardesForestier VALUES (9,"Reserve naturelle de l'etang de Saint-Bonnet","Golo","Thierry",'1980-06-06');
--Erreur : reserve de travail inexistant
INSERT INTO GardesForestier VALUES (123,"Reserve naturelle de Saint martin d'heres","Golo","Thierry",'1980-06-06');
--Erreur : Garde sans nom
INSERT INTO GardesForestier VALUES (29,"Reserve naturelle du Marais d'Orx",NULL,"Nicolas",'1992-03-04');
--Erreur : Garde sans prenom
INSERT INTO GardesForestier VALUES (30,"Reserve naturelle du Marais d'Orx","Golo",NULL,'1992-03-04');

--Erreur : l'animal habite déjà dans la reserve
INSERT INTO Habite VALUES ("Reserve naturelle nationale de la plaine des Maures","Aigle royal",133);
--Erreur : animal inexistant
INSERT INTO Habite VALUES ("Reserve naturelle nationale de la plaine des Maures","Quoicoubebou des Montagne",860);
--Erreur : reserve inexistant
INSERT INTO Habite VALUES ("Reserve naturelle d'Everste","Loutre d'Europe",988);
--Erreur : reserve et animal inexistant
INSERT INTO Habite VALUES ("Reserve naturelle de l'ascenscion de l'Everste","Inoxtag",1);
--Erreur : nombre d'animal négatif
INSERT INTO Habite VALUES ("Reserve naturelle du Marais d'Orx","Aigle royal",-33);


--Erreur : la plante pousse déjà dans la reserve
INSERT INTO PousseDans VALUES ("Reserve naturelle nationale de la grotte du Pont d'Arc","Hetre",99);
--Erreur : plante inexistant
INSERT INTO PousseDans VALUES ("Reserve naturelle nationale de la plaine des Maures","Fleur jolie",350);
--Erreur : reserve inexistant
INSERT INTO PousseDans VALUES ("Reserve naturelle de l'ascenscion de l'Everste","Tulipe sauvage",680);
--Erreur : nombre de plante négatif
INSERT INTO PousseDans VALUES ("Reserve naturelle de Scandola","Tulipe sauvage",-9);



--Erreur : parcours traverse déjà la reserve
INSERT INTO Traverse VALUES ("Reserve naturelle de l'etang de Saint-Bonnet","Roche Colombe depuis Saou");
--Erreur : parcours inexistant
INSERT INTO Traverse VALUES ("Reserve Naturelle du Massif du Montious","Chemin de l'Evereste");
--Erreur : reserve inexistant
INSERT INTO Traverse VALUES ("Reserve naturelle de l'ascenscion de l'Everste","GR13");

