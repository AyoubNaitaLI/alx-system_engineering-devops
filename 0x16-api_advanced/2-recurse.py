#!/usr/bin/python3
""" Fetching subreddit childrens titles"""


import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """ Function that returns the list of all subreddit hot posts"""
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    query = f'?count={count}&after={after}'
    try:
        if count == 0 and after == "":
            url = endpoint
        else:
            url = endpoint + query
        r = requests.get(url, headers={"User-Agent": "ME"},
                         allow_redirects=False)
        childrens = r.json().get("data").get("children")
        for post in childrens:
            hot_list.append(post.get("data").get("title"))
        count = r.json().get("data").get("dist")
        after = r.json().get("data").get("after")
        if count != 0 and after is not None:
            return recurse(subreddit, hot_list=hot_list, count=count,
                           after=after)
        else:
            return hot_list
    except Exception:
        return None
