#!/usr/bin/python3
"""function queries Reddit API (https://www.reddit.com/dev/api/)
and prints the titles of the first 10 hot posts listed for
a given subreddit"""

import requests


def top_ten(subreddit):
    """function prints title of the first 10 hot posts

    subreddit:->String subreddit name
    print None if subreddit not valid
    """

    sub_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    sub_top_posts = requests.get(
        sub_url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
    )

    # check status code
    if sub_top_posts.status_code >= 300:
        print(None)
    else:
        [
            print(child.get("data").get("title"))
            for child in sub_top_posts.json().get("data").get("children")
        ]
