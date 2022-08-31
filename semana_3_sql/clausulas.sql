SELECT * FROM vuelos LIMIT 2;
SELECT * FROM vuelos ORDER BY duracion ASC;
SELECT * FROM vuelos ORDER BY duracion DESC;
SELECT origen, COUNT(*) FROM vuelos GROUP BY origen;
SELECT origen, COUNT(*) FROM vuelos GROUP BY origen HAVING COUNT(*) > 1;
