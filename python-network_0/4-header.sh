#!/bin/bash
# Script that sends a GET request with a custom header and displays the response body
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
