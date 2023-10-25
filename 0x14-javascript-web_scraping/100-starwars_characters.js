#!/usr/bin/node

const request = require('request');
const urlID = process.argv[2];
const homeworld = 'https://swapi-api.alx-tools.com/api/films/';
request.get(homeworld + urlID, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const task = data.characters;
  for (const i of task) {
    request.get(i, function (error, response, bo_dy) {
      if (error) {
        console.log(error);
      }
      const dt = JSON.parse(bo_dy);
      console.log(dt.name);
    });
  }
});