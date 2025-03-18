#!/bin/bash
# This script sends a GET request to the URL and displays the size of the response body in bytes
curl -s "$1" | awk '{print length}'
