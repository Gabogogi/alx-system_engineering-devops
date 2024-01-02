#!/usr/bin/python3
'''uses a REST API to return info on'''

import requests
import sys


if __name__ == '__main_':
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    user_response = requests.get(f"{url}users/{employee_id}")
    user = user_response.json()
    params = {"userId": employee_id}
    todo_response = requests.get(f"{url}todos", params=params)
    todos = todo_response.json()
    completed_tasks = []
    for todo in todos:
        if todo.get("completed") is True:
            completed_tasks.append(todo.get("title"))

    print(f"Employee {user.get('name')} is done with tasks \
          {len(completed_tasks)}/{len(todos)}")

    for complete in completed_tasks:
        print("\t {}".format(complete))
