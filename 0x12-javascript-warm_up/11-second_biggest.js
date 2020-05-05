#!/usr/bin/node
const myArray = process.argv.slice(2);

if (!myArray[0] || myArray.length === 1) {
  console.log(0);
} else {
  console.log('entered');
  myArray.sort(function (a, b) {
    return a - b;
  });
  console.log(myArray[myArray.length - 2]);
}
