CREATE TABLE IF NOT EXISTS Reserves_base(
	nom_reserve TEXT NOT NULL,
	code_reserve TEXT NOT NULL,
	superficie_reserve REAL NOT NULL,
	date_creation_reserve DATE NOT NULL,
	numero_departement_reserve INTEGER NOT NULL,
	CONSTRAINT pk_reserve PRIMARY KEY (nom_reserve),
	CONSTRAINT uk_code UNIQUE (code_reserve),
	CONSTRAINT ck_superficie CHECK (superficie_reserve > 0),
	CONSTRAINT ck_numero_departement CHECK (numero_departement_reserve > 0 AND numero_departement_reserve < 97)
);
	
CREATE TABLE IF NOT EXISTS Faune(
	nom_faune TEXT NOT NULL,
	taille_moyenne_faune REAL NOT NULL,
	couleur_faune TEXT NOT NULL,
	regime_alimentaire_faune TEXT NOT NULL,
	est_protege_faune TEXT NOT NULL,
	CONSTRAINT pk_faune PRIMARY KEY (nom_faune),
	CONSTRAINT ck_taille CHECK (taille_moyenne_faune > 0),
	CONSTRAINT ck_regime CHECK (regime_alimentaire_faune = 'carnivore' OR regime_alimentaire_faune = 'omnivore' OR regime_alimentaire_faune = 'herbivore' OR regime_alimentaire_faune = 'insectivore'),
	CONSTRAINT ck_protege CHECK (est_protege_faune = 'oui' OR est_protege_faune = 'non')
);

CREATE TABLE IF NOT EXISTS Flore(
	nom_flore TEXT NOT NULL,
	famille_flore TEXT NOT NULL,
	type_flore TEXT NOT NULL,
	est_protege_flore TEXT NOT NULL,
	CONSTRAINT pk_flore PRIMARY KEY (nom_flore),
	CONSTRAINT ck_type CHECK (type_flore = 'arbre' OR type_flore = 'arbuste' OR type_flore = 'plante' OR type_flore = 'fleur' OR type_flore = 'champignon'),
	CONSTRAINT ck_protege CHECK (est_protege_flore = 'oui' OR est_protege_flore = 'non')
);
	
CREATE TABLE IF NOT EXISTS Parcours(
	nom_parcours TEXT NOT NULL,
	departement_depart_parcours INTEGER NOT NULL,
	departement_arrivee_parcours INTEGER NOT NULL,
	duree_parcours TIME NOT NULL,
	type_parcours TEXT NOT NULL,
	CONSTRAINT pk_parcours PRIMARY KEY (nom_parcours),
	CONSTRAINT ck_depart CHECK (departement_depart_parcours > 0 AND departement_depart_parcours < 97),
	CONSTRAINT ck_arrivee CHECK (departement_arrivee_parcours > 0 AND departement_arrivee_parcours < 97),	
	CONSTRAINT duree_parcours CHECK (duree_parcours > '00:00:00'),
	CONSTRAINT ck_type CHECK (type_parcours = 'chemin' OR type_parcours = 'route' OR type_parcours = 'GR' OR type_parcours = 'sentier')
);

CREATE TABLE IF NOT EXISTS GardesForestier(
	matricule_garde_forestier INTEGER NOT NULL,
	reserve_de_travail_garde_forestier TEXT NOT NULL,
	nom_garde_forestier TEXT NOT NULL,
	prenom_garde_forestier TEXT NOT NULL,
	date_de_naissance_garde_forestier DATE NOT NULL,
	CONSTRAINT pk_code PRIMARY KEY (matricule_garde_forestier),
	CONSTRAINT fk_reserve FOREIGN KEY (reserve_de_travail_garde_forestier) REFERENCES Reserves_base (nom_reserve)
);

CREATE TABLE IF NOT EXISTS Habite(
	nom_reserve TEXT NOT NULL,
	nom_faune TEXT NOT NULL,
	nb_individus_habite INTEGER NOT NULL,
	CONSTRAINT pk_habite PRIMARY KEY (nom_reserve,nom_faune),
	CONSTRAINT fk_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_faune FOREIGN KEY (nom_faune) REFERENCES Faune (nom_faune)
);

CREATE TABLE IF NOT EXISTS PousseDans(
	nom_reserve TEXT NOT NULL,
	nom_flore TEXT NOT NULL,
	nb_individus_pousse_dans INTEGER NOT NULL,
	CONSTRAINT pk_pousse_dans PRIMARY KEY (nom_reserve,nom_flore),
	CONSTRAINT fk_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_flore FOREIGN KEY (nom_flore) REFERENCES Flore (nom_flore)
);

CREATE TABLE IF NOT EXISTS Traverse(
	nom_reserve TEXT NOT NULL,
	nom_parcours TEXT NOT NULL,
	CONSTRAINT pk_traverse PRIMARY KEY (nom_reserve,nom_parcours),
	CONSTRAINT fk_reserve FOREIGN KEY (nom_reserve) REFERENCES Reserves_base (nom_reserve),
	CONSTRAINT fk_parcours FOREIGN KEY (nom_parcours) REFERENCES Parcours (nom_parcours)
); 