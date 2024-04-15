#!/usr/bin/python3

"""This module adds the 'Louisiana' state as a State
object to the `hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def add_state_to_db(
    username: str, password: str, database: str, state_name: str
):
    """Adds the 'Louisiana' state as a State object to the database."""

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        new_state = State(name=state_name)
        session.add(new_state)
        session.commit()

        print(new_state.id)


if __name__ == "__main__":
    try:
        add_state_to_db(sys.argv[1], sys.argv[2], sys.argv[3], "Louisiana")
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <db_name>\n"
        )
        sys.exit(1)
