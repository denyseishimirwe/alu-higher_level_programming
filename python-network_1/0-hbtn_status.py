#!/usr/bin/python3

"""
Fetches the status from a given URL using urllib.
"""
import urllib.request


def fetch_status(url):
    """Fetches and prints the status from the given URL."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))

if __name__ == "__main__":
    fetch_status("http://0.0.0.0:5050/status")
