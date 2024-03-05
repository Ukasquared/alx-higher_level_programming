#!/usr/bin/python3
""" urllib module """
from urllib import request


def request_response():
    """ http request """
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        decode_content = content.decode('utf-8')
        print(f"Body response:\n\t- type: {type(content)}\n\t\
- content: {content}\n\t- utf8 content: {decode_content}")

if __name__ == "__main__":
    request_response()
