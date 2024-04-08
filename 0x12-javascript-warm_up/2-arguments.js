#!/usr/bin/node

const lenArg = process.argv.length;

if (lenArg <= 2) {
  console.log('No arguement');
} else if (lenArg === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
