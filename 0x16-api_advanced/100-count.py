#!/usr/bin/python3
""" Fetching and parsing subreddit childrens titles"""


import requests


def count_words(subreddit, word_list, keywords_count={}, count=0, after=""):
    """ Function that prints a sorted count of given keywords """
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
        if len(keywords_count) == 0:
            for i in range(len(word_list)):
                word_list[i] = word_list[i].lower()
            for word in list(set(word_list)):
                keywords_count[word] = 0
        for post in childrens:
            for word in word_list:
                if word.lower() in post.get("data").get("title").lower():
                    keywords_count[word] += 1
        count = r.json().get("data").get("dist")
        after = r.json().get("data").get("after")
        if count != 0 and after is not None:
            count_words(subreddit, word_list,
                        keywords_count=keywords_count, count=count,
                        after=after)
        else:
            for key, val in keywords_count.items():
                if val != 0:
                    print(f"{key}: {val}")
    except Exception as e:
        pass
