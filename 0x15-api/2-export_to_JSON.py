#!/usr/bin/python3
'''extends Python script to export data in the JSON'''

import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    user_response = requests.get(f"{url}users/{employee_id}").json()
    username = user_response.get("username")

    params = {"userId": employee_id}
    todo_response = requests.get(f"{url}todos", params=params)
    todos = todo_response.json()

    data_to_export = {employee_id: []}

    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        data_to_export[employee_id].append(task_info)
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
