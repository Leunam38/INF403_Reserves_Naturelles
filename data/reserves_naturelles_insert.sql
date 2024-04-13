INSERT INTO Reserves_base VALUES ("Reserve naturelle des Hauts de Chartreuse","FR3600136",4420.40,'01/10/1997',38);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle du Cirque du grand lac des Estaris","FR3600015",145.00,'15/05/1974',05);
INSERT INTO Reserves_base VALUES ("Reserve naturelle de l'Étang de Saint-Bonnet","FR9300069",51.40,'16/12/2011',38);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle du Massif du Montious","FR9300191",738.59,'16/07/2020',65);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle du Lac de Malaguet","FR9300141",54.21,'02/10/2014',43);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle d'Iroise","FR3600108",1129.00,'12/10/1992',29);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle de la Colline du Bastberg a Bouxwiller","FR9300109",6.45,'16/03/2012',67);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle de Lilleau des Niges","FR3600045",121.00,'31/01/1980',75);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle du Marais d'Yves","FR3600053",188.26,'28/08/1981',75);
INSERT INTO Reserves_base VALUES ("Reserve Naturelle de la Grotte de Hautecourt","FR3600047",10.22,'10/09/1980',01);




INSERT INTO Faune VALUES ("Chamois",1.25,"marron","herbivore","oui");
INSERT INTO Faune VALUES ("Ours",2.1,"marron","omnivore","oui");
INSERT INTO Faune VALUES ("Marmotte",0.65,"marron","herbivore","oui");
INSERT INTO Faune VALUES ("Sanglier",1.45,"marron","omnivore","non");
INSERT INTO Faune VALUES ("Lievre",0.55,"gris","herbivore","non");
INSERT INTO Faune VALUES ("Biche",2.1,"marron","herbivore","non");
INSERT INTO Faune VALUES ("Bison d'Europe",2.9,"marron","herbivore","oui");
INSERT INTO Faune VALUES ("Corneille noire",0.52,"noire","omnivore","non");
INSERT INTO Faune VALUES ("Mesange charbonniere",0.24,"jaune","omnivore","non");
INSERT INTO Faune VALUES ("Renards",0.67,"orange","carnivore","non");





INSERT INTO Flore VALUES ("Rhododendron","Éricacees","fleur","non");
INSERT INTO Flore VALUES ("Sapin","Pinaceae","arbre","non");
INSERT INTO Flore VALUES ("Morilles","Morchellaceae","fleur","oui");
INSERT INTO Flore VALUES ("Bouleau","Betulacees","arbre","non");
INSERT INTO Flore VALUES ("Fougere","Dennstaedtiaceae","plante","non");
INSERT INTO Flore VALUES ("Anemone sauvage","Renonculacees","fleur","oui");
INSERT INTO Flore VALUES ("Scandix etoile","Apiaceae","plante","oui");
INSERT INTO Flore VALUES ("Corbeille d'argent des Pyrenees","Brassicaceae","fleur","oui");
INSERT INTO Flore VALUES ("Niveole d'ete","Amaryllidaceae","fleur","oui");
INSERT INTO Flore VALUES ("Fontinale chevelue","Bryophytes","plante","oui");





INSERT INTO Parcours VALUES ("GR93",11,29,'06:30:00',"GR");
INSERT INTO Parcours VALUES ("Les Trois Becs",01,29,'05:20:00',"sentier");
INSERT INTO Parcours VALUES ("Roche Colombe depuis Saou",26,26,'04:15:00',"chemin");
INSERT INTO Parcours VALUES ("D398",49,75,'19:13:00',"route");
INSERT INTO Parcours VALUES ("GR20",93,93,'20:20:00',"GR");
INSERT INTO Parcours VALUES ("GR13",65,45,'03:52:00',"GR");
INSERT INTO Parcours VALUES ("Plateau des Charmilles",01,01,'08:25:00',"sentier");
INSERT INTO Parcours VALUES ("D234",06,07,'19:13:00',"route");
INSERT INTO Parcours VALUES ("GR29",49,22,'02:20:00',"GR");
INSERT INTO Parcours VALUES ("GR77",32,38,'07:07:00',"GR");





