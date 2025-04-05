#!/usr/bin/python3


"""
Documentation
Fetches data from the url using
the urllib module in python.
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            x_request_id = response.headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL.")
        print("Reason:", e.reason)

if __name__ == "__main__":
    fetch_x_request_id(sys.argv[1])
