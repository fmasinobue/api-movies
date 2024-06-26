import os 
# pip install mysql-connector-python
import mysql.connector  # Importa el conector MySQL para conectar con la base de datos
from flask import g  # Importa g de Flask para almacenar datos durante la petición
# pip install python-dotenv
from dotenv import load_dotenv  

d = os.path.dirname(__file__)
os.chdir(d)

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),  
    'password': os.getenv('DB_PASSWORD'),  
    'host': os.getenv('DB_HOST'),  
    'database': os.getenv('DB_NAME'),  
    'port': os.getenv('DB_PORT', 3306)  # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
}


# Función para obtener la conexión de la base de datos
def get_db():
    # Si no hay una conexión a la base de datos en g, la creamos
    # g, que es un objeto de Flask que se usa para almacenar datos durante la vida útil de una solicitud.
    if 'db' not in g:
        print("···· Abriendo conexion a DB ····")
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    # Retorna la conexión a la base de datos
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Intenta obtener la conexión de la base de datos desde g
    db = g.pop('db', None)
    # Si hay una conexión, la cerramos
    if db is not None:
        print("···· Cerrando conexion a DB ····")
        db.close()
# Función para inicializar la base de datos
def init_db():
    db = get_db()
    cursor = db.cursor()

    # Crear tablas si no existen con todas las claves e índices incluidos
    sql_commands = [
        """CREATE TABLE IF NOT EXISTS `genres` (
            `id_genre` int NOT NULL AUTO_INCREMENT,
            `name` varchar(45) NOT NULL,
            PRIMARY KEY (`id_genre`),
            UNIQUE KEY `name_UNIQUE` (`name`)
        ) ;""",
        
        """CREATE TABLE IF NOT EXISTS `movies` (
            `id_movie` int NOT NULL AUTO_INCREMENT,
            `title` varchar(100) NOT NULL,
            `poster_url` varchar(200),
            `release_year` int DEFAULT '2024',
            `adult` tinyint(1) DEFAULT '0',
            PRIMARY KEY (`id_movie`)
        ) ;""",
        
        """CREATE TABLE IF NOT EXISTS `reviews` (
            `id_review` INT NOT NULL AUTO_INCREMENT,
            `id_movie` INT NULL,
            `reviewer_name` VARCHAR(100) NULL,
            `comment` TEXT NULL,
            `rating` DECIMAL(4,2) NULL,
            PRIMARY KEY (`id_review`),
            INDEX `fk_movie_idx` (`id_movie` ASC),
            CONSTRAINT `fk_movie`
                FOREIGN KEY (`id_movie`)
                REFERENCES `movies` (`id_movie`)
                ON DELETE SET NULL
                ON UPDATE CASCADE
        ) ;""",
        
        """CREATE TABLE IF NOT EXISTS `movies_genres` (
            `id_movie_genre` int NOT NULL AUTO_INCREMENT,
            `id_movie` int DEFAULT NULL,
            `id_genre` int DEFAULT NULL,
            PRIMARY KEY (`id_movie_genre`),
            KEY `FK1_movie_idx` (`id_movie`),
            KEY `FK2_idx` (`id_genre`),
            CONSTRAINT `FK1_movie` FOREIGN KEY (`id_movie`) REFERENCES `movies` (`id_movie`) ON DELETE SET NULL,
            CONSTRAINT `FK2` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id_genre`) ON DELETE SET NULL
        ) ;"""
    ]

    for command in sql_commands:
        cursor.execute(command)

    db.commit()

    # Inserciones de géneros si no existen
    cursor.execute("""
        INSERT INTO genres (name) VALUES
            ('Acción'), ('Comedia'), ('Drama'), ('Ciencia Ficción'), ('Romance'),
            ('Terror'), ('Aventura'), ('Animación'), ('Fantasía'), ('Documental'),
            ('Musical'), ('Crimen'), ('Suspenso')
        ON DUPLICATE KEY UPDATE name=name;
    """)

    db.commit()
    cursor.close()

# Función para inicializar la aplicación con el cierre automático de la conexión a la base de datos
def init_app(app):
    # Registrar la función close_db para que se llame automáticamente
    # cuando el contexto de la aplicación se destruye
    app.teardown_appcontext(close_db)
