#!/usr/bin/python3
'''extends Python script to export data in the JSON for all emp'''

import json
import requests


def get_user_data():
    '''get data for all users'''
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(f"{url}users").json()

    data_to_export = {}

    for user in users:
        user_id = user["id"]

        todo_response = requests.get(url + f"todos?userId={user_id}")

        todo_list = todo_response.json()

        data_to_export[user_id] = []

        for todo in todo_list:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            data_to_export[user_id].append(task_info)
        return data_to_export


if __name__ == "__main__":
    data_to_export = get_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
