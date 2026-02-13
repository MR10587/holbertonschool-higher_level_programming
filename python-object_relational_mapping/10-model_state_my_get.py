#!/usr/bin/python3
"""
Prints the id of the first State matching the given name
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name searched>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    state_which_was_given = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State).
             filter(State.name == state_which_was_given).
             order_by(State.id).first())

    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()