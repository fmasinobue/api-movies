# Instalar con pip install flask
from flask import Flask, jsonify, request
# Instalar con pip install flask-cors
from flask_cors import CORS

from app.models.movie import Movie


from app.database import init_app

"""
Crear las dependencias
pip freeze > requirements.txt

Instalar todas las dependencias
pip install -r requirements.txt

"""
app = Flask(__name__)
CORS(app)

# Inicializar la base de datos con la aplicación Flask
init_app(app)


@app.route('/')
def principal():
    return "Hola que tal!!! 🏆"

@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.json
    print("que hay en data ", data)
    new_movie = Movie(title=data['title'], adult=data['adult'], release_year=data['release_year'], poster_url=data['poster_url'])
    new_movie.save()
    return jsonify({'message': 'Movie created successfully'}), 201


@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.get_all()
    movies_json=[]
    for m in movies:
        movies_json.append(m.serialize())
    return movies_json
    # Manera resumida:
    # return jsonify([movie.serialize() for movie in movies])

'''
@app.route('/movies/<int:id>', methods=['GET'])
def get_by_id_movie(id):
    movie = Movie.get_by_id(id)
    if movie:
        return jsonify(movie.serialize())
    else:
        return jsonify({'message': 'Movie Not found'}), 404
'''
if __name__ == '__main__':
    app.run(debug=True)