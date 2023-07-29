#!/usr/bin/python3
"""
Using task #0, extend Python script to export data in the JSON format.
Requirements:

Records all tasks from all employees
Format must be:
{
    "USER_ID": [
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        },
        {
            "username": "USERNAME",
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS
        }
        ,
        ... ],
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            }
            , ... ]
        }
File name must be: todo_all_employees.json

if __name__ == "__main__":
    import requests
    import json

    filename = "todo_all_employees.json"

    id_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    todo_ = "https://jsonplaceholder.typicode.com/todos"
    todo_list_url = requests.get(todo_).json()
    user_todo_list = []

    for i in range (len(id_arr)):
        user_ = f"https://jsonplaceholder.typicode.com/users?id={id_arr[i]}"
        user_url = requests.get(user_).json()

        name = user_url[0]["name"]
        username = user_url[0]["username"]


        for job_done in todo_list_url:
            if job_done["userId"] == id_arr[i]:
                user_todo_list.append(job_done)

    tasks_list = []
    # write to json
    with open(filename, "w", encoding="utf-8") as json_file:
        for user_analytic in user_todo_list:

            print(f"stepping the loop one at a time {user_analytic}")
            print("\n")
                # writer.writeheader()
            data = {
                            "task": user_analytic["title"],
                            "completed": user_analytic["completed"],
                            "username": username,
                    }
            tasks_list.append(data)

        data = {id_arr[i]: tasks_list for i in range(len(id_arr))}
        json.dump(data, json_file, indent=4)
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    import json

    #  Fetch todos and user
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    users = get("https://jsonplaceholder.typicode.com/users").json()

    #  Compose data to be dumped in JSON file
    data = {}

    for user in users:
        #  Extract user specific todos
        userId = user["id"]
        user_todos = []
        for todo in todos:
            if todo["userId"] == userId:
                user_todos.append(todo)

        #  Create user data object
        tasks = []

        for todo in user_todos:
            obj = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            tasks.append(obj)

        data.update({userId: tasks})

    #  write data to a JSON file
    fname = "todo_all_employees.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f)
