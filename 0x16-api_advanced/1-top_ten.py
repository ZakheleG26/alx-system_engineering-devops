#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
    Returns the top ten posts for a given subreddit.
    '''
    user_agent = {'User-Agent': 'MyRedditBot/1.0 by YourUsername'}
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    response = requests.get(url, headers=user_agent)

    try:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(argv) == 2:
        top_ten(argv[1])
    else:
        print("Usage: python script.py <subreddit>")
