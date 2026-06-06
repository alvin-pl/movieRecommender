PROJECT NAME:
Movie Recommender

TARGET USERS:
People who want to watch a movie but do not know what to pick

CORE ACTIONS:
Choose a movie genre
Search for a movie
Search for an actor
view movie recommendations
click a movie to see more details

MAIN SCREENS/PAGES:
Home
Movie choice 
Movie results
Movie detail

DATA MODELS:
Movie
-id
-title
-genre
-releaseDate
-actors
-runtime
-description
-posterURL
-trailerURL

User
-id
-username 

CORE FUNCTIONS:
searchMovie()
getMovieRecommendations()
getMovieDetails()
filterMoviesByGenre()
searchMovieByActor()

API ROUTES:
GET api/movies
GET api/movies/search
GET api/movie/recommendation
GET api/movies/{id}

EXTERNAL SERVICES:
Movie API (e.g., TMDb, OMDB)
Trailer link (e.g., YouTube)

MVP:
search + pick movie genre
get movie results back

VERSION 2:
login
database
saved movie
movie trailer
movie opinions/reviewa

SCALE:
admin page
put data is JSON file
cache api results
add ratings
personalized recommendations



# movieRecommender
