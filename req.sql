BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "vehicule" (
	"vehicule_id"	INTEGER NOT NULL,
	"vehicule_desc"	TEXT NOT NULL,
	PRIMARY KEY("vehicule_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "poste" (
	"poste_id"	INTEGER NOT NULL,
	"poste_desc"	TEXT NOT NULL,
	PRIMARY KEY("poste_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ordre" (
	"ordre_id"	INTEGER NOT NULL,
	"ordre_desc"	TEXT NOT NULL,
	"poste"	INTEGER NOT NULL,
	"vehicule"	INTEGER NOT NULL,
	PRIMARY KEY("ordre_id" AUTOINCREMENT),
	FOREIGN KEY("vehicule") REFERENCES "vehicule"("vehicule_id"),
	FOREIGN KEY("poste") REFERENCES "poste"("poste_id")
);
CREATE TABLE IF NOT EXISTS "incident" (
	"incident_id"	INTEGER NOT NULL,
	"incident_desc"	TEXT NOT NULL,
	"ordre"	INTEGER NOT NULL,
	"etat"	TEXT NOT NULL,
	PRIMARY KEY("incident_id" AUTOINCREMENT),
	FOREIGN KEY("ordre") REFERENCES "ordre"("ordre_id")
);
INSERT INTO "vehicule" ("vehicule_id","vehicule_desc") VALUES (0,'vehicule4

');
INSERT INTO "vehicule" ("vehicule_id","vehicule_desc") VALUES (1,'vehicule1');
INSERT INTO "vehicule" ("vehicule_id","vehicule_desc") VALUES (2,'vehicule2');
INSERT INTO "vehicule" ("vehicule_id","vehicule_desc") VALUES (3,'vehicule3');
INSERT INTO "poste" ("poste_id","poste_desc") VALUES (0,'');
INSERT INTO "poste" ("poste_id","poste_desc") VALUES (1,'poste1');
INSERT INTO "poste" ("poste_id","poste_desc") VALUES (2,'poste2');
INSERT INTO "poste" ("poste_id","poste_desc") VALUES (3,'poste3');
INSERT INTO "ordre" ("ordre_id","ordre_desc","poste","vehicule") VALUES (1,'ordre1_poste1_vehicule1',1,1);
INSERT INTO "ordre" ("ordre_id","ordre_desc","poste","vehicule") VALUES (2,'ordre2_poste1_vehicule2',1,2);
INSERT INTO "ordre" ("ordre_id","ordre_desc","poste","vehicule") VALUES (3,'ordre3_poste2_vehicule1',2,1);
INSERT INTO "ordre" ("ordre_id","ordre_desc","poste","vehicule") VALUES (4,'ordre4_poste3_vehicule2',3,2);
INSERT INTO "ordre" ("ordre_id","ordre_desc","poste","vehicule") VALUES (5,'ordre5_poste2_vehicule2',2,2);
INSERT INTO "incident" ("incident_id","incident_desc","ordre","etat") VALUES (1,'incident1_ordre1',1,'OPEN');
INSERT INTO "incident" ("incident_id","incident_desc","ordre","etat") VALUES (2,'incident2_ordre2',2,'OPEN');
INSERT INTO "incident" ("incident_id","incident_desc","ordre","etat") VALUES (3,'incident3_ordre2',2,'OPEN');
INSERT INTO "incident" ("incident_id","incident_desc","ordre","etat") VALUES (4,'incident4_ordre4',4,'OPEN');
INSERT INTO "incident" ("incident_id","incident_desc","ordre","etat") VALUES (5,'incident5_ordre4',4,'OPEN');
COMMIT;



-- Selectionner un vehicule
-- Retourne vehicule_desc
SELECT "vehicule_desc"
FROM "vehicule"
WHERE "vehicule_id" = 0;


-- Selectionner tous les incidents avec un vehicule 
-- Retourne incident_id, incident_desc et etat
SELECT "incident_id", "incident_desc", "etat"
FROM "incident"
LEFT JOIN "ordre" ON "incident"."ordre" = "ordre"."ordre_id"
WHERE "vehicule" = 2;


-- Selectionner la liste des postes de travail ayant eu un incident impliquant le vehicule 2
-- Retourne poste_id et poste_desc (Pas de Doublons)
SELECT "poste"."poste_id", "poste"."poste_desc"
FROM "incident"
LEFT JOIN "ordre" ON "incident"."ordre" = "ordre"."ordre_id"
LEFT JOIN "poste" ON "ordre"."poste" = "poste"."poste_id"
WHERE "ordre"."vehicule" = 2
GROUP BY "poste"."poste_desc";


-- Selelectionne l'identifiant d'un incident et l'ordre de travail lié
-- Retourne incident_id et ordre
SELECT "incident"."incident_id", "ordre"."ordre_id"
FROM "incident"
LEFT JOIN "ordre" ON "ordre"."ordre_id" = "incident"."ordre"
WHERE "ordre"."vehicule" = 2;