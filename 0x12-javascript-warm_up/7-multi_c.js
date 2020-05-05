#!/usr/bin/node
const myNum = process.argv.slice(2);
const limit = myNum[0];
if (limit) {
  for (let index = 0; index < limit; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
