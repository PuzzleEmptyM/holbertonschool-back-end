#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    API endpoint
    """
    url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/todos"

    employee_data = requests.get(employee_url).json()
    todo_data = requests.get(todo_url, params={"userId": employee_id}).json()

    employee_name = employee_data.get("username")
    tasks = []

    for task in todo_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    json_file_path = f"{employee_id}.json"

    with open(json_file_path, mode='w') as json_file:
        json.dump({str(employee_id): tasks}, json_file, indent=2)


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
