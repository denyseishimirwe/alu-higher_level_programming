#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response
curl -s "$1" | awk '{print "GET / => \"" $0 "\""}'
