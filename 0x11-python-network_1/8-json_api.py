#!/usr/bin/python3

""" search API """
import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(argv) > 1:
        q = argv[1]
    new_data = {'q': q}
    try:
        response = requests.post(url, data=new_data)
        json_text = response.json()
        if not json_text:
            print("No result")
        else:
            print("[{}] {}".format(json_text['id'], json_text['name']))
    except ValueError:
        print("not a valid JSON")
