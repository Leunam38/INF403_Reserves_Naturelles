CREATE TABLE IF NOT EXISTS Reserves_base(
	nom_reserve TEXT NOT NULL,
	code_reserve TEXT NOT NULL,
	superficie_reserve REAL NOT NULL,
	date_creation_reserve DATE NOT NULL,
	numero_departement_reserve INTEGER NOT NULL,
	CONSTRAINT pk_reserve PRIMARY KEY (nom_reserve),
	CONSTRAINT uk_reserve_code UNIQUE (code_reserve),
	CONSTRAINT ck_reserve_superficie CHECK (superficie_reserve > 0),
	CONSTRAINT ck_reserve_numero_departement CHECK (numero_departement_reserve > 0 AND numero_departement_reserve < 97)	
	CONSTRAINT ck_valid_date_reserve CHECK(date_creation_reserve IS date(date_creation_reserve,'+0 days'))
);
	
CREATE TABLE IF NOT EXISTS Faune(
	nom_faune TEXT NOT NULL,
	taille_moyenne_faune REAL NOT NULL,
	couleur_faune TEXT NOT NULL,
	regime_alimentaire_faune TEXT NOT NULL,
	est_protege_faune TEXT NOT NULL,
	CONSTRAINT pk_faune PRIMARY KEY (nom_faune),
	CONSTRAINT ck_faune_taille CHECK (taille_moyenne_faune > 0),
	CONSTRAINT ck_faune_regime CHECK (regime_alimentaire_faune = 'carnivore' OR regime_alimentaire_faune = 'omnivore' OR regime_alimentaire_faune = 'herbivore' OR regime_alimentaire_faune = 'insectivore'),
	CONSTRAINT ck_faune_protege CHECK (est_protege_faune = 'oui' OR est_protege_faune = 'non')
);

CREATE TABLE IF NOT EXISTS Flore(
	nom_flore TEXT NOT NULL,
	famille_flore TEXT NOT NULL,
	type_flore TEXT NOT NULL,
	est_protege_flore TEXT NOT NULL,
	CONSTRAINT pk_flore PRIMARY KEY (nom_flore),
	CONSTRAINT ck_flore_type CHECK (type_flore = 'arbre' OR type_flore = 'arbuste' OR type_flore = 'plante' OR type_flore = 'fleur' OR type_flore = 'champignon'),
	CONSTRAINT ck_flore_protege CHECK (est_protege_flore = 'oui' OR est_protege_flore = 'non')
);
	
CREATE TABLE IF NOT EXISTS Parcours(
	nom_parcours TEXT NOT NULL,
	departement_depart_parcours INTEGER NOT NULL,
	departement_arrivee_parcours INTEGER NOT NULL,
	duree_parcours TIME NOT NULL,
	type_parcours TEXT NOT NULL,
	CONSTRAINT pk_parcours PRIMARY KEY (nom_parcours),
	CONSTRAINT ck_parcours_depart CHECK (departement_depart_parcours > 0 AND departement_depart_parcours < 97),
	CONSTRAINT ck_parcours_arrivee CHECK (departement_arrivee_parcours > 0 AND departement_arrivee_parcours < 97),	
	CONSTRAINT ck__parcours_duree CHECK (duree_parcours > '00:00:00'),
	CONSTRAINT ck__parcours_type CHECK (type_parcours = 'chemin' OR type_parcours = 'route' OR type_parcours = 'GR' OR type_parcours = 'sentier')
);

CREATE TABLE IF NOT EXISTS GardesForestier(
	matricule_garde_forestier INTEGER NOT NULL,
	reserve_de_travail_garde_forestier TEXT NOT NULL,
	nom_garde_forestier TEXT NOT NULL,
	prenom_garde_forestier TEXT NOT NULL,
	date_de_naissance_garde_forestier DATE NOT NULL,
	CONSTRAINT pk_gardesForestier_matricule PRIMARY KEY (matricule_garde_forestier),
	CONSTRAINT fk_gardesForestier_reserve FOREIGN KEY (reserve_de_travail_garde_forestier) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT ck_valid_date_garde CHECK(date_de_naissance_garde_forestier IS date(date_de_naissance_garde_forestier,'+0 days'))

);

CREATE TABLE IF NOT EXISTS Habite(
	nom_reserve TEXT NOT NULL,
	nom_faune TEXT NOT NULL,
	nb_individus_habite INTEGER NOT NULL,
	CONSTRAINT pk_habite PRIMARY KEY (nom_reserve,nom_faune),
	CONSTRAINT fk_habite_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_habite_faune FOREIGN KEY (nom_faune) REFERENCES Faune (nom_faune),
	CONSTRAINT ck_habite_nb CHECK (nb_individus_habite >= 0)
);

CREATE TABLE IF NOT EXISTS PousseDans(
	nom_reserve TEXT NOT NULL,
	nom_flore TEXT NOT NULL,
	nb_individus_pousse_dans INTEGER NOT NULL,
	CONSTRAINT pk_pousse_dans PRIMARY KEY (nom_reserve,nom_flore),
	CONSTRAINT fk_pousse_dans_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_pousse_dans_flore FOREIGN KEY (nom_flore) REFERENCES Flore (nom_flore),
	CONSTRAINT ck_pousse_dans_nb CHECK (nb_individus_pousse_dans >= 0)
);

CREATE TABLE IF NOT EXISTS Traverse(
	nom_reserve TEXT NOT NULL,
	nom_parcours TEXT NOT NULL,
	CONSTRAINT pk_traverse PRIMARY KEY (nom_reserve,nom_parcours),
	CONSTRAINT fk_traverse_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_traverse_parcours FOREIGN KEY (nom_parcours) REFERENCES Parcours (nom_parcours)
); 

CREATE VIEW IF NOT EXISTS Reserves(nom_reserve,code_reserve,superficie_reserve,date_creation_reserve,numero_departement_reserve,nb_animaux_proteges_reserve) AS
WITH nb_individus AS (
	SELECT nom_reserve,	SUM(nb_individus_habite) AS nb_animaux_proteges_reserve
	FROM Reserves_base JOIN Habite USING (nom_reserve) 
					   JOIN Faune USING (nom_faune)
	WHERE est_protege_faune = 'oui'
	GROUP BY nom_reserve
	),
	nb_individus_tot AS(
	SELECT nom_reserve, nb_animaux_proteges_reserve
	FROM nb_individus
	UNION 
	SELECT nom_reserve, 0
	FROM Reserves_base
	WHERE nom_reserve NOT IN (SELECT nom_reserve
							  FROM nb_individus))
SELECT nom_reserve,
	   code_reserve,
	   superficie_reserve,
	   date_creation_reserve,
	   numero_departement_reserve, 
	   nb_animaux_proteges_reserve
FROM nb_individus_tot JOIN Reserves_base USING (nom_reserve);