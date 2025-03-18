#!/bin/bash
# Script that sends a GET request to URL and displays only the body if status code is 200
curl -s -I "$1" | grep "HTTP/" | grep -q "200 OK" && curl -s "$1"
