#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status and
display header"""
import requests
from sys import argv

if __name__ == "__main__":
    # gets the variables
    url = argv[1]
    post_data = {'email': argv[2]}
    # returns an object from post request
    response = requests.post(url, data=post_data)
    # print the content
    print(content.text)
