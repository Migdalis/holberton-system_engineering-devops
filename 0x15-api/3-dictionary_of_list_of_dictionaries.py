#!/usr/bin/python3
"""Script that returns information about
TODO list progress for a given employee ID"""
import json
import requests


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/users"
    employees = requests.get(url).json()

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url).json()

    new_dict = {}
    with open(filename, 'w') as file:
        for employee in employees:
            list_tasks = []
            for todo in response:
                if todo.get('userId') == employee.get('id'):
                    dict_task = {}
                    dict_task['username'] = employee.get('username')
                    dict_task['task'] = todo.get('title')
                    dict_task['completed'] = todo.get('completed')
                    list_tasks.append(dict_task)
            new_dict[employee.get('id')] = list_tasks
        json.dump(new_dict, file)
