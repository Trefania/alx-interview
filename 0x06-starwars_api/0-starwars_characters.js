#!/usr/bin/node

const request = require('request');

// Function to retrieve the character names from a specific Star Wars movie
function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  // Make a request to the Star Wars API to get the movie data
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const film = JSON.parse(body);
      const characters = film.characters;

      // Iterate over the character URLs and fetch their data
      characters.forEach((characterUrl) => {
        // Make a request to each character URL
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name); // Print the character name
          }
        });
      });
    }
  });
}

// Retrieve the movie ID from the command line argument
const movieId = process.argv[2];

// Call the function with the provided movie ID
getMovieCharacters(movieId);
