#!/usr/bin/python3
"""Fourth ORM"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3], port=3306
        )
    cs = db.cursor()
    cs.execute(
        "SELECT cities.name \
        FROM cities JOIN states \
        ON states.id = cities.state_id \
        ORDER BY cities.id ASC"
    )
    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    db.close()
