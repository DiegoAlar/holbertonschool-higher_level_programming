#!/usr/bin/node
const myNums = process.argv.slice(2);
const num1 = parseInt(myNums[0]);
const num2 = parseInt(myNums[1]);

function myFun (a, b) {
  console.log(a + b);
}
myFun(num1, num2);
