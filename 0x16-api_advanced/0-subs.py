#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
        for a given subreddit
    If an invalid subreddit is given, the function should return 0
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers,
                            allow_redirects=False).json()
    subscribers = response.get('data', {}).get('subscribers')

    if not subscribers:
        return 0
    return subscribers
