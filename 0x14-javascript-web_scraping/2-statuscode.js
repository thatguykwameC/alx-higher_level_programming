#!/usr/bin/node

// This script makes a request to the received URL and displays the status code

const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
