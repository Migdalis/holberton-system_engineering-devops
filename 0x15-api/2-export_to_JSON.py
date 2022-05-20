#!/usr/bin/python3
"""Script that returns information about
TODO list progress for a given employee ID"""
import json
import requests
import sys


if len(sys.argv) == 2:
    try:
        id = int(sys.argv[1])
        list_tasks = []
        filename = sys.argv[1] + ".json"
        url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
        employee = requests.get(url).json()

        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url).json()
        for todo in response:
            if todo['userId'] == id:
                dict_task = {}
                dict_task['task'] = todo.get('title')
                dict_task['completed'] = todo.get('completed')
                dict_task['username'] = employee.get('username')
                list_tasks.append(dict_task)
        new_dict = {}
        new_dict[sys.argv[1]] = list_tasks

        with open(filename, 'w') as file:
            json.dump(new_dict, file)
    except Exception:
        exit()
