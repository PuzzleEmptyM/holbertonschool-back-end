#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import csv
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
    completed_tasks = [(t["completed"], t["title"]) for t in todo_data]

    csv_file_path = f"{employee_id}.csv"

    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for completed, task_title in completed_tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": completed,
                "TASK_TITLE": task_title
            })

    print("Number of tasks in CSV: OK")


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))
