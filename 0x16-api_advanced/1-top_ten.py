#!/usr/bin/python3
'''
Obtain top 10 posts for a Reddit subreddit
'''
import requests
import sys


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts
    listed for a given subreddit. '''
    headers = {'User-Agent': 'MyAPIReddit'}

    params = {
        'limit' : 10
    }

    # end point for subreddit info
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        print('None')
    else:
        sub_data = res.json()
        top_posts = sub_data['data']['children']
        if len(top_posts) == 0:
            print(None)
        else:
            for post in top_posts:
                print(post['data']['title'])


top_ten('python')
# print(top_ten('ben'))