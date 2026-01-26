#!/usr/bin/python3
"""First No sql"""

import sys
from sqlalchemy import create_engine, text
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://%s:%s@localhost/%s"
        % (sys.argv[1], sys.argv[2], sys.argv[3])
    )

    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, name FROM states ORDER BY id ASC")
        )

        for row in result:
            print(f"{row.id}: {row.name}")
