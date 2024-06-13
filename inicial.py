
from flask import Flask, jsonify


print(">>>>>>>",__name__)

app = Flask(__name__)

class Movie:
    def __init__(self, id, title, release_year, adult=False):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.adult = adult


# Datos de ejemplo
movies = [
    Movie(1, "The Shawshank Redemption", 1994),
    Movie(2, "The Godfather", 1972),
    Movie(3, "The Dark Knight", 2008, True)
]
print(movies)


@app.route('/')
def principal():
    return "Hola que tal!!! 🏆"

@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Recupera todas las películas de la lista de ejemplo.
    """
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



if __name__ == '__main__':
    app.run(debug=True)