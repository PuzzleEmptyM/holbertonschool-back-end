#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import json
import requests


def get_all_employees_todo_progress():
    """
    API endpoint
    """
    url = "https://jsonplaceholder.typicode.com"
    users_url = f"{url}/users"
    todos_url = f"{url}/todos"

    all_employees_data = []

    users_data = requests.get(users_url).json()

    for user in users_data:
        employee_id = user["id"]
        employee_name = user["username"]

        todo_data = requests.get(todos_url,
                                 params={"userId": employee_id}).json()
        tasks = []
        for task in todo_data:
            tasks.append({
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
            })

        all_employees_data.append({str(employee_id): tasks})

    json_file_path = "todo_all_employees.json"

    with open(json_file_path, mode='w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)


if __name__ == "__main__":
    get_all_employees_todo_progress()
