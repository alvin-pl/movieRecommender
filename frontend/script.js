// Listen for button clicks
// Send requests to Flask backend
// Receive movie results
// Display movie cards on the page

const API_BASE_URL = "http://127.0.0.1:5000";

const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const genreSelect = document.getElementById("genreSelect");
const genreButton = document.getElementById("genreButton");
const resultsDiv = document.getElementById("results");

searchButton.addEventListener("click", async function () {
    const query = searchInput.value;

    const response = await fetch(`${API_BASE_URL}/api/movies/search?query=${query}`);
    const movies = await response.json();

    displayMovies(movies);
});

genreButton.addEventListener("click", async function () {
    const genre = genreSelect.value;

    const response = await fetch(`${API_BASE_URL}/api/movies/genre?genre=${genre}`);
    const movies = await response.json();

    displayMovies(movies);
});

function displayMovies(movies) {
    resultsDiv.innerHTML = "";

    if (movies.length === 0) {
        resultsDiv.innerHTML = "<p>No movies found.</p>";
        return;
    }

    movies.forEach(function (movie) {
        const movieCard = document.createElement("div");
        movieCard.className = "movie-card";

        movieCard.innerHTML = `
            <h3>${movie.title}</h3>
            <p><strong>Genre:</strong> ${movie.genre}</p>
            <p><strong>Release Date:</strong> ${movie.release_date}</p>
            <p><strong>Actors:</strong> ${movie.actors.join(", ")}</p>
            <p><strong>Runtime:</strong> ${movie.runtime}</p>
            <p>${movie.description}</p>
            <a href="${movie.trailer_url}" target="_blank">Watch Trailer</a>
        `;

        resultsDiv.appendChild(movieCard);
    });
}