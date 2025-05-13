drop database evidence;

create database evidence;
use evidence;

create table vydavatelstvi (idv int NOT NULL PRIMARY KEY, jmeno varchar(255) NOT NULL, zeme varchar(255) NOT NULL);
insert into vydavatelstvi values
(1, "Rockstar games", "Cesko"),
(2, "Epic games", "Nemecko"),
(3, "bethesda", "USA"),
(4, "Battlenet", "Slovensko"),
(5, "Riot", "Svedsko");

create table deskove_hry (idd int NOT NULL AUTO_INCREMENT PRIMARY KEY, nazev varchar(255) NOT NULL, rok_vydani int NOT NULL, idv int NOT NULL, FOREIGN KEY (idv) REFERENCES vydavatelstvi(idv));
insert into deskove_hry values
(0, "DOOM ETERNAL", 2020, 3),
(0, "DOOM 2016", 2016, 3),
(0, "FORTNITE", 2017, 2),
(0, "GTA V", 2013, 1),
(0, "GTA VI", 2026, 1),
(0,"Valochcant", 2018, 5),
(0, "Warzone", 2020, 4);


SELECT jmeno, zeme, nazev, rok_vydani FROM vydavatelstvi INNER JOIN deskove_hry ON vydavatelstvi.idv = deskove_hry.idv;
