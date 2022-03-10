#!/usr/bin/python3
""" script uses this REST API(https://jsonplaceholder.typicode.com/) for a given employee ID,
returns information about his/her Todo list progress.
"""

import json
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    urlAddr = "https://jsonplaceholder.typicode.com/users/{}".format(employeeId)
    user = requests.get(urlAddr)

    employeeName = user.json().get("name")

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    nTaskDone = 0
    totalNumberOfTasks = 0

    for jobDone in todos.json():
        if jobDone.get("userId") == int(employeeId):
            totalNumberOfTasks += 1
            if jobDone.get("completed"):
                nTaskDone += 1

    print(
        "Employee {} is done with task({}/{})".format(
            employeeName, nTaskDone, totalNumberOfTasks
        )
    )

    for jobDone in todos.json():
        if jobDone.get("userId") == int(employeeId) and jobDone.get("completed"):
            print("".join("\t " + jobDone.get("title")))
        else:
            "NO oo!"

"""LIST  COMPREHENSION METHOD
table = "\n".join(
        [
            "\t" + jobDone.get("title")
            for jobDone in todos.json()
            if jobDone.get("userId") == int(employeeId) and jobDone.get("completed")

        ]
    )
    print(table)"""
