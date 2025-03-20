#!/bin/bash
# Send GET request with the custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "http://$1"
