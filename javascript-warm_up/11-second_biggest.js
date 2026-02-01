#!/usr/bin/node
const nmbr = process.argv.length - 2;

if (!nmbr || nmbr === 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secMax = -Infinity;

  for (let i = 2; i <= process.argv.length; i++) {
    if (process.argv[i] > max) {
      secMax = max;
      max = process.argv[i];
    } else if (process.argv[i] > secMax && process.argv[i] != max) {
      secMax = process.argv[i];
    }
  }

  console.log(secMax);
}
