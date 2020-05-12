#!/usr/bin/node
const myUrl = process.argv.slice(2)[0];
const request = require('request');
request(myUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  console.log('code:', response.statusCode);
});
