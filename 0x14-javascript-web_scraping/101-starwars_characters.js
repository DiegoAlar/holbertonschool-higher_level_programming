#!/usr/bin/node
const id = process.argv.slice(2)[0];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(body);
        const data = JSON.parse(body);
        const chars = data.characters;
        return (chars);
      } else {
        console.log(error);
      }
    });
  });
}

function doRequest2 (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(body);
        const data2 = JSON.parse(body);
        console.log(data2.name);
      } else {
        reject(error);
      }
    });
  });
}

// Usage:

async function main () {
  const res = await doRequest(url);
  for (let index = 0; index < JSON.parse(res).characters.length; index++) {
    const charUrl = JSON.parse(res).characters[index];
    await doRequest2(charUrl);
  }
}

main();
