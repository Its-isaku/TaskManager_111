
#? Libriaries
import requests

#? URL of the API tp create a task
URL = "http://127.0.0.1:5000/tasks" #* URL of the API

#? Function to create a task    
def create_task(name, summary, description):
    
    #* Create a dictionary with the task data
    task_data = {
    "name": name,
    "summary": summary,
    "description": description
    }
    
    #* Send a POST request to the API
    response = requests.post(URL, json=task_data) 
    if response.status_code == 204:
        print("Task created successfully")
    else: 
        print(f"Error creating task")
        
#? ca;ll the function to create a task
if __name__ == "__main__":
    
    #* Prompt the user for task data
    print("Create a new task by filling the prompts below: ")
    name = input("Task name: ")
    summary = input("Task summary: ")
    description = input("Task description: ")
    create_task(name, summary, description)