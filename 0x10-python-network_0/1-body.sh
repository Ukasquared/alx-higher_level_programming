#!/bin/bash
#Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

if [ -z "$1" ]; then
	echo "Usage: "$0" <Url>"
	exit 1
fi

url="$1"
response=$(curl -s -i "$url")

# Extract the HTTP status code
http_status=$(echo "$response" | awk '/^HTTP/ {print $2}')

# Check if the status code is 200
if [ "$http_status" -eq 200 ]; then
    # Extract and display the response body
    response_body=$(echo "$response" | awk '/^$/{flag=1; next} {if (flag) print}')
    echo "$response_body"
fi
