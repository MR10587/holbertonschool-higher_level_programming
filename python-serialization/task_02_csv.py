#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open('filename.csv', 'r', newline='' ) as f:
            data = csv.DictReader(f)
        for i in data:
            json.dump(i, data.json)
        return True
    except FileNotFoundError:
        return False
