#!/usr/bin/node
const myArgs = process.argv.slice(2);
const url = myArgs[0];
const myFile = myArgs[1];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log(body);
  fs.writeFile(myFile, body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
