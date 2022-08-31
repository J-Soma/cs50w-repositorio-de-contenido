CREATE TABLE vuelos (
    id SERIAL PRIMARY KEY,
    origen VARCHAR NOT NULL,
    destino VARCHAR NOT NULL,
    duracion INTEGER NOT NULL
);
