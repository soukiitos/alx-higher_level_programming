#!/usr/bin/node
const arr = process.argv.slice(2).map(arg => parseInt(arg)).filter(Number.isInteger);
arr.sort((a, b) => b - a);
console.log(arr[1] || 0);
