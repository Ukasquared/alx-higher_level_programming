#!/usr/bin/python3

""" model state instance"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2],
                                  argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    query = session.query(State).all()
    for result in query:
        print(f"{result.id}")
