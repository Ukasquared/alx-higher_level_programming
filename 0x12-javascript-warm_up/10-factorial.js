#!/usr/bin/node

const args = process.argv;
const firstArg = Number(args[2]);
if (!firstArg) console.log(1);
const factorial = function (firstArg) {
  if (firstArg === 1) {
    return (1);
  }
  return firstArg * factorial(firstArg - 1);
};

console.log(factorial(firstArg));
