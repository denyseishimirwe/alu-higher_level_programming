#!/bin/bash
# Script that sends a GET request with a custom header and displays the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
