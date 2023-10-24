#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const homeworld = 'https://swapi-api.alx-tools.com/api/films/';

request(homeworld + url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log('ERROR: ' + response.statusCode);
  } else {
    const resp = JSON.parse(body);
    console.log(resp.title);
  }
});
