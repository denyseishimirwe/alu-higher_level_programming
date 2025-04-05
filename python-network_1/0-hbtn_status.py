#!/usr/bin/python3


"""
Fetches the status from a given URL using urllib with authentication support.
"""
import urllib.request
import urllib.error


def fetch_status(url):
    """Fetches and prints the status from the given URL, handling errors."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "your_session_cookie_here"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error: HTTP Error", e.code)
    except urllib.error.URLError as e:
        print("Error: Unable to fetch the URL.")
        print("Reason:", e.reason)

if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")
