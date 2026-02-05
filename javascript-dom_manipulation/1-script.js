#!//usr/bin/node
document.addEventListener("DOMContentLoaded", () => {
    const head = document.querySelector("header");

    document.querySelector("#red_header").addEventListener("click", () => {
        head.style.color = "#FF0000";
    });
});
