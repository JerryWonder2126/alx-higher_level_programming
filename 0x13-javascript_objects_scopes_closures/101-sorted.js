#!/usr/bin/node

const dict = require('./101-data.js').dict;

const result = {};

for (const key of Object.keys(dict)) {
  const value = dict[key];
  if (!(value in result)) {
    result[value] = [];
  }
  result[value].push(key);
}

console.log(result);
