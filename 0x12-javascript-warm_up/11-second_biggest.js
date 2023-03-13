#!/usr/bin/node

const nums = process.argv.splice(2).map(value => parseInt(value));

function secondLargest (numArray) {
  numArray.sort((a, b) => a - b);
  return !numArray.length || numArray.length === 1 ? 0 : numArray.slice(-2, -1)[0];
}

console.log(secondLargest(nums));
