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
    duree INT
);

CREATE TABLE ACTIVITE (
    id_act INTEGER PRIMARY KEY AUTOINCREMENT,
    id_dest INTEGER,
    nom_act TEXT,
    sup_cost INT,
    duree_act INT,
    date_act DATE,
    desc_act TEXT,
    FOREIGN KEY (id_dest) REFERENCES DESTINATION(id_dest)
);

CREATE TABLE VOYAGE (
    id_voy INTEGER PRIMARY KEY AUTOINCREMENT,
    id_dest INTEGER,
    date_depart DATE,
    date_retour DATE,
    places INT,
    cost INT,
    FOREIGN KEY (id_dest) REFERENCES DESTINATION(id_dest)
);

CREATE TABLE RESERVATION (
    id_res INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER,
    id_dest INTEGER,
    cost INT,
    FOREIGN KEY (id_client) REFERENCES CLIENT(id_client),
    FOREIGN KEY (id_dest) REFERENCES DESTINATION(id_dest)
);

CREATE TABLE PAIEMENT (
    id_paim INTEGER PRIMARY KEY AUTOINCREMENT,
    id_res INTEGER,
    cost INT,
    paye_date DATE,
    FOREIGN KEY (id_res) REFERENCES RESERVATION(id_res)
);

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Nantes-Paris', 'Vol à Paris sans escale ', 180, 280, 70);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (1, 'Louvres', 17, 3, 'None', 'Visite guidée du musée du Louvres');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Paris-Barcelone', 'Vol direct vers Barcelone', 220, 320, 90);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (2, 'Sagrada Familia', 20, 4, '2023-12-30', 'Visite guidée de la Sagrada Familia');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('New York-Miami', 'Vol de New York à Miami', 300, 250, 120);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (3, 'South Beach', 25, 5, '2023-12-28', 'Détente sur la plage de South Beach');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Rio de Janeiro-Buenos Aires', 'Vol de Rio de Janeiro à Buenos Aires', 280, 220, 100);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (4, 'Tango Show', 25, 3, '2023-08-10', 'Spectacle de tango');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Bangkok-Phuket', 'Vol de Bangkok à Phuket', 180, 150, 70);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (5, 'Plage de Patong', 20, 4, '2023-07-05', 'Relaxation sur la plage de Patong');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Berlin-Amsterdam', 'Vol de Berlin à Amsterdam', 210, 180, 80);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (6, 'Musée Van Gogh', 18, 3, '2023-06-15', 'Visite du musée Van Gogh');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Copenhague-Stockholm', 'Vol de Copenhague à Stockholm', 190, 160, 75);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (7, 'Vasa Museum', 16, 3, '2023-05-20', 'Exploration du musée Vasa');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Prague-Vienne', 'Vol de Prague à Vienne', 220, 200, 85);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (8, 'Château de Schönbrunn', 22, 4, '2023-04-10', 'Visite du château de Schönbrunn');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Toronto-Montréal', 'Vol de Toronto à Montréal', 150, 180, 60);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (9, 'Vieux-Montréal', 15, 2, '2023-03-05', 'Exploration du Vieux-Montréal');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Hong Kong-Shanghai', 'Vol de Hong Kong à Shanghai', 260, 220, 95);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (10, 'Tour de la Perle Orientale', 25, 3, '2023-02-15', 'Visite de la Tour de la Perle Orientale');

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('Istanbul-Athènes', 'Vol de Istanbul à Athènes', 230, 190, 85);
INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES (11, 'Parthénon', 20, 4, '2023-01-25', 'Visite du Parthénon');


/*
Patern :

INSERT INTO DESTINATION (nom_dest, desc_dest, cost, places, duree) VALUES ('None', 'None', 0, 0, 0);

INSERT INTO ACTIVITE (id_dest, nom_act, sup_cost, duree_act, date_act, desc_act) VALUES ('None', 0, 0, 31-12-2023, 'None');

INSERT INTO VOYAGE (date_depart, date_retour, places, cost) VALUES (30-12-2023, 31-12-2023, 0, 0);

INSERT INTO RESERVATION (cost) VALUES (0);

INSERT INTO PAIEMENT (cost, paye_date) VALUES (0, 31-12-2023);
*/
