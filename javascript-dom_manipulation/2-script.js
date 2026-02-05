#!//usr/bin/node
document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector("header");
    document.querySelector("#red_header").addEventListener("click", () =>{
        header.classList.add("red");
    });
});
