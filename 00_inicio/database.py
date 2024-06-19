import mysql.connector  # Importa el conector MySQL para conectar con la base de datos


DATABASE_CONFIG = {
    'user': "root",  
    'password': "1234",  
    'host': "localhost",  
    'database': "cac-movies2",  
    'port': 3306
}


# Función para obtener la conexión de la base de datos
def get_db():

    db = mysql.connector.connect(**DATABASE_CONFIG)
    # Retorna la conexión a la base de datos
    return db


# Función para cerrar la conexión a la base de datos
def close_db(db):
    db.close()


