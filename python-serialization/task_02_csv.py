#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open('filename.csv', 'r', newline='' ) as f:
            data = csv.DictReader(f)
        with open(data.json, 'w') as f:
            for i in data:
                json.dump(i, f)
        return True
    except FileNotFoundError:
        return False
