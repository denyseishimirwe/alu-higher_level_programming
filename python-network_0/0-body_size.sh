#!/bin/bash
# This script sends a GET request to a URL and displays the response body
curl -sL "$1" | sed -n '1p'
