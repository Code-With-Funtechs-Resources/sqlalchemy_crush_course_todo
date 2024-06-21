from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean


BASE = declarative_base()

# table for the todo
class Todo(BASE):
    __tablename__: str = 'todo'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    done = Column(Boolean, default=False)

    def __init__(
            self, title, done
    ):
        self.title = title
        self.done = done