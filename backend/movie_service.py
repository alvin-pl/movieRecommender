# where your movie logic lives

# Responsibility:

# search movies
# filter by genre
# find movie by ID
# return recommendations

from movies import movieData


def get_all_movies():
    return movieData

# not sure what this
def search_movies(query):
    query = query.lower()

    results = []

    for movie in movies:
        title_match = query in movie["title"].lower()
        actor_match = any(query in actor.lower() for actor in movie["actors"])

        if title_match or actor_match:
            results.append(movie)

    return results


def get_movies_by_genre(genre):
    genre = genre.lower()

    results = []

    for movie in movies:
        if movie["genre"].lower() == genre:
            results.append(movie)

    return results