#!/usr/bin/node

const var1 = parseInt(process.argv[2]);
const output = var1 ? `My number: ${var1}` : 'Not a number';

console.log(output);
