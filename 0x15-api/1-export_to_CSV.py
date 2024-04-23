#!/usr/bin/python3
""" Gathering employees data from an API """


import requests
import sys


if __name__ == '__main__':
    url_info = 'https://jsonplaceholder.typicode.com/users?id='
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId='
    r_user = requests.get(url_info + sys.argv[1])
    username = r_user.json()[0].get("username")
    r_todos = requests.get(url_todos + sys.argv[1])
    with open(sys.argv[1] + ".csv", "a") as f:
        for task in r_todos.json():
            id = sys.argv[1]
            t_status = task.get("completed")
            title = task.get("title")
            line = f"\"{id}\",\"{username}\",\"{t_status}\",\"{title}\"\n"
            f.write(line)
