
#~ <|-------------------------------------- Notes --------------------------------------|>
#? REST - Representational State Transfer
#? Architecture designing design pattern for building connected services

#? ReSTful systems should consist of:
#* 1. Idempotent routes and routines
#* 2. Endpoints that use plural nouns for names: /users, /products, /orders, etc.
#* 3. HTTP methods should be mapped correctly to the type of operation, so:
#*  3.1. POST is for create
#*  3.2. GET is for read
#*  3.3. PUT/PATCH are for update (complete and partial)
#*  3.4. DELETE is for deleting
#*  3.5. Remember, scan is another read operation, so that uses GET as well.
#~ <|-----------------------------------------------------------------------------------|>

#& |-------------------library's-------------------|

from flask import (Flask, request)
from app.database import task

#& |-------------------local files-------------------|

app = Flask(__name__)

#& |-------------------routes-------------------|

#? Double decorator to avoid 404 error
@app.get("/") #? root route
@app.get("/tasks") #? get all tasks
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out #* Flask will return a 200 status by default

#? get a single task
@app.get("/tasks/<int:pk>") #* <-- <int:pk> --> is a path parameter | pk = primary key
def get_single_task(pk):
    out = {
        "task": task.selected_by_id(pk),
        "ok": True
    }
    return out

#? create a new task
@app.post("/tasks") 
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

#? update a task
@app.put("/tasks/<int:pk>") 
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

#? delete a task
@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

