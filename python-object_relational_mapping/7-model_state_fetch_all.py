#!/usr/bin/python3
"""First No sql"""

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://%s:%s@localhost/%s"
        %(sys.argv[1], sys.argv[2], sys.argv[3])
    )

    with engine.connect() as conn:
        result = conn.execute(
            "SELECT id, name FROM states ORDER BY id ASC"
        )

        for row in result:
            print(f"{row[0]}: {row[1]}")
