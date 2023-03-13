#!/usr/bin/node

const vars = process.argv.slice(2).map(value => parseInt(value));

function add (a, b) {
  return a + b;
}

console.log(add(...vars));
