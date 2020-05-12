#!/usr/bin/node
const myId = process.argv.slice(2)[0];
if (myId) {
  const myUrl = 'https://swapi-api.hbtn.io/api/films/' + myId;
  const request = require('request');
  request(myUrl, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      if (JSON.parse(body).title) {
        console.log(JSON.parse(body).title);
      }
    }
  });
}
