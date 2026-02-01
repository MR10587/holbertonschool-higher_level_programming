#!/usr/bin/node
const nmbr = process.argv.length - 2;

if (nmbr < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let secMax = -Infinity;

  for (let i = 2; i < process.argv.length; i++) {
    const n = Number(process.argv[i]);

    if (n > max) {
      secMax = max;
      max = n;
    } else if (n > secMax && n < max) {
      secMax = n;
    }
  }

  console.log(secMax);
}
