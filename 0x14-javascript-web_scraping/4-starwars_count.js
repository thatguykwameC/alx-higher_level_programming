#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles”
// is present. Character ID is 18.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(
      results.reduce((count, movie) => {
        return movie.characters.find((character) => character.endsWith('/18/'))
          ? count + 1
          : count;
      }, 0)
    );
  }
});
