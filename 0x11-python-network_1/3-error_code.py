#!/usr/bin/python3
""" manages HTTPErrors"""
from urllib import request, error
from sys import argv

def manage_errors():
    """ manage http errors"""
    url = argv[1]
    try:
         with request.urlopen(url) as response:
             content = response.read().decode('utf-8')
             print(content)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    manage_errors()
