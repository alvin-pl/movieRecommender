# the power button for your Flask server

# Responsibility:

# create Flask app
# Connect routes
# run server

from flask import Flask
from flask_cors import CORS
from movie_routes import movie_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(movie_routes)


@app.route("/")
def home():
    return {"message": "Movie Recommender API is running"}


if __name__ == "__main__":
    app.run(debug=True)