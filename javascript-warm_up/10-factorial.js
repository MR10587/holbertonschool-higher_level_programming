#!/usr/bin/node
function factorial () {
  let proc = 1;
  const num = process.argv[2];

  if (Number(num) === 1) {
    console.log('NaN');
  } else if (!Number(num) || !num) {
    console.log(1);
  } else {
    for (let i = 1; i <= num; i++) {
      proc *= i;
    }
    console.log(proc);
  }
}
