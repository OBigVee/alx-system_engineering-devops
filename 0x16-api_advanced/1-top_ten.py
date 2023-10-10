#!/usr/bin/python3
"""function queries the Reddit API and then prints the titles
of the first 10 hot posts listed for a give subreddit"""

import requests


def top_ten(subreddit):
    """function queries subreddit and prints titles
    of first 10 post"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    COUNT = 10

    r = requests.get(
        url=url, headers={"User-Agent": "My_User_Agent"}, allow_redirects=False
    )
    if r.status_code < 300:
        posts = [
            post["data"]["title"]
            for post in r.json().get("data").get("children", [])
            [:COUNT]
            ]
        for post in posts:
            print(post)
    else:
        print(None)
