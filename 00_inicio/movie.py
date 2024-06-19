
from review import Review
import mysql.connector  # Importa el conector MySQL para conectar con la base de datos


# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': "root",  
    'password': "1234",  
    'host': "localhost",  
    'database': "cac-movies2",  
    'port': 3306  # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
}

class Movie:
    # Constructor de la clase Movie
    def __init__(self, id_movie=None, title=None, adult=False, release_year=None, poster_url=None, reviews=None):
        self.id_movie = id_movie  # ID de la película, se asigna automáticamente para nuevas películas
        self.title = title  # Título de la película
        self.adult = adult  # Indicador de si la película es para adultos
        self.release_year = release_year  # Año de lanzamiento de la película
        self.poster_url = poster_url  # URL del póster de la película
        self.reviews = reviews
        

    # Método para guardar o actualizar una película en la base de datos
    def save(self):
        # db = get_db()  # Obtener la conexión a la base de datos
        db = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = db.cursor()
        if self.id_movie:
            # Si la película ya tiene un ID, se actualiza su registro en la base de datos
            cursor.execute("""
                UPDATE movies SET title = %s, adult = %s, release_year = %s, poster_url = %s
                WHERE id_movie = %s
            """, (self.title, self.adult, self.release_year, self.poster_url, self.id_movie))
        else:
            # Si la película no tiene un ID, se inserta un nuevo registro en la base de datos
            cursor.execute("""
                INSERT INTO movies (title, adult, release_year, poster_url) VALUES (%s, %s, %s, %s)
            """, (self.title, self.adult, self.release_year, self.poster_url))
            self.id_movie = cursor.lastrowid  # Obtener el ID asignado por la base de datos
        db.commit()  # Confirmar la transacción
        cursor.close()
        db.close()

    # Método estático para obtener todas las películas con sus reseñas de la base de datos
    @staticmethod
    def get_all():
        """
        Retorna un listado de OBJETOS Movie, cada uno con sus reseñas.
        """
        db = mysql.connector.connect(**DATABASE_CONFIG)

        cursor = db.cursor()
        query = """
            SELECT 
                m.id_movie, m.title, m.adult, m.release_year, m.poster_url,
                r.id_review, r.reviewer_name, r.comment, r.rating
            FROM 
                movies m
            LEFT JOIN 
                reviews r ON m.id_movie = r.id_movie
        """
        print(query)
        return []
        cursor.execute(query)  # Ejecutar la consulta para obtener todas las películas con sus reseñas
        rows = cursor.fetchall()  # Obtener todos los resultados
        
        movies_dict = {}
        
        for row in rows:
            id_movie = row[0]
            if id_movie not in movies_dict:
                movies_dict[id_movie] = Movie(
                    id_movie=row[0], title=row[1], adult=row[2], release_year=row[3], poster_url=row[4], reviews=[]
                )
            if row[5] is not None:
                review = Review(
                    id_review=row[5], id_movie=row[0], reviewer_name=row[6], comment=row[7], rating=row[8]
                )
                movies_dict[id_movie].reviews.append(review)

        cursor.close()
        db.close()
        return list(movies_dict.values())  # Devolver la lista de películas con sus reseñas
    '''
    @staticmethod
    def get_by_id(movie_id):
        db = get_db()
        cursor = db.cursor()

        # Ejecutar la consulta con JOIN para obtener la película y sus reseñas
        cursor.execute("""
            SELECT 
                m.id_movie, m.title, m.poster_url, m.release_year, m.adult,
                r.id_review, r.reviewer_name, r.comment, r.rating
            FROM 
                movies m
            LEFT JOIN 
                reviews r ON m.id_movie = r.id_movie
            WHERE 
                m.id_movie = %s
        """, (movie_id,))
        
        rows = cursor.fetchall()
        cursor.close()

        if rows:
            # Utilizamos un diccionario para mapear las películas por su ID para evitar duplicados
            movie_map = {}
            for row in rows:
                if row[0] not in movie_map:
                    # Si la película aún no está en el mapa, la añadimos con sus datos básicos
                    movie_map[row[0]] = Movie(id_movie=row[0], title=row[1], poster_url=row[2], release_year=row[3], adult=row[4], reviews=[])

                # Añadir la reseña si existe (puede ser None si no hay reseñas asociadas)
                if row[5] is not None:
                    review = Review(id_review=row[5], id_movie=row[0], reviewer_name=row[6], comment=row[7], rating=row[8])
                    movie_map[row[0]].reviews.append(review)

            # Devolver la película encontrada por su ID
            return movie_map[movie_id]

        return None  # Si no se encontró la película, devolver None

    # Método para eliminar una película de la base de datos
    def delete(self):
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("DELETE FROM movies WHERE id_movie = %s", (self.id_movie,))  # Ejecutar la consulta para eliminar la película
        db.commit()  # Confirmar la transacción
        cursor.close()

    # Método para serializar un objeto Movie a un diccionario
    def serialize(self):
        return {
            'id_movie': self.id_movie,  # ID de la película
            'title': self.title,  # Título de la película
            'adult': self.adult,  # Indicador de si la película es para adultos
            'release_year': self.release_year,  # Año de lanzamiento de la película
            'poster_url': self.poster_url,  # URL del póster de la película
            'reviews': [review.serialize() for review in self.reviews]  # Lista de reseñas serializadas
        }
    '''

    def __str__(self):
        return f"PELI: {self.id_movie} - {self.title} - {self.release_year}"

