#!/usr/bin/python3
""" The Gather Data From An API Module """
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    API endpoint
    """
    api_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            todos = response.json()

            # Filter completed tasks
            completed_tasks = [task for task in todos if task['completed']]

            # Display employee TODO list progress
            print(f"Employee {todos[0]['userId']} is done with tasks ({len(completed_tasks)}/{len(todos)}):")

            # Display titles of completed tasks
            for task in completed_tasks:
                print(f"\t{task['title']}")
        else:
            # Display an error message if the request was not successful
            print(f"Error: Unable to fetch data. Status code:{response.status_code}")

    except requests.ConnectionError:
        # Display an error message for connection issues
        print("Error: Unable to connect to the API.")


if __name__ == "__main__":
    """
    Check if an employee ID is provided as a command-line argument
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        # Get the employee ID from the command-line argument
        employee_id = int(sys.argv[1])

        # Call the function to get and display employee TODO list progress
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Please provide a valid integer for the employee ID.")
