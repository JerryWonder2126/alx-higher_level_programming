#!/usr/bin/node

const var1 = parseInt(process.argv[2]);

function factorial (a) {
  if (!a) return 1;
  return a * factorial(a - 1);
}

console.log(factorial(var1));
