#!/usr/bin/node
const argv1 = process.argv[2];
const argv2 = process.argv[3];

if (argv1 && argv2) {
  console.log(argv1, 'is', argv2);
} else if (argv1 && !argv2) {
  console.log(argv1, 'is undefined');
} else {
  console.log('undefined is undefined');
}
