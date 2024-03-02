#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -s -i "$1")
http_status=$(curl -s -i $1 | awk '/^HTTP/ {print $2}')
response_body=$(echo "$response" | awk '/^$/{flag=1; next} {if (flag) print}')
    echo "$response_body"
