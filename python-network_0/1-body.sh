#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response
curl -sL "$1" -o /dev/null -w "%{http_code}" | grep -q "^200$" && curl -sL "$1"
