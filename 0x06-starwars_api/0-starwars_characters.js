#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Construct the URL for the Star Wars API based on the movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, async (error, response, body) => {
  // Check if there was an error with the request
  error && console.log(error);

  // Parse the response body and get the characters array
  const charactersArray = JSON.parse(response.body).characters;

  // Iterate through each character URL in the characters array
  for (const character of charactersArray) {
    // Create a promise to handle the asynchronous request
    await new Promise((resolve, reject) => {
      // Make a GET request to each character URL
      request(character, (error, response, body) => {
        // Check if there was an error with the request
        error && console.log(error);

        // Parse the character data and print the character name
        console.log(JSON.parse(body).name);

        // Resolve the promise to continue the loop
        resolve();
      });
    });
  }
});
