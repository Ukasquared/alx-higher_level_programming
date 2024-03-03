#!/usr/bin/python3
""" print the value of the header in a http response"""
from urllib import request
from sys import argv

def request_header():
    """ prints the header value"""
    with request.urlopen(argv[1]) as response:
        get_hvalue = response.getheader('X-Request-Id')
        print(get_hvalue)

if __name__ == "__main__":
    request_header()
