#!/usr/bin/node
const nmbrargs = process.argv.length - 2;

if (nmbrargs === 0) {
  console.log('No argument');
} else if (nmbrargs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
