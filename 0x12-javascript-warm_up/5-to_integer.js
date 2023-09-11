#!/usr/bin/node
const intnum = parseInt(process.argv[2]);
if (isNaN(intnum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${intnum}`);
}
