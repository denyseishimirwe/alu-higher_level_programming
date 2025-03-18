#!/bin/bash
# This script sends a GET request to the URL and handles redirections up to 5 times, displaying the body if status is 200
response=$(curl -Ls -w "%{http_code}" -o response_body.txt "$1"); [ "${response: -3}" -eq 200 ] && cat response_body.txt || (curl -s -I "$1" | grep -i Location && exit 0)
