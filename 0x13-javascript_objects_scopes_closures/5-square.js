#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    /* call the constructor of the rectangle class */
    super(size, size);
  }
}

module.exports = Square;
