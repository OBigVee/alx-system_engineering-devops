#!/usr/bin/python3
""" xtension of script in 0-gather_data_from_an_API.py.
This script export data in the JSON forma"""


import json
import requests
import sys

if __name__ == "__main__":
    

    urlAddr = "https://jsonplaceholder.typicode.com/users"

    users = requests.get(urlAddr).json()
    toDos = requests.get("https://jsonplaceholder.typicode.com/todos")

    #employeeUname = users.get("username")

    fileName = "todo_all_employees.json"

    
    track_all = {}
    track_username = {}
    caches = []
    for user in users:
        employeeXId = user.get("id") 
        track_all[employeeXId] = []
        track_username[employeeXId] = user.get("username")
        #caches.append(track_username)
        #track_all[]
    #print(type(track_all))
    for jobDone in toDos.json():
        todo_task_caches = {}
        taskId = jobDone.get("userId")
        todo_task_caches["username"] = track_username.get(taskId)
        todo_task_caches["task"] = jobDone.get("title")
        todo_task_caches["completed"] = jobDone.get("completed")
        track_all.get(taskId).append(todo_task_caches)
        
  
    with open(fileName, "w") as file:
        json.dump(track_all, file)
    

    # for jobDone in toDos.json():
    #    todo_task_caches = {}
    #    todo_task_caches["username"] = users.get("username")
    #    todo_task_caches["task"] = jobDone.get("title")
    #    todo_task_caches["completed"] = jobDone.get("completed")
    #     caches.appendtodo_task_caches)
    # json_file = {}
    # json_file[employeeId] = caches
    
