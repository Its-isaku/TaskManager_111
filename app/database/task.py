
#? libraries
from app.database import get_db

#? Format the output
def output_formatter(results):
    out = []
    for task in results:
        res = {
            "id": task[0],
            "name": task[1],
            "summary": task[2],
            "description": task[3],
            "is_done": task[4]
        }
        out.append(res)
    return out

#? Get all tasks
def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM tasks", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

#? Select a task by id
def selected_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id, )) #! Comma
    results = cursor.fetchall()
    if results:
        return output_formatter(results) [0] #* [0] to get the first element of the list
    return {}

#? Insert a new task
def insert(task_data):
    task_tuple = (
        task_data["name"],
        task_data["summary"],
        task_data["description"]
    )
    statement = """
        INSERT INTO tasks (
            name,
            summary,
            description
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

#? Update a task by id
def update_by_id(task_data, task_id):
    task_tuple = (
        task_data["name"],
        task_data["summary"],
        task_data["description"],
        task_data["is_done"],
        task_id
    )
    statement = """
        UPDATE tasks
        SET 
            name = ?,
            summary = ?,
            description = ?,
            is_done = ?
        WHERE id = ?
    """
    conn = get_db()
    conn = conn.execute(statement, task_tuple)
    conn.commit()

#? Delete a task by id
def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id = ?", (task_id, )) #! Comma
    conn.commit()