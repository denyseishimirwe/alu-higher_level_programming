#!/bin/bash
# Script that sends a GET request to URL and displays only the body if status code is 200
curl -sL -o /tmp/curl_body -w "%{http_code}" "$1" | grep -q "200" && cat /tmp/curl_body
