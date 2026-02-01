#!/usr/bin/node
function add(a, b) {
    if (Number(process.argv[2]) && Number(process.argv[3])) {
        const sum = Number(process.argv[2]) + Number(process.argv[3]);
        console.log(sum);
    } else {
        console.log("NaN");
    }
}

add()