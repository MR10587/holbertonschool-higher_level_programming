#!/usr/bin/python3
import requests
import csv


url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    a = requests.get(url)
    print(f"Status Code: {a.status_code}")

    if a.status_code == 200:
        j = a.json()
        for title in j:
            print(title["title"])


def fetch_and_save_posts():
    a = requests.get(url)
    print(f'Status code: {a.status_code}')
    if a.status_code == 200:
        j = a.json()
        new_post = []
        for post in j:
            new_post.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        with open("posts.csv", 'w', newline='', encoding='utf-8') as f:
            new_file = csv.DictWriter(
                f,
                fieldnames=["id", "title", "body"]
            )
            new_file.writeheader()
            new_file.writerows(new_post)
