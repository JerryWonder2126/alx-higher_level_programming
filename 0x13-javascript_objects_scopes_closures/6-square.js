#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const filler = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(filler.repeat(this.width));
    }
  }
}

module.exports = Square;
