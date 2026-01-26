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
        WHERE states.name = %s \
        ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    rows = cs.fetchall()
    print(', '.join(row[0] for row in rows))

    cs.close()
    db.close()
