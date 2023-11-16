#!/usr/bin/python3
"""
Gather Data From An API Module
"""

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
    todo_data = requests.get(todo_url,
                             params={"userId": employee_id}).json()

    employee_name = employee_data.get("name")
    completed_tasks = [t["title"] for t in todo_data if t["completed"]]
    number_done = len(completed_tasks)
    number_total = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_done, number_total))
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":

    get_employee_todo_progress(int(sys.argv[1]))
