# this defines your api URLs

# Responsibility:

# when user visits /api/movies, return all movies
# when user searches, return matching movies
# when users filters by genre, return recommended movies

from flask import Blueprint, jsonify, request
from movie_service import get_all_movies, search_movies, get_movies_by_genre

movie_routes = Blueprint("movie_routes", __name__)


@movie_routes.route("/api/movies", methods=["GET"])
def movies_index():
    return jsonify(get_all_movies())


@movie_routes.route("/api/movies/search", methods=["GET"])
def movies_search():
    query = request.args.get("query", "")
    results = search_movies(query)
    return jsonify(results)


@movie_routes.route("/api/movies/genre", methods=["GET"])
def movies_by_genre():
    genre = request.args.get("genre", "")
    results = get_movies_by_genre(genre)
    return jsonify(results)