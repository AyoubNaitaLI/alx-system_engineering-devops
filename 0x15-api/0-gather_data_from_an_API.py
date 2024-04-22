#!/usr/bin/python3
""" Gathering employees data from an API """


import requests
import sys


if __name__ == '__main__':
    url_info = 'https://jsonplaceholder.typicode.com/users?id='
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    r_user = requests.get(url_info + sys.argv[1])
    username = r_user.json()[0].get("name")
    r_todos = requests.get(url_todos + sys.argv[1])
    n_task = len(r_todos.json())
    done_t = 0
    for task in r_todos.json():
        if task.get("completed") is True:
            done_t += 1
    print(f'Employee {username} is done with tasks({done_t}/{n_task}):')
    for task in r_todos.json():
        if task.get("completed") is True:
            print(f"\t {task.get('title')}")
