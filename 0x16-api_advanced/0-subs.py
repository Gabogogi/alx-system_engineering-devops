#!/usr/bin/python3
'''
Obtain number of subscribers from a Reddit subreddit
'''
import sys
import requests


subreddit = sys.argv[1]


def number_of_subscribers(subreddit):
    '''a function that queries the Reddit API
    and returns the number of subscribers, 0 if not valid '''
    headers = {'User-Agent': 'MyAPIReddit'}

    # end point for subreddit info
    res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about.json',
                       headers=headers)

   if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
