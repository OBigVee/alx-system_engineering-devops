#!/usr/bin/python3


import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[1]
    addressWithId = "https://jsonplaceholder.typicode.com/users/{}".format(employeeId)
    user = requests.get(addressWithId)

    employeeName = user.json().get("name")
    print(employeeId)

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    nTaskDone = 0
    totalNumberOfTasks = 0

    for jobDone in todos.json():
        if jobDone.get("employeeId") == int(employeeId):
            totalNumberOfTasks += 1
            if jobDone.get("completed"):
                nTaskDone += 1

    print(
        "Employee {} is done with task({}/{})".format(
            employeeName, nTaskDone, totalNumberOfTasks
        )
    )

    print(
        "\n".join(
            [
                "\t " + jobDone.get("title")
                for jobDone in todos.json()
                if jobDone.get("employeeId") == int(employeeId)
                and jobDone.get(nTaskDone)
            ]
        )
    )
    # print("\n".join(["\t" + jobDone.get('title') for jobDone]))
