#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status and
display header"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        response = requests.get(url)
        content = response.headers.get('X-Request-Id')
        print(content)
    except requests.ConnectionError as e:
        print("",end="")
