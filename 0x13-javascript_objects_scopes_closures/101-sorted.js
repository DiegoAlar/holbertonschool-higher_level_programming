#!/usr/bin/node
const dict = require('./101-data').dict;
const aDict = {};
Object.keys(dict).forEach(function (key) {
  if (aDict[dict[key]]) {
    aDict[dict[key]].push(key);
  } else {
    aDict[dict[key]] = [key];
  }
});
console.log(aDict);
