#!/usr/bin/node
exports.esrever = function (l) {
  return l.reduceRight(function (a, b) {
    a.push(b);
    return a;
  }, []);
};
