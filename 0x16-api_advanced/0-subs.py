#!/usr/bin/python3

"""function queries reddit API and then returns the number of
subscribers(not active users, total subscribers)
for a given subreddit forum
"""
import requests


def number_of_subscribers(subreddit):
    """function returns no of subreddit subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    r = requests.get(
        url=url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
    )
    if r.status_code >= 300:
        return 0

    return r.json().get("data").get("subscribers")
