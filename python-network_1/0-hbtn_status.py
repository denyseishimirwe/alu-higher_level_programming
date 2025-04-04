#!/usr/bin/python3


"""
Fetches the status from a given URL using urllib with error handling.
"""
import urllib.request
import urllib.error


def fetch_status(url):
    """Fetches and prints the status from the given URL, handling errors."""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode("utf-8"))
    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL.")
        print("Reason:", e.reason)

if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")
