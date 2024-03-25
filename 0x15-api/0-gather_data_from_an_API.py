#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":

    user_Id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_Id))

    name = user.json().get('name')

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in tasks.json():
        if task.get('userId') == int(user_Id):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in tasks.json()
          if task.get('userId') == int(user_Id) and task.get('completed')]))
