#!/usr/bin/node

// This script reads from a file and displays the contents on standard output.

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
