#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const aObj = {};
    for (const obj in data) {
      if (data[obj].completed) {
        if (isNaN(aObj[data[obj].userId])) {
          aObj[data[obj].userId] = 1;
        } else {
          aObj[data[obj].userId] += 1;
        }
      }
    }
    console.log(aObj);
  }
});
