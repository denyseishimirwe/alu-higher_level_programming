#!/usr/bin/python3


"""
Script that fetches https://intranet.hbtn.io/status or http://0.0.0.0:5050/status
and prints the body response with details.

Uses the urllib module and ensures proper output format.
"""
import urllib.request

def fetch_status(url):
    """Fetches the status of the given URL and prints its details."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    # Fetching from the given URL (can be updated or passed as an argument)
    fetch_status('https://intranet.hbtn.io/status')  # For https
    # Uncomment below line to test the other URL
    # fetch_status('http://0.0.0.0:5050/status')  # For local server
