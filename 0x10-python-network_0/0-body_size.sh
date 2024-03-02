#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# check if the argument is empty
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit
fi

# if the first argument is true store the url
url = "$1"

# obtain the byte of the body of response in a variable
response = $(curl -s -o dev/null -w "%{size_download}" "$url"})

# print response if curl was succesful
if [$? -ne 0 ]; then
	echo "$response"
fi
