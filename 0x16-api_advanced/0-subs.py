#!/usr/bin/python3
""" Fetching information from subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Function that returns the number of subscribers of a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        r = requests.get(url, headers={"User-Agent": "Me"},
                         allow_redirects=False)
        return r.json().get("data").get("subscribers")
    except Exception:
        return 0
