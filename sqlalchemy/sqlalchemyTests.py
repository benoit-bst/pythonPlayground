#!/usr/bin/python

from sqlalchemy import Column, Integer, String  # pragma: no cover
from sqlalchemy.ext.declarative import declarative_base  # pragma: no cover
from sqlalchemy import create_engine  # pragma: no cover
from sqlalchemy.orm import sessionmaker  # pragma: no cover

Base = declarative_base()

# # conn = engine.connect()
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(250), nullable=False)

#---------------------------------
# Create an engine that stores data in the local directory's
# test.db file.
engine = create_engine('sqlite:///test.db')

#---------------------------------
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
# insert a user in the DB
new_person = User(username='tata')
session.add(new_person)

new_person = User(username='spetegnief')
session.add(new_person)

session.commit()

#---------------------------------
# Connect to db
conn = engine.connect()
result = conn.execute("select username from users")
for row in result:
  print("username", row['username'])
conn.close()
