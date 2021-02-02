CREATE DATABASE IF NOT EXISTS gabrielh_abm;
use gabrielh_abm;

CREATE TABLE usuarios(
    id           int(25) auto_increment not null PRIMARY KEY,
    nombre       varchar(50),
    apellido     varchar(100),
    email        varchar(255) not null UNIQUE,
    password     varchar(255) not null,
    fecha        date not null
)