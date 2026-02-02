#!/usr/bin/python3
"""Model State"""

import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://%s:%s@localhost/%s"
        % (sys.argv[1], sys.argv[2], sys.argv[3])
    )

    session = Session(engine)
    state = (
        session.query(State).
        filter(State.name.ilike("%a%")).
        order_by(State.id).all()
        )
    for i in state:
        print(f"{i.id}: {i.name}")

    session.close()
