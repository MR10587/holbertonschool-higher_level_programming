#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r', newline='' ) as f:
            data = csv.DictReader(f)
            with open(data, 'w') as a:
                for i in data:
                    json.dump(i, a)
        return True
    except FileNotFoundError:
        return False
