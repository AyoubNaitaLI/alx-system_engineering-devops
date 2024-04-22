#!/usr/bin/python3
""" Gathering employees data from an API storing it in .json file"""


import json
import requests
import sys


if __name__ == '__main__':
    url_info = 'https://jsonplaceholder.typicode.com/users?id='
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    r_user = requests.get(url_info + sys.argv[1])
    username = r_user.json()[0].get("username")
    r_todos = requests.get(url_todos + sys.argv[1])
    data = {}
    task_l = []
    for task in r_todos.json():
        task_info = {}
        t_status = task.get("completed")
        title = task.get("title")
        task_info["task"] = title
        task_info["completed"] = t_status
        task_info["username"] = username
        task_l.append(task_info)
    data[sys.argv[1]] = task_l
    with open(sys.argv[1] + ".json", "w") as f:
        f.write(json.dumps(data))
