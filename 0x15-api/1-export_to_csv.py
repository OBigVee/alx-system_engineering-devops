#!/usr/bin/python3
""" extension of script in 0-gather_data_from_an_API.py.
This script export data in the CSV format"""

import sys
import requests

if __name__ == "__main__":
    employeeId = sys.argv[1]

    urlAddr = "https://jsonplaceholder.typicode.com/users/{}".format(employeeId)

    user = requests.get(urlAddr)
    toDos = requests.get("https://jsonplaceholder.typicode.com/todos")

    employeeUname = user.json().get("username")
    taskCompletedStatus = ""  # toDos.get("completed")
    # taskTitle =  #toDos.get("title")

    fileName = "{}.csv".format(employeeId)

    with open(fileName, "w") as file:
        [
            file.write(
                """\n "{}","{}","{}","{}"\n""".format(
                    employeeId,
                    jobDone.get("username"),
                    jobDone.get("completed"),
                    jobDone.get("title"),
                )
            )
            for jobDone in toDos.json()
            if jobDone.get("userId") == int(employeeId)
        ]
        # for jobDone in toDos.json():
        #     if jobDone.get("userId") == int(
        #         employeeId
        #     ):  # and jobDone.get("username") and jobDone.get():
        #         # taskTitle = jobDone.get("title")
        #         # if jobDone.get("completed") != False:
        #         #     taskCompletedStatus = True
        #         file.write(
        #             "\n {}, {}, {}, {}\n".format(
        #                 employeeId,
        #                 jobDone.get("username"),
        #                 jobDone.get("completed"),
        #                 jobDone.get("title"),
        #             )
        #         )
    # print(
    #     "\n {}, {}, {}, {}".format(
    #         employeeId, employeeName, taskCompletedStatus, taskTitle
    #     )
    # )
