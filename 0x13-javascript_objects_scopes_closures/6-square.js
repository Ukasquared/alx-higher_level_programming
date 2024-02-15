#!/usr/bin/node
const Squar = require('./5-square.js');

class Square extends Squar {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        if (c) {
          string += c;
        } else {
          string += 'X';
        }
      }
      console.log(string);
    }
  }
}

module.exports = Square;
