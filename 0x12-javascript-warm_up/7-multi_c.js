#!/usr/bin/node

const args = process.argv;
const firstArg = Number(args[2]);
if (!firstArg) console.log('Missing number of occurrences');
for (let i = 0; i < firstArg; i++) console.log('C is fun');
