#!/usr/bin/node
const myNum = process.argv.slice(2);
const limit = myNum[0];
if (limit && parseInt(myNum[0])) {
  for (let index = 0; index < limit; index++) {
    for (let index2 = 0; index2 < limit; index2++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
