#!/usr/bin/node
/**
* Writes the content of two files into an output file
*/
const fs = require('fs');
const filePaths = process.argv.slice(2);
if (!filePaths.length === 3) {
  const [file1, file2, output] = filePaths;
  try {
    const fileContents = [file1, file2].map(value => fs.readFileSync(value, 'utf-8'));
    fs.writeFileSync(output, fileContents.join(''));
  } catch (err) {
    console.log(err.message);
  }
}
