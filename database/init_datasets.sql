CREATE TABLE CLIENT (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT,
    nom TEXT,
    age INTEGER,
    adresse TEXT,
    mail TEXT,
    tel_num INT
);

CREATE TABLE DESTINATION (
    id_dest INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_dest TEXT,
    desc_dest TEXT,
    cost INT,
    places INT,
    duree INT,
);

CREATE TABLE ACTIVITE (
    id_act INTEGER PRIMARY KEY AUTOINCREMENT,
    id_dest INTEGER FOREIGN KEY id_dest REFERENCES DESTINATION(id_dest),
    nom_act TEXT,
    sup_cost INT,
    duree_act INT,
    date_act DATE,
    desc_act TEXT
);

CREATE TABLE VOYAGE (
    id_voy INTEGER PRIMARY KEY AUTOINCREMENT,
    id_dest INTEGER FOREIGN KEY id_dest REFERENCES DESTINATION(id_dest),
    date_depart DATE,
    date_retour DATE,
    places INT,
    cost INT
);

CREATE TABLE RESERVATION (
    id_res INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cient INTEGER FOREIGN KEY id_client REFERENCES CLIENT(id_client),
    id_dest INTEGER FOREIGN KEY id_dest REFERENCES DESTINATION(id_dest),
    cost INT
);

CREATE TABLE PAIEMENT (
    id_paim INTEGER PRIMARY KEY AUTOINCREMENT,
    id_res INTEGER FOREIGN KEY id_res REFERENCES RESERVATION(id_res),
    cost INT,
    paye_date DATE
);

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('John Doe', "sdfgkishg", 25, 3, 5);