#!/usr/bin/python3
'''
Obtain number of subscribers from a Reddit subreddit
'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''a function that queries the Reddit API
    and returns the number of subscribers, 0 if not valid '''
    headers = {'User-Agent': 'MyAPIReddit'}

    # end point for subreddit info
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0
    sub_data = res.json().get('data')
    return sub_data.get('subscribers')
