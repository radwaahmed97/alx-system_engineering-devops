#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()
    tasksAll = {}

    for user in users:
        taskList = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        tasksAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(tasksAll, f)
