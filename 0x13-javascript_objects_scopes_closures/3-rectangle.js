#!/usr/bin/node
module.exports = class Rectangle {
  constructor (i, j) {
    if (i > 0 && j > 0) {
      [this.width, this.height] = [i, j];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
