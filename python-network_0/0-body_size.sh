#!/bin/bash
# This script sends a GET request to the URL and prints the size of the response body in bytes
curl -s "$1" | wc -c
