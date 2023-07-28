#!/usr/bin/python3
"""
Using  task #0, extend your Python script to
export data in the JSON format.
Requirements:

Records all tasks that are owned by this employee
Format must be: {
    "USER_ID": [
        {
            "task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
        {
            "task":"TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": "USERNAME"
        },
          ... ]
        }
File name must be: USER_ID.json
"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    userId = int(sys.argv[1])
    filename = str(userId) + ".json"

    todo_ = "https://jsonplaceholder.typicode.com/todos"
    user_ = f"https://jsonplaceholder.typicode.com/users?id={userId}"

    todo_list_url = requests.get(todo_).json()
    user_url = requests.get(user_).json()

    name = user_url[0]["name"]
    username = user_url[0]["username"]

    user_todo_list = []
    for job_done in todo_list_url:
        if job_done["userId"] == userId:
            user_todo_list.append(job_done)

    tasks_list = []
    # write to json
    with open(filename, "w", encoding="utf-8") as json_file:
        for user_analytic in user_todo_list:
            # writer.writeheader()
            data = {
                        "task": user_analytic["title"],
                        "completed": user_analytic["completed"],
                        "username": username,
                }
            tasks_list.append(data)

        data = {userId: tasks_list}
        json.dump(data, json_file)
