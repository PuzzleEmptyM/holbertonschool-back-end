#!/usr/bin/python3
"""
Gather Data From An API Module
"""

import requests
import sys


def get_user_info(employee_id):
    """
    Retrieve user information from the API.
    """
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise requests.RequestException(f"Error: Unable to fetch user data. Status code: {response.status_code}")


def get_employee_todo_progress(employee_id):
    """
    API endpoint
    """
    try:
        # Retrieve user data to get the employee name
        user_info = get_user_info(employee_id)
        employee_name = user_info.get('name', f"User {employee_id}")

        # Make a GET request to the API for TODO list
        api_url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        response_todos = requests.get(api_url_todos)

        if response_todos.status_code == 200:
            # Convert the response to JSON format
            todos = response_todos.json()

            # Filter completed tasks
            completed_tasks = [task for task in todos if task['completed']]

            # Display employee TODO list progress
            print(
                f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(todos)}):")

            # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")
        else:
            # Display an error message if the request for TODO list was not successful
            print(
                f"Error: Unable to fetch TODO list data. Status code: {response_todos.status_code}")

    except requests.RequestException as e:
        # Handle API request exceptions
        print(f"Error: {e}")

    except ValueError:
        # Handle invalid employee ID
        print("Error: Please provide a valid integer for the employee ID.")

if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(f'Unexpected error: {e}')
        exit(1)
