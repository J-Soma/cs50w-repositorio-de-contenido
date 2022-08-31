SELECT * FROM vuelos;
SELECT origen, destino FROM vuelos;
SELECT * FROM vuelos WHERE id = 3;
SELECT * FROM vuelos WHERE origen = 'New York';
SELECT * FROM vuelos WHERE duracion > 500;
SELECT * FROM vuelos WHERE destino = 'Paris' AND duracion > 500;
SELECT * FROM vuelos WHERE destino = 'Paris' OR duracion > 500;
SELECT COUNT(*) FROM vuelos;
SELECT AVG(duracion) FROM vuelos;
