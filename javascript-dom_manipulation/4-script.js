#!/usr/bin/node
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector("#add_item");
    const ul = document.querySelector(".my_list");

    btn.addEventListener("click", () =>{
        let li = document.createElement("li");
        li.textContent = "Item";
        ul.append(li);
    });
});
