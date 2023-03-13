#!/usr/bin/node

const var1 = parseInt(process.argv[2]);
if (!var1) console.log('Missing number of occurrences');
for (let i = 0; i < var1; i++) {
  console.log('X'.repeat(var1));
}
