#!/usr/bin/node
const argv1 = process.argv[2];
if (argv1) {
  for (let i = 0; i < argv1; i++) {
    if (argv1) { console.log('C is fun'); }
  }
} else {
  console.log('Missing number of occurrences');
}
