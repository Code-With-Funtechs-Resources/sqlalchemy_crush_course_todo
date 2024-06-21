from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import BASE

uri: str = 'sqlite:///todo_app.db'

engine = create_engine(uri)
session = sessionmaker(
    bind=engine
)
db_session = session()

# bind the database
BASE.metadata.create_all(bind=engine)

# try to test my connection
try:
    connection = engine.connect()
    connection.close()
    print('Ping!! connected successfully')
except Exception as e:
    print(e)