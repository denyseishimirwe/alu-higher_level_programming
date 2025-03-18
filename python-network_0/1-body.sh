#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response only if the status code is 200 (no redirection)
curl -s -o response_body.txt -w "%{http_code}" "$1" | grep -q "200" && cat response_body.txt
