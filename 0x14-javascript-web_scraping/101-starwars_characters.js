#!/usr/bin/node
const request = require('request');
const urlID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + urlID, function (error, response, body) {
  if (!error) {
    const chrs = JSON.parse(body).characters;
    printCharacters(chrs, 0);
  }
});

function printCharacters (chrs, index) {
  request(chrs[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chrs.length) {
        printCharacters(chrs, index + 1);
      }
    }
  });
}
