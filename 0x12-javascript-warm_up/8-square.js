#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let arg = '';
    for (let j = 0; j < size; j++) {
      arg += 'X';
    }
    console.log(arg);
  }
} else {
  console.log('Missing size');
}
