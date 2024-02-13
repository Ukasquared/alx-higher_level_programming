#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(Number(args[2]), Number(args[3]));
