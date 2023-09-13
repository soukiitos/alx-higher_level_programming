#!/usr/bin/node
module.exports = class Rectangle {
  constructor (i, j) {
    if (i > 0 && j > 0) {
      [this.width, this.height] = [i, j];
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
