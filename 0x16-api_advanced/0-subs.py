#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    URL = 'https://www.reddit.com/r/'
    res = requests.get('{}{}/about.json'.
                       format(URL, subreddit),
                       headers={'User-Agent': 'ALX-User-Agent'},
                       allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')
