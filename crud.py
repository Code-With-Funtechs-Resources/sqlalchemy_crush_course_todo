from connection import db_session
from model import Todo
import decode

# create
def create_todo(title: str, done: bool):
    title = title
    done = done 
    req = Todo(title, done)
    db_session.add(req)
    db_session.commit()
    print("Data added successfully")
    

# get 
# get all data
def all_todos():
    res = db_session.query(Todo).all()
    docs = decode.decode_todos(res)
    print(docs)

# get one
def todo(_id: int):
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
        doc = decode.decode_todo(res)
        print(doc)
    else:
        print(F'record with id {_id} do not Exist')

# update
def update_todo(_id: int , data:dict):
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
        if 'title' in data:
            res.title = data['title']
        if 'done' in data:
            res.done = data['done']
        db_session.commit()
        todo(_id)

    else:
        print(F'record with id {_id} do not Exist')

# delete
def delete_todo(_id: int):
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
        db_session.delete(res)
        db_session.commit()
        print('Data deleted successfully')
    else:
        print(F'record with id {_id} do no t Exist')


# create_todo('Web dev', False)

# all_todos()

todo(2)

# update_todo(1, {'done': True})

# delete_todo(3)