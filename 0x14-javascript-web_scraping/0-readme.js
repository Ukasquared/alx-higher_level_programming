#!/usr/bin/node

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, (err, fileData) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(fileData.toString());
});
