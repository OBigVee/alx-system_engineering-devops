#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about
his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    userId = int(argv[1])
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        ).json()
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
               userId)).json()

    user_todo_list = []
    for job_done in todo_list:
        if job_done['userId'] == userId:
            user_todo_list.append(job_done)

    #  get todo analytics
    todo_total = len(user_todo_list)
    todo_completed = sum(job_done['completed'] for job_done in user_todo_list)

    print('Employee {} is done with tasks({}/{}):'.format(
          user['name'], todo_completed, todo_total))
    cj = [job_done for job_done in user_todo_list if job_done['completed']]
    for job_done in cj:
        print('\t {}'.format(job_done['title']))
