#!/usr/bin/node
const arg1 = process.argv.slice(2);
const parsedInt = parseInt(arg1);
if (!isNaN(parsedInt)) {
  for (let i = 0; i < parsedInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
