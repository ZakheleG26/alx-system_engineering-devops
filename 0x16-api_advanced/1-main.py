#!/usr/bin/python3

"""
1-main
"""
import sys

if __name__ == '__main__':
    try:
        top_ten = __import__('1-top_ten').top_ten
        if len(sys.argv) < 2:
            print("Please pass an argument for the subreddit to search.")
        else:
            top_ten(sys.argv[1])
    except Exception as e:
        print(f"An error occurred: {e}")
