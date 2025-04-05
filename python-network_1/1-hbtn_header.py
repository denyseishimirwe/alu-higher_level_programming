#!/usr/bin/python3


"""
Fetches a URL and displays the value of the X-Request-Id variable in the response header.
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    """Fetches the URL and prints the X-Request-Id from the response headers, if present."""
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
