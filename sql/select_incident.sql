-- Selelectionne l'identifiant d'un incident et l'ordre de travail lié
-- Retourne incident_id et ordre
SELECT "incident"."incident_id", "ordre"."ordre_id"
FROM "incident"
LEFT JOIN "ordre" ON "ordre"."ordre_id" = "incident"."ordre"
WHERE "ordre"."vehicule" = ?;