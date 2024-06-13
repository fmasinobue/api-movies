# Instalar con pip install flask
from flask import Flask, jsonify, request
# Instalar con pip install flask-cors
from flask_cors import CORS

from app.models import Movie

from app.dataPeli import movies
"""
Crear las dependencias
pip freeze > requirements.txt

Instalar todas las dependencias
pip install -r requirements.txt

"""
app = Flask(__name__)
CORS(app)




# Datos de ejemplo
# movies = [
#     Movie(1, "The Shawshank Redemption", 1994),
#     Movie(2, "The Godfather", 1972),
#     Movie(3, "The Dark Knight", 2008, True)
# ]


@app.route('/')
def principal():
    return "Hola que tal!!! 🏆"

@app.route('/movies', methods=['GET','POST'])
def moviesEndpoint():
    """
    Recupera todas las películas de la lista de ejemplo.
    """
    if request.method == 'GET':
        movies_list = [] 
        for movie in movies:
            peli={
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "adult": movie.adult
            }
            movies_list.append(peli) 

        return jsonify(movies_list)
    else:
        # POST
        data = request.get_json()
        print("Holaaaaaaaaaa",data)
        new_movie = Movie(
            id=data['id'],
            title=data.get('title'),
            release_year=data.get('release_year'),
            adult=data.get('adult', False)
        )
        movies.append(new_movie)
        new_movie_dict = {
            "id": new_movie.id,
            "title": new_movie.title,
            "release_year": new_movie.release_year,
            "adult": new_movie.adult
        }
        print(">>>>>>>>>>>>>>>>>>>>>>>",len(movies))
        return jsonify(new_movie_dict), 203



if __name__ == '__main__':
    app.run(debug=True)