#!/usr/bin/node

// This script writes the contents received on the CLI to a file.

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (error) => {
  if (error) {
    console.log(error);
  }
});
