#!/usr/bin/node
const myFile = process.argv.slice(2)[0];
const fs = require('fs');
fs.readFile(myFile, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
