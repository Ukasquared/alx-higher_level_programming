#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  let index = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newArray[index] = list[i];
    index++;
  }
  return (newArray);
};
