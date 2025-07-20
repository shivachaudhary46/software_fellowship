'''
importing important libraries, and classes from fastapi like FastAPI, HTTPException, 
JSONResponse. 
'''
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from pydantic import BaseModel
import json 

'''
we are appending new dictionary elements in the todos.json, so we have proper 
backend structure flowing. 
'''
DATA_PATH = "todos.json"

'''
intitalising the FastAPI
'''
app = FastAPI()

'''
Base model checks whether the request methods follows 
{id: int, title: str, completed: bool}
these structures. 
'''
class Todo(BaseModel):
    id: int
    title: str
    completed: bool 

'''
reading and writing todos.json file
'''
def read_todos():
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []

def write_todos(todo):
    try:
        with open(DATA_PATH, 'w') as f:
            json.dump(todo, f, indent=2 )
    except FileNotFoundError:
        return []

'''
routing /create-todo app which will create a post method in the app. read todos.json. 
file and extract all elements in variable todos. so, todos, must be a list of an dictonary 
items. if todos first element [id] equals to todo.id then we cannot append same element in that 
todos.json file. so, it priotize redundancy. So, raise HTTPextension error. And converting each 
element to dictionary because new element must be added to our todos app. and we can finally 
write_todos function with dictinary as argument. 
'''
@app.post("/create-todo")
def create_todos(todo: Todo):
    todos = read_todos()

    for t in todos:
        if t["id"] == int(todo.id):
            raise HTTPException(status_code=400, detail='Todo with given id already exist')
    
    todo_dict = todo.dict()
    todos.append(todo_dict)
    write_todos(todos)

    return todo_dict

'''
routing with get request as ('/') default page, we have to read an todos.json file and return 
content of the json file by using JSONResponse(content=your_file_readed, status_code=200)
'''
@app.get("/")
def read_todos_route():
    todos = read_todos()
    return JSONResponse(content=todos, status_code=200)

'''
routing with get request in get_todo/{your_id_in_intger} route 
and returning with json id, title and completed
'''
@app.get("/get-todo/{todo_id}")
def get_todo_by_id(todo_id: int):
    todos = read_todos()

    for t in todos:
        if int(t['id'] == todo_id):
            return JSONResponse(content=t, status_code=200)
        
    raise HTTPException(status_code=404, detail="Todo not found")
    