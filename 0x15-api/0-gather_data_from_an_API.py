#!/usr/bin/python3
"""Script that returns information about
TODO list progress for a given employee ID"""
import requests
import sys


if len(sys.argv) == 2:
    try:
        id = int(sys.argv[1])
        list_tasks = []
        total_tasks = 0
        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url).json()
        for todo in response:
            if todo['userId'] == id:
                total_tasks += 1
                if todo['completed'] is True:
                    list_tasks.append("\t " + todo['title'])
        url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
        employee = requests.get(url).json()
        print("Employee {} is done with tasks({}/{}):".format(
            employee['name'], len(list_tasks), total_tasks))
        print("\n".join(list_tasks))
    except Exception:
        exit()
