#!/usr/bin/node
const sqrSize = process.argv[2];

if (Number(sqrSize)) {
  for (let i = 0; i < sqrSize; i++) {
    console.log('X'.repeat(sqrSize));
  }
} else {
  console.log('Missing size');
}
