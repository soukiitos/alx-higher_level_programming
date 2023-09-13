#!/usr/bin/node
exports.converter = function (i) {
  return j => j.toString(i);
};
