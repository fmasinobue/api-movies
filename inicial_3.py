import os, time
# Instalar con pip install flask
from flask import Flask, jsonify, request
# Instalar con pip install flask-cors
from flask_cors import CORS

"""
Para trabajar con archivos asegurar que un nombre de archivo 
proporcionado por el usuario sea seguro para guardarlo en el sistema de archivos.
"""
# Si es necesario, pip install Werkzeug 
from werkzeug.utils import secure_filename

from app.models.movie import Movie
from app.database import init_app, init_db

"""
Crear las dependencias
pip freeze > requirements.txt

Instalar todas las dependencias
pip install -r requirements.txt

"""
d = os.path.dirname(__file__)
os.chdir(d)

ruta_destino = 'static/img/'


app = Flask(__name__)
CORS(app)

# Inicializar la base de datos con la aplicación Flask
init_app(app)

@app.route('/init-db')
def init_db_route():
    init_db()
    return "Base de datos inicializada correctamente."

@app.route('/')
def principal():
    return "Hola que tal!!! 🏆"

@app.route('/movies', methods=['POST'])
def create_movie():
    print("HOLA")
    # data = request.json
    data = request.form
    print("que hay en data ", data)
    archivo=request.files['imagen']
    print(archivo)
    # Trabajamos con la imagen
    # Utilizamos la función `secure_filename` para obtener un nombre de archivo seguro para la imagen cargada. 
    # Esta función elimina caracteres especiales que podrían causar problemas de seguridad.
    nombre_imagen = secure_filename(archivo.filename)

    print(">>>>>>>>>", nombre_imagen)

    # Separamos el nombre base del archivo y su extensión utilizando `os.path.splitext`.
    # Esto nos permite trabajar con el nombre y la extensión por separado.
    nombre_base, extension = os.path.splitext(nombre_imagen)

    # Generamos un nuevo nombre para el archivo utilizando el nombre base original y 
    # agregando un timestamp para asegurarnos de que el nombre del archivo sea único.
    # Concatenamos el nombre base, un guion bajo, el timestamp actual y la extensión.
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"

    # Guardamos el archivo en la ruta de destino utilizando el nuevo nombre generado.
    # `os.path.join` se asegura de que la ruta sea correcta, sin importar el sistema operativo.
    archivo.save(os.path.join(ruta_destino, nombre_imagen))



    new_movie = Movie(title=data['title'], adult=data['adult'], release_year=data['release_year'], poster_url=nombre_imagen)
    new_movie.save()
    return jsonify({'message': 'Pelicula creada correctamente 😎'}), 201


@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.get_all()
    movies_json=[]
    for m in movies:
        movies_json.append(m.serialize())
    return movies_json
    # Manera resumida:
    # return jsonify([movie.serialize() for movie in movies])


@app.route('/movies/<int:id>', methods=['GET'])
def get_by_id_movie(id):
    movie = Movie.get_by_id(id)
    if movie:
        return jsonify(movie.serialize())
    else:
        return jsonify({'message': 'Pelicula no encontrada'}), 404

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.get_by_id(id)
    if not movie:
        return jsonify({'message': 'Pelicula no encontrada'}), 404
    movie.delete()
    return jsonify({'message': 'La peli fue borrada'})

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.get_by_id(id)
    if not movie:
        return jsonify({'message': 'Pelicula no encontrada'}), 404
    data = request.form
    movie.title = data.get('title', movie.title)
    movie.adult = data.get('adult', movie.adult)
    movie.release_year = data.get('release_year', movie.release_year)
    # movie.poster_url = data.get('poster_url', movie.poster_url)
    movie.save()
    return jsonify({'message': 'Pelicula actualizada correctamente 😋'})


if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000)