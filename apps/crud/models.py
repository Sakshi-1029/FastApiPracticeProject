from sqlalchemy import Column, Integer, String

# from db.session import Base, engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(50))


# Create the database
# Base.metadata.create_all(engine)
