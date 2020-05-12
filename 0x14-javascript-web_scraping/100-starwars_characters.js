#!/usr/bin/node
const id = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const chars = data.characters;
    for (let index = 0; index < chars.length; index++) {
      const charUrl = chars[index];
      request(charUrl, function (error, response, body2) {
        if (error) {
          console.log(error);
        } else {
          const dataChar = JSON.parse(body2);
          console.log(dataChar.name);
        }
      });
    }
  }
});
