-- Selectionner la liste des postes de travail ayant eu un incident impliquant le vehicule 2
-- Retourne poste_id et poste_desc (Pas de Doublons)
SELECT "poste"."poste_id", "poste"."poste_desc"
FROM "incident"
LEFT JOIN "ordre" ON "incident"."ordre" = "ordre"."ordre_id"
LEFT JOIN "poste" ON "ordre"."poste" = "poste"."poste_id"
WHERE "ordre"."vehicule" = ?
GROUP BY "poste"."poste_desc";