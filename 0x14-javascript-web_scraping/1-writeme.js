#!/usr/bin/node

const filePath = process.argv[2];
const text = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, text, (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
