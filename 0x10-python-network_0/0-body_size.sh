#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# if the first argument is true store the url
url="$1"

# obtain the byte of the body of response in a variable
response=$(curl -s -o dev/null -w "%{size_download}" "$url")

# print response if curl was succesful
echo "$response"
