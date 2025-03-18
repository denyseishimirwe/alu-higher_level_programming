#!/bin/bash
# This script sends a GET request to the URL, follows redirections, and displays the body of the response for a 200 status code
curl -Ls "$1" -w "%{http_code}" -o response_body.txt | grep -q "200" && cat response_body.txt
