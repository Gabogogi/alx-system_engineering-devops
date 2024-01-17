#!/usr/bin/python3
import requests
"""Module for task 0"""

def number_of_subscribers(subreddit):
    '''
    A function that queries the Reddit API and returns the number of subscribers,
    0 if the subreddit is not valid.
    '''
    headers = {'User-Agent': 'MyAPIReddit'}
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)