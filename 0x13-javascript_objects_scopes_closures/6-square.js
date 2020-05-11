#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charPrint;
    if (c && typeof c === 'string') {
      charPrint = c;
    } else {
      charPrint = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let k = 0; k < this.width; k++) {
        process.stdout.write(charPrint);
      }
      console.log('');
    }
  }
}
module.exports = Square;
