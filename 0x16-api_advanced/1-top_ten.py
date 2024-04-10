#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers,
                            params={'limit': '10'}, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
