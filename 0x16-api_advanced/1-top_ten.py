#!/usr/bin/python3
"""function queries the Reddit API and prints the titles
of the first 10 hot posts listed for a give subreddit"""

import requests


def top_ten(subreddit):
    """function queries subreddit and prints titles
    of first 10 post"""

    url = f"https://www.reddit.com/r/{subreddit}.json"
    COUNT = 10
    list_of_post = []

    r = requests.get(
        url=url, headers={"User-Agent": "My_User_Agent"}, allow_redirects=False
    )
    if r.status_code >= 300:
        print(None)
    else:
        for post in r.json().get("data").get("children"):
            COUNT -= 1
            if COUNT >= 0:
                list_of_post.append(post.get("data").get("title"))
    for post in list_of_post:
        print(post)