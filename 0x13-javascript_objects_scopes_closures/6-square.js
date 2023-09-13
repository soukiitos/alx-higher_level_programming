#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (a) {
    if (a === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(a.repeat(this.width));
      }
    }
  }
};
