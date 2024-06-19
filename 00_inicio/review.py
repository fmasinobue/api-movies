
import mysql.connector  # Importa el conector MySQL para conectar con la base de datos

# Configuración de la base de datos usando variables de entorno
DATABASE_CONFIG = {
    'user': "root",  
    'password': "1234",  
    'host': "localhost",  
    'database': "cac-movies2",  
    'port': 3306  # Puerto del servidor de la base de datos, por defecto es 3306 si no se especifica
}

class Review:
    # Constructor de la clase Review
    def __init__(self, id_review=None, id_movie=None, reviewer_name=None, comment=None, rating=None):
        self.id_review = id_review  # ID de la reseña, se asigna automáticamente para nuevas reseñas
        self.id_movie = id_movie  # ID de la película asociada
        self.reviewer_name = reviewer_name  # Nombre del revisor
        self.comment = comment  # Comentario de la reseña
        self.rating = rating  # Calificación de la reseña

    # Método para guardar o actualizar una reseña en la base de datos
    def save(self):
        db = mysql.connector.connect(**DATABASE_CONFIG)

        cursor = db.cursor()
        if self.id_review:
            # Si la reseña ya tiene un ID, se actualiza su registro en la base de datos
            cursor.execute("""
                UPDATE reviews SET id_movie = %s, reviewer_name = %s, comment = %s, rating = %s
                WHERE id_review = %s
            """, (self.id_movie, self.reviewer_name, self.comment, self.rating, self.id_review))
        else:
            # Si la reseña no tiene un ID, se inserta un nuevo registro en la base de datos
            cursor.execute("""
                INSERT INTO reviews (id_movie, reviewer_name, comment, rating) VALUES (%s, %s, %s, %s)
            """, (self.id_movie, self.reviewer_name, self.comment, self.rating))
            self.id_review = cursor.lastrowid  # Obtener el ID asignado por la base de datos
        db.commit()  # Confirmar la transacción
        cursor.close()
        db.close()
    '''
    # Método estático para obtener todas las reseñas de la base de datos
    @staticmethod
    def get_all():
        """
        Retorna un listado de OBJETOS, cada uno sera una reseña
        """
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reviews")  # Ejecutar la consulta para obtener todas las reseñas
        rows = cursor.fetchall()  # Obtener todos los resultados
        # Crear una lista de objetos Review a partir de los resultados
        reviews = [Review(id_review=row[0], id_movie=row[1], reviewer_name=row[2], comment=row[3], rating=row[4]) for row in rows]
        cursor.close()
        close_db(db)
        return reviews  # Devolver la lista de reseñas

    # Método estático para obtener una reseña por su ID
    @staticmethod
    def get_by_id(review_id):
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("SELECT * FROM reviews WHERE id_review = %s", (review_id,))  # Ejecutar la consulta para obtener la reseña por ID
        row = cursor.fetchone()  # Obtener el resultado
        cursor.close()
        close_db(db)
        if row:
            # Si se encontró la reseña, devolver un objeto Review con sus datos
            return Review(id_review=row[0], id_movie=row[1], reviewer_name=row[2], comment=row[3], rating=row[4])
        return None  # Si no se encontró la reseña, devolver None

    # Método para eliminar una reseña de la base de datos
    def delete(self):
        db = get_db()  # Obtener la conexión a la base de datos
        cursor = db.cursor()
        cursor.execute("DELETE FROM reviews WHERE id_review = %s", (self.id_review,))  # Ejecutar la consulta para eliminar la reseña
        db.commit()  # Confirmar la transacción
        cursor.close()
        close_db(db)


    # Método para serializar un objeto Review a un diccionario
    def serialize(self):
        return {
            'id_review': self.id_review,  # ID de la reseña
            'id_movie': self.id_movie,  # ID de la película asociada
            'reviewer_name': self.reviewer_name,  # Nombre del revisor
            'comment': self.comment,  # Comentario de la reseña
            'rating': self.rating  # Calificación de la reseña
        }
    '''
    # Método para representar la instancia de Review como una cadena
    def __str__(self):
        return f"RESEÑA: {self.id_review} - {self.reviewer_name} - {self.rating}"

