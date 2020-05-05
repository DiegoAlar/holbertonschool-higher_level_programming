#!/usr/bin/node
const myNum = process.argv.slice(2);
let num;
if (myNum[0]) {
  num = parseInt(myNum[0]);
} else {
  num = 1;
}
function recursiveFun (n) {
  if (n < 0) {
    return -1;
  } else if (n === 0) {
    return 1;
  }
  return (n * recursiveFun(n - 1));
}
const result = recursiveFun(num);
console.log(result);
