#!/usr/bin/node
const sqr_size = process.argv[2];

if (Number(sqr_size)) {
  for (let i = 0; i < sqr_size; i++) {
    console.log('X'.repeat(sqr_size));
  }
} else {
  console.log('Missing size');
}
