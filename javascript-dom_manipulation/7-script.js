#!/usr/bin/node
const ul = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        for(movie of data.results) {
            const li = document.createElement("li");
            li.textContent = movie.title;
            ul.append(li);
        };
    });