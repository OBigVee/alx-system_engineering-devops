#!/usr/bin/python3
"""extension of task #0 python script to export data in the CSV format
- Records all tasks that are owned by this employee
- Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name must be: USER_ID.csv
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    userId = int(argv[1])
    filename = str(userId) + ".csv"
    todo_list = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    ).json()
    name = user["name"]
    username = user["username"]

    user_todo_list = []
    for job_done in todo_list:
        if job_done["userId"] == userId:
            user_todo_list.append(job_done)

    with open(filename, "w", encoding="utf-8") as csv_file:
        for user_analytic in user_todo_list:
            # writer.writeheader()
            csv_file.write("{},{},{},{}\n".format(
                userId, username,
                user_analytic['completed'], user_analytic['title']
            ))
