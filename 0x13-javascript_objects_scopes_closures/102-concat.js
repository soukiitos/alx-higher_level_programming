#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');
fs.readFile(argv[2], 'utf8')
  .then(i => fs.writeFile(argv[4], i, 'utf8'))
  .catch(j => console.error(j));
fs.readFile(argv[3], 'utf8')
  .then(i => fs.writeFile(argv[4], i, { flag: 'a' }, 'utf8'))
  .catch(j => console.error(j));
