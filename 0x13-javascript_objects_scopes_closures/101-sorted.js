#!/usr/bin/node
const { dict } = require('./101-data');
const obj = Object.entries(dict).reduce((a, [key, value]) => {
  if (!a[value]) {
    a[value] = [];
  }
  a[value].push(key);
  return a;
}, {});
console.log(obj);
