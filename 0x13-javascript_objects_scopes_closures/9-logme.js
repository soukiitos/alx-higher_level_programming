#!/usr/bin/node
let i = 0;
exports.logMe = function (j) {
  console.log(`${i++}: ${j}`);
};
