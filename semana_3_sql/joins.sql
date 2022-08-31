CREATE TABLE pasajeros (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    id_vuelo INTEGER REFERENCES vuelos
);

INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Alice', 1);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Bob', 1);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Charlie', 2);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Dave', 2);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Erin', 4);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Frank', 6);
INSERT INTO pasajeros (nombre, id_vuelo) VALUES ('Grace', 6);


SELECT origen, destino, nombre FROM vuelos INNER JOIN pasajeros ON pasajeros.id_vuelo = vuelos.id;
SELECT origen, destino, nombre FROM vuelos JOIN pasajeros ON pasajeros.id_vuelo = vuelos.id;
SELECT origen, destino, nombre FROM vuelos LEFT OUTER JOIN pasajeros ON pasajeros.id_vuelo = vuelos.id;
SELECT origen, destino, nombre FROM vuelos RIGHT OUTER JOIN pasajeros ON pasajeros.id_vuelo = vuelos.id;
