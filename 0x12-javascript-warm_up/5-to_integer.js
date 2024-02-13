#!/usr/bin/node

const args = process.argv;
const firstNum = Number(args[2]);
if (firstNum) console.log(`My number: ${firstNum}`);
else console.log('Not a number');
