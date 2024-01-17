#!/usr/bin/python3
import requests
"""Module for task 0"""

def number_of_subscribers(subreddit):
    '''
    A function that queries the Reddit API and returns the number of subscribers,
    0 if the subreddit is not valid.
    '''
    headers = {'User-Agent': 'MyAPIReddit'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        sub_data = res.json().get('data', {})
        return sub_data.get('subscribers', 0)
    else:
        return 0