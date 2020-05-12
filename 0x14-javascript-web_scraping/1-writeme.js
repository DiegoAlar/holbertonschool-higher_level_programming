#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');
const myFile = myArgs[0];
const data = myArgs[1];
fs.writeFile(myFile, data, function (err) {
  if (err) {
    console.error(err);
  }
});
