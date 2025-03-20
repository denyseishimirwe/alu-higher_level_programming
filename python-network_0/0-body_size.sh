#!/bin/bash
# This script sends a GET request and displays the content length of the response body
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
