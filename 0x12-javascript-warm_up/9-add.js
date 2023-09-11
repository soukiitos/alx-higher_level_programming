#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const Firstarg = parseInt(process.argv[2]);
const Secarg = parseInt(process.argv[3]);
if (!isNaN(Firstarg) && !isNaN(Secarg)) {
  console.log(add(Firstarg, Secarg));
} else {
  console.log(NaN);
}
