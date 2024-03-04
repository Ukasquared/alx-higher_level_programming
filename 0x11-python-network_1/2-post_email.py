#!/usr/bin/python3
""" sents am email to a url"""
from urllib import request, parse
from sys import argv

def post_email():
    """ post and email to a url"""
    email = argv[2]
    parsed_data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(argv[1], data=parsed_data) as response:
        content = response.read().decode('utf-8')
        print(content)

if __name__ == "__main__":
    post_email()
