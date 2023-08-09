#!/usr/bin/python3
"""script queries Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
if no results are found for the given subreddit, the function
should return None"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """the function returns a list containing the titles of all
    hot articles for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}

    r = requests.get(
        url=url,
        headers={"User-Agent": "My_User_Agent"},
        allow_redirects=False,
        params=params,
    )

    if r.ok:
        data = r.json().get("data")
        if len(data.get("children")) != 0:
            # hot_list = [post.get("data") for post in data.get("children") ]
            for post in data.get("children"):
                hot_list.append(post.get("data"))
            after = data.get("after")

            if after is None:
                return hot_list
            return recurse(subreddit, hot_list=hot_list, after=after)
    return None
