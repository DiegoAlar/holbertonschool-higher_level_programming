#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const character = '18';
    const listCharsId = [];
    const data = JSON.parse(body).results;
    for (const obj in data) {
      const listChars = data[obj].characters;
      for (let index = 0; index < listChars.length; index++) {
        const charId = listChars[index].split('/');
        if ((charId[charId.length - 2]) === character) {
          listCharsId.push(charId[charId.length - 2]);
        }
      }
    }
    console.log(listCharsId.length);
  }
});
