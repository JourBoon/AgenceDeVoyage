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

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Nantes-Paris', 'Vol à Paris sans escale ', 180, 280, 70);

INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (1, 'Louvres', 17, 3, 'None', 'Visite guidée du musée du Louvres');

/*
INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('None', 'None', 0, 0, 0);

INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES ('None', 0, 0, 31-12-2023, 'None');

INSERT INTO VOYAGE (date_depart, date_retour, places, cost) VALUES (30-12-2023, 31-12-2023, 0, 0);

INSERT INTO RESERVATION (cost) VALUES (0);

INSERT INTO PAIEMENT (cost, paye_date) VALUES (0, 31-12-2023);
*/
