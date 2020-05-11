#!/usr/bin/node
exports.esrever = function (list) {
  const aList = [];
  let i = 0;
  for (let index = (list.length) - 1; index >= 0; index--) {
    aList[i] = list[index];
    i++;
  }
  return aList;
};
