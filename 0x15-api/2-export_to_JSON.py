#!/usr/bin/python3
""" xtension of script in 0-gather_data_from_an_API.py.
This script export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]

    urlAddr = "https://jsonplaceholder.typicode.com/users/{}".format(
        employeeId
        )

    user = requests.get(urlAddr).json()
    toDos = requests.get("https://jsonplaceholder.typicode.com/todos")

    employeeUname = user.get("username")

    fileName = "{}.json".format(employeeId)

    caches = []
    for jobDone in toDos.json():
        task_caches = {}
        if jobDone.get("userId") == int(employeeId):
            task_caches["task"] = jobDone.get("title")
            task_caches["completed"] = jobDone.get("completed")
            task_caches["username"] = user.get("username")
            caches.append(task_caches)

    json_file = {}
    json_file[employeeId] = caches
    with open(fileName, "w") as file:
        json.dump(json_file, file)
