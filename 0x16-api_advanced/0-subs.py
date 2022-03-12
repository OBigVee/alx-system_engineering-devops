#!/usr/bin/python3
""" function queries the Reddit API (https://www.reddit.com/dev/api/)
and returns the number of subcribers(not active users,total subcribers)
for a given subbreddit"""


import requests

# if __name__ == "__main__":


def number_of_subscribers(subreddit):
    """function returns the number subreddit
    subcribers.
    subreddit: subreddit url path

    return 0 if subreddit not a valid subreddit
    """

    sub_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    get_subs_n = requests.get(
        sub_url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
    )

    # check status_code
    if get_subs_n.status_code >= 300:
        return 0
    else:
        return get_subs_n.json().get("data").get("subscribers")
