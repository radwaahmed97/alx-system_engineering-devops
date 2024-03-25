#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":

    user_Id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_Id))
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()

    tasksUser = {}
    taskList = []

    for task in tasks:
        if task.get('userId') == int(user_Id):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    tasksUser[user_Id] = taskList

    filename = user_Id + '.json'
    with open(filename, mode='w') as f:
        json.dump(tasksUser, f)
