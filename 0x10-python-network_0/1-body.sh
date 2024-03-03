#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the bodyresponse
curl -s "$1"|grep "HTTP\/1.1 200" | sed -n "2p"
