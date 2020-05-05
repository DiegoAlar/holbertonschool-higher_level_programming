#!/usr/bin/node
var myArgs = process.argv.slice(1);
if (myArgs.length === 1) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
