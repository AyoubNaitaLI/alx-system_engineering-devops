#!/usr/bin/python3
""" Listing the top 10 hot posts for a given subreddit """
import requests


def top_ten(subreddit):
    """ Function that list the top 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    try:
        r = requests.get(url, headers={"User-Agent": "Me"},
                         allow_redirects=False)
        children_list = r.json().get("data").get("children")
        for i in range(0, 10):
            print(children_list[i].get("data").get("title"))
    except Exception as e:
        print(e)
