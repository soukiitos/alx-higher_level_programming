#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const data = JSON.parse(body);
    for (const i in data) {
      const task = data[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
	  completed[task.userId] = 1;
	} else {
	  completed[task.userId]++;
	}
      }
    }
    console.log(completed);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});