INSERT INTO GardesForestier VALUES (0,"Reserve naturelle des Hauts de Chartreuse","Cepacare","Ciceron",'12/03/1959');
INSERT INTO GardesForestier VALUES (1,"Reserve Naturelle de la Colline du Bastberg a Bouxwiller","Debonzieu","Ella",'22/12/1989');
INSERT INTO GardesForestier VALUES (2,"Reserve Naturelle du Marais d'Yves","Dehors","Igor",'02/04/2000');
INSERT INTO GardesForestier VALUES (3,"Reserve Naturelle d'Iroise","Ouzi","Jacques",'17/07/1988');
INSERT INTO GardesForestier VALUES (4,"Reserve Naturelle du Lac de Malaguet","Édeu","Jean",'27/01/1972');
INSERT INTO GardesForestier VALUES (5,"Reserve Naturelle de la Grotte de Hautecourt","Brille","Laure",'12/08/2004');
INSERT INTO GardesForestier VALUES (6,"Reserve Naturelle du Massif du Montious","Fer","Lucie",'15/03/1999');
INSERT INTO GardesForestier VALUES (7,"Reserve Naturelle de la Grotte de Hautecourt","Erateur","Maude",'12/03/1959');
INSERT INTO GardesForestier VALUES (8,"Reserve Naturelle du Cirque du grand lac des Estaris","Ponce","Pierre",'07/10/1969');
INSERT INTO GardesForestier VALUES (9,"Reserve naturelle de l'Étang de Saint-Bonnet","Golo","Thierry",'10/06/1980');
INSERT INTO GardesForestier VALUES (10,"Reserve Naturelle d'Iroise","Bernerd","Bart",'17/07/1989');




INSERT INTO Habite VALUES ("Reserve Naturelle du Massif du Montious","Chamois",258);
INSERT INTO Habite VALUES ("Reserve Naturelle du Cirque du grand lac des Estaris","Chamois",146);
INSERT INTO Habite VALUES ("Reserve Naturelle d'Iroise","Chamois",259);
INSERT INTO Habite VALUES ("Reserve Naturelle de la Grotte de Hautecourt","Renards",486);
INSERT INTO Habite VALUES ("Reserve naturelle de l'Étang de Saint-Bonnet","Chamois",19);
INSERT INTO Habite VALUES ("Reserve Naturelle d'Iroise","Lievre",46);
INSERT INTO Habite VALUES ("Reserve Naturelle du Lac de Malaguet","Corneille noire",761);
INSERT INTO Habite VALUES ("Reserve Naturelle du Massif du Montious","Renards",241);
INSERT INTO Habite VALUES ("Reserve Naturelle de Lilleau des Niges","Sanglier",469);
INSERT INTO Habite VALUES ("Reserve Naturelle du Lac de Malaguet","Bison d'Europe",12);





INSERT INTO pousseDans VALUES ("Reserve Naturelle du Massif du Montious","Rhododendron",2578);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Cirque du grand lac des Estaris","Morilles",1746);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Massif du Montious","Scandix etoile",761);
INSERT INTO pousseDans VALUES ("Reserve Naturelle de la Grotte de Hautecourt","Fougere",973);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Massif du Montious","Niveole d'ete",781);
INSERT INTO pousseDans VALUES ("Reserve Naturelle d'Iroise","Corbeille d'argent des Pyrenees",99);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Lac de Malaguet","Bouleau",432);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Massif du Montious","Fougere",9791);
INSERT INTO pousseDans VALUES ("Reserve Naturelle de Lilleau des Niges","Anemone sauvage",316);
INSERT INTO pousseDans VALUES ("Reserve Naturelle du Lac de Malaguet","Niveole d'ete",184);


INSERT INTO Traverse VALUES ("Reserve Naturelle d'Iroise","GR93");
INSERT INTO Traverse VALUES ("Reserve Naturelle du Lac de Malaguet","GR93");
INSERT INTO Traverse VALUES ("Reserve Naturelle de Lilleau des Niges","D398");
INSERT INTO Traverse VALUES ("Reserve naturelle de l'Étang de Saint-Bonnet","Roche Colombe depuis Saou");
INSERT INTO Traverse VALUES ("Reserve Naturelle du Massif du Montious","GR13");
INSERT INTO Traverse VALUES ("Reserve Naturelle du Lac de Malaguet","GR13");
INSERT INTO Traverse VALUES ("Reserve naturelle de l'Étang de Saint-Bonnet","GR77");
INSERT INTO Traverse VALUES ("Reserve naturelle des Hauts de Chartreuse","GR77");
INSERT INTO Traverse VALUES ("Reserve Naturelle de la Grotte de Hautecourt","GR77");
INSERT INTO Traverse VALUES ("Reserve Naturelle de la Grotte de Hautecourt","Plateau des Charmilles");