#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# obtain the byte of the body of response in a variable
response=$(curl -s -o dev/null -w "%{size_download}" "$1")

# print response if curl was succesful
echo "$response"
