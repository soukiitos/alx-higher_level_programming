#!/usr/bin/node
exports.nbOccurences = function (l, search) {
  const f = l.filter(current => current === search);
  return f.length;
};
