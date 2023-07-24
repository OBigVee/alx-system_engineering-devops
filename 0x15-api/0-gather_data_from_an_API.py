#!/usr/bin/python3
"""script uses this REST API(https://jsonplaceholder.typicode.com/) for
a given employee ID,
returns information about his/her Todo list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(url)
    employee_name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    n_task_done = 0
    total_number_of_tasks = 0

    for job_done in todos.json():
        if job_done.get("userId") == int(employee_id):
            total_number_of_tasks += 1
            if job_done.get("completed"):
                n_task_done += 1
    print("Employee {} is done with task({}/{})".format(
        employee_name,
        n_task_done,
        total_number_of_tasks
        ))
    # print(
    # f"Employee {
    # employee_name
    # }is done with task({n_task_done}/{total_number_of_tasks})")

    for job_done in todos.json():
        if (
            job_done.get("userId") == int(employee_id)
            and job_done.get("completed")
        ):
            print("".join("\t" + job_done.get("title")))
        else:
            "No oo!"
