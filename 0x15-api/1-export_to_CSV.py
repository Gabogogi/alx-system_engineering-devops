#!/usr/bin/python3
'''extends Python script to export data in the CSV'''

import csv
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    user_response = requests.get(f"{url}users/{employee_id}")

    user = user_response.json()
    username = user.get("username")
    params = {"userId": employee_id}
    todo_response = requests.get(f"{url}todos", params=params)
    todos = todo_response.json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([employee_id, username, todo.get("completed"),
                            todo.get("title")])
