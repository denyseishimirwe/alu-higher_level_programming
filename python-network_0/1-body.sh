#!/bin/bash
# Script that sends a GET request to URL and displays only the body if status code is 200
curl -s -L -w '%{http_code}' "$1" -o /dev/null 2>/dev/null | grep -q "200" && curl -s -L "$1"
