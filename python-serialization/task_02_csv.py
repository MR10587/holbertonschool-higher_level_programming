#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', newline='' ) as f:
            text = list(csv.DictReader(f))

            with open('data.json', 'w') as a:
                json.dump(text, a)
        return True
    except FileNotFoundError:
        return False
