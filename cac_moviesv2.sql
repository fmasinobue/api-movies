CREATE DATABASE  IF NOT EXISTS `cac-movies2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cac-movies2`;

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
  CONSTRAINT `FK1_movie` FOREIGN KEY (`id_movie`) REFERENCES `movies` (`id_movie`),
  CONSTRAINT `FK2` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id_genre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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

-- peliculas
INSERT INTO movies (title, release_year, adult) VALUES ('El Señor de los Anillos: La Comunidad del Anillo', 2021, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Pulp Fiction', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Titanic', 1997, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Forrest Gump', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El Rey León', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El Padrino', 1972, 1);
INSERT INTO movies (title, release_year, adult) VALUES ('Interestelar', 2014, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Harry Potter y la piedra filosofal', 2001, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('La La Land', 2016, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('El club de la lucha', 1999, 0);

-- Películas adicionales
INSERT INTO movies (title, release_year, adult) VALUES ('Matrix', 1999, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Inception', 2010, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Avengers: Endgame', 2019, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Joker', 2019, 1);
INSERT INTO movies (title, release_year, adult) VALUES ('The Dark Knight', 2008, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Shutter Island', 2010, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('The Social Network', 2010, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Spider-Man: No Way Home', 2021, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Gladiator', 2000, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('The Shawshank Redemption', 1994, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('The Wolf of Wall Street', 2013, 1);
INSERT INTO movies (title, release_year, adult) VALUES ('Parasite', 2019, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('The Grand Budapest Hotel', 2014, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Mad Max: Fury Road', 2015, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Black Panther', 2018, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Toy Story 3', 2010, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Coco', 2017, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Whiplash', 2014, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('The Revenant', 2015, 0);
INSERT INTO movies (title, release_year, adult) VALUES ('Her', 2013, 0);

-- Asociación de "El Señor de los Anillos: La Comunidad del Anillo" con los géneros "Acción" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (1, 1), (1, 7);

-- Asociación de "Pulp Fiction" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (2, 3), (2, 12);

-- Asociación de "Titanic" con los géneros "Romance" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (3, 5), (3, 3);

-- Asociación de "Forrest Gump" con el género "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (4, 3);

-- Asociación de "El Rey León" con los géneros "Animación" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (5, 8), (5, 7);

-- Asociación de "El Padrino" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (6, 3), (6, 12);

-- Asociación de "Interestelar" con el género "Ciencia Ficción"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (7, 4);

-- Asociación de "Harry Potter y la piedra filosofal" con los géneros "Fantasía" y "Aventura"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (8, 9), (8, 7);

-- Asociación de "La La Land" con los géneros "Musical" y "Drama"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (9, 11), (9, 3);

-- Asociación de "El club de la lucha" con los géneros "Drama" y "Crimen"
INSERT INTO movies_genres (id_movie, id_genre) VALUES (10, 3), (10, 12);

-- Asociaciones de las películas adicionales
INSERT INTO movies_genres (id_movie, id_genre) VALUES (11, 4), (11, 1); -- Matrix
INSERT INTO movies_genres (id_movie, id_genre) VALUES (12, 4), (12, 3); -- Inception
INSERT INTO movies_genres (id_movie, id_genre) VALUES (13, 1), (13, 7); -- Avengers: Endgame
INSERT INTO movies_genres (id_movie, id_genre) VALUES (14, 3), (14, 12); -- Joker
INSERT INTO movies_genres (id_movie, id_genre) VALUES (15, 1), (15, 12); -- The Dark Knight
INSERT INTO movies_genres (id_movie, id_genre) VALUES (16, 3), (16, 13); -- Shutter Island
INSERT INTO movies_genres (id_movie, id_genre) VALUES (17, 3); -- The Social Network
INSERT INTO movies_genres (id_movie, id_genre) VALUES (18, 1), (18, 7); -- Spider-Man: No Way Home
INSERT INTO movies_genres (id_movie, id_genre) VALUES (19, 7), (19, 3); -- Gladiator
INSERT INTO movies_genres (id_movie, id_genre) VALUES (20, 3); -- The Shawshank Redemption
INSERT INTO movies_genres (id_movie, id_genre) VALUES (21, 3), (21, 12); -- The Wolf of Wall Street
INSERT INTO movies_genres (id_movie, id_genre) VALUES (22, 3), (22, 12); -- Parasite
INSERT INTO movies_genres (id_movie, id_genre) VALUES (23, 3), (23, 2); -- The Grand Budapest Hotel
INSERT INTO movies_genres (id_movie, id_genre) VALUES (24, 1), (24, 7); -- Mad Max: Fury Road
INSERT INTO movies_genres (id_movie, id_genre) VALUES (25, 1), (25, 7); -- Black Panther
INSERT INTO movies_genres (id_movie, id_genre) VALUES (26, 8); -- Toy Story 3
INSERT INTO movies_genres (id_movie, id_genre) VALUES (27, 8); -- Coco
INSERT INTO movies_genres (id_movie, id_genre) VALUES (28, 3); -- Whiplash
INSERT INTO movies_genres (id_movie, id_genre) VALUES (29, 1), (29, 7); -- The Revenant
INSERT INTO movies_genres (id_movie, id_genre) VALUES (30, 3), (30, 5); -- Her

-- Críticas para las películas
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (1, 'Enzo', 'safa....', 3.8); -- El Señor de los Anillos
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (2, 'Jane Smith', 'Amazing!', 4.8); -- Pulp Fiction
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (3, 'Alice Johnson', 'Loved it!', 4.7); -- Titanic
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (3, 'Bob Brown', 'Classic!', 4.9); -- Titanic
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (4, 'Charlie Davis', 'Incredible!', 4.6); -- Forrest Gump
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (4, 'David Evans', 'Timeless!', 4.8); -- Forrest Gump
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (4, 'Eva Green', 'Heartwarming!', 4.7); -- Forrest Gump
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (5, 'Frank Harris', 'Best animation ever!', 4.9); -- El Rey León
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (6, 'Grace King', 'Masterpiece!', 5.0); -- El Padrino
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (6, 'Hank Lee', 'Epic!', 4.9); -- El Padrino
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (6, 'Ivy Martinez', 'Brilliant!', 4.8); -- El Padrino
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (7, 'Jack Nelson', 'Mind-blowing!', 4.7); -- Interestelar
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (7, 'Kara O\'Brien', 'Out of this world!', 4.8); -- Interestelar
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (8, 'Liam Peters', 'Magical!', 4.6); -- Harry Potter
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (8, 'Mona Quinn', 'Enchanting!', 4.7); -- Harry Potter
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (8, 'Nina Roberts', 'Wonderful!', 4.8); -- Harry Potter
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (8, 'Oscar Scott', 'Fantastic!', 4.9); -- Harry Potter
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (9, 'Paul Turner', 'Lovely!', 4.6); -- La La Land
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (9, 'Quinn Underwood', 'Beautiful!', 4.7); -- La La Land
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (10, 'Rachel Vance', 'Thought-provoking!', 4.5); -- El club de la lucha
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (10, 'Steve Williams', 'Intense!', 4.6); -- El club de la lucha
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (10, 'Tom Xavier', 'Unforgettable!', 4.7); -- El club de la lucha
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (10, 'Uma Young', 'Brilliant!', 4.8); -- El club de la lucha
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (13, 'Victor Adams', 'Spectacular!', 4.8); -- Avengers: Endgame
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (13, 'Wendy Brooks', 'Fantastic!', 4.7); -- Avengers: Endgame
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (13, 'Xander Clark', 'Epic finale!', 4.9); -- Avengers: Endgame
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (14, 'Yvonne Davis', 'Dark and gripping!', 4.6); -- Joker
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (14, 'Zachary Evans', 'Haunting performance!', 4.8); -- Joker
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (17, 'Alex Brown', 'Brilliant screenplay!', 4.5); -- The Social Network
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (17, 'Brianna Clark', 'Engaging and insightful!', 4.7); -- The Social Network
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (19, 'Carla Diaz', 'Epic and thrilling!', 4.8); -- Gladiator
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (19, 'Daniel Edwards', 'Masterpiece!', 4.9); -- Gladiator
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (19, 'Erin Foster', 'Timeless!', 4.7); -- Gladiator
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (22, 'Faith Green', 'Incredible story!', 4.8); -- Parasite
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (22, 'Gavin Harris', 'Fantastic direction!', 4.9); -- Parasite
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (25, 'Holly James', 'A Marvel masterpiece!', 4.8); -- Black Panther
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (25, 'Isaac Kelly', 'Cultural phenomenon!', 4.9); -- Black Panther
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (28, 'Jake Lee', 'Intense and captivating!', 4.7); -- Whiplash
INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (28, 'Karen Martinez', 'Outstanding performances!', 4.8); -- Whiplash
