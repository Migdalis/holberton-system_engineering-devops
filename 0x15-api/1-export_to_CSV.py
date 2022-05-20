#!/usr/bin/python3
"""Script that returns information about
TODO list progress for a given employee ID"""
import requests
import sys


if len(sys.argv) == 2:
    try:
        id = int(sys.argv[1])
        filename = sys.argv[1] + ".csv"
        list_tasks = []
        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url).json()
        for todo in response:
            if todo.get('userId') == id:
                list_tasks.append(todo)
        url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
        employee = requests.get(url).json()
        with open(filename, 'w') as file:
            for task in list_tasks:
                row = '\"{}\",\"{}\",\"{}\",\"{}\"\n'.format(
                    str(id), employee.get('username'),
                    str(task.get('completed')), task.get('title'))
                file.write(row)
    except Exception:
        exit()
