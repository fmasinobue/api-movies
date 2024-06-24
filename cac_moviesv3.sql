CREATE DATABASE  IF NOT EXISTS `cac-movies3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cac-movies3`;

--
-- Table structure for table `genres`
--
DROP TABLE IF EXISTS `reviews`;
DROP TABLE IF EXISTS `movies_genres`;
DROP TABLE IF EXISTS `genres`;

CREATE TABLE `genres` (
  `id_genre` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_genre`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `movies`;

CREATE TABLE `movies` (
  `id_movie` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `poster_url` varchar(200),
  `release_year` int DEFAULT '2024',
  `adult` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_movie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `reviews` (
  `id_review` INT NOT NULL AUTO_INCREMENT,
  `id_movie` INT NULL,
  `reviewer_name` VARCHAR(100) NULL,
  `comment` TEXT NULL,
  `rating` DECIMAL(4,2) NULL,
  PRIMARY KEY (`id_review`)
);

ALTER TABLE `reviews` 
ADD INDEX `fk_movie_idx` (`id_movie` ASC) VISIBLE;
ALTER TABLE `reviews` 
ADD CONSTRAINT `fk_movie`
  FOREIGN KEY (`id_movie`)
  REFERENCES `movies` (`id_movie`)
  ON DELETE SET NULL
  ON UPDATE CASCADE;



CREATE TABLE `movies_genres` (
  `id_movie_genre` int NOT NULL AUTO_INCREMENT,
  `id_movie` int DEFAULT NULL,
  `id_genre` int DEFAULT NULL,
  PRIMARY KEY (`id_movie_genre`),
  KEY `FK1_movie_idx` (`id_movie`),
  KEY `FK2_idx` (`id_genre`),
  CONSTRAINT `FK1_movie` FOREIGN KEY (`id_movie`) REFERENCES `movies` (`id_movie`) ON DELETE SET NULL,
  CONSTRAINT `FK2` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id_genre`) ON DELETE SET NULL
);


/* INSERTS */
-- generos
INSERT INTO genres (name) VALUES ('Acción');
INSERT INTO genres (name) VALUES ('Comedia');
INSERT INTO genres (name) VALUES ('Drama');
INSERT INTO genres (name) VALUES ('Ciencia Ficción');
INSERT INTO genres (name) VALUES ('Romance');
INSERT INTO genres (name) VALUES ('Terror');
INSERT INTO genres (name) VALUES ('Aventura');
INSERT INTO genres (name) VALUES ('Animación');
INSERT INTO genres (name) VALUES ('Fantasía');
INSERT INTO genres (name) VALUES ('Documental');
INSERT INTO genres (name) VALUES ('Musical');
INSERT INTO genres (name) VALUES ('Crimen');
INSERT INTO genres (name) VALUES ('Suspenso');



-- INSERT INTO movies_genres (id_movie, id_genre) VALUES (1, 1), (1, 7);

-- INSERT INTO movies_genres (id_movie, id_genre) VALUES (2, 3), (2, 8);