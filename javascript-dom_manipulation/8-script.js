#!/usr/bin/node
document.addEventListener("DOMContentLoaded", () => {
    const hi = document.querySelector("#hello");
    (async function() {
        const response = await fetch("https://hellosalut.stefanbohacek.com/?lang=fr");
        const data = await response.json();
        console.log(data);
        hi.textContent = data.hello;
    })();
});
