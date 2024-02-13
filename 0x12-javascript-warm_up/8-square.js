#!/usr/bin/node

const arg = process.argv;
const firstArg = Number(arg[2]);
if (!firstArg) console.log('Missing size');
for (let i = 0; i < firstArg; i++) {
  let string = '';
  for (let j = 0; j < firstArg; j++) {
    string += 'X';
  }
  console.log(string);
}
