#!/usr/bin/node
const myArgs = process.argv.slice(1);
if (myArgs.length === 1) {
  console.log('No argument');
} else if (myArgs.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
