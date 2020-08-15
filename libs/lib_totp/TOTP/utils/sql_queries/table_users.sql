CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(64) UNIQUE,
    name VARCHAR(48),
    surname VARCHAR(48),
    city VARCHAR(48),
    dateBirth VARCHAR(16),
    income INTEGER,
    secretKey VARCHAR(16)
);