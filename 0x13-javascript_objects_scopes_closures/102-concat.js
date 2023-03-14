#!/usr/bin/node
/**
* Writes the content of two files into an output file
*/
const fs = require('fs');
const [file1, file2, output] = process.argv.slice(2);
const fileContents = [file1, file2].map(value => fs.readFileSync(value, 'utf-8'));
fs.writeFileSync(output, fileContents.join(''));
