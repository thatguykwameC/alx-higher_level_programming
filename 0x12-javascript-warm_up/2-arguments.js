#!/usr/bin/node

const lenArg = process.argv.length;

if (lenArg === 3) {
  console.log('Arguement found');
} else if (lenArg > 3) {
  console.log('Arguements found');
} else {
  console.log('No arguement');
}
