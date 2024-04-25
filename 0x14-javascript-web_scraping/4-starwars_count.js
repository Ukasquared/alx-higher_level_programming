#!/usr/bin/node
// Script that prints all movies of the
// character Wedge Antilles

const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movie = JSON.parse(body).results;
  const wedge = movie.filter(movie => movie.characters.includes(
    'https://swapi-api.alx-tools.com/api/people/14/'));
  console.log(wedge.length);
});
