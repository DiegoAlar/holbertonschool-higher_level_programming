#!/usr/bin/node
const list = require('./100-data').list;
const aList = [];
const map1 = list.map(function (x) {
  aList.push(list.indexOf(x) * x);
});

console.log(list);
console.log(aList);
