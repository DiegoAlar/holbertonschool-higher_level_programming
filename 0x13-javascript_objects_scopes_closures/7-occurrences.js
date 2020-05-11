#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      result += 1;
    }
  }
  return result;
};
