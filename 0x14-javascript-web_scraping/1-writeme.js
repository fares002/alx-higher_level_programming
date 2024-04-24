#!/usr/bin/node
fs = require('fs');

filePath = process.argv[2];
testData = process.argv[3];

fs.writeFile(filePath, testData, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
