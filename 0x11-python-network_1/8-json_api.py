#!/usr/bin/python3

""" search API """
import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if argv[2]:
        q = argv[2]
    new_data = {'q': q}
    response = requests.post(url, data=new_data)
    try:
        json_text = response.json()
        if not json_text:
            print("No result")
        else:
            print("[{}] {}".format(json_text['id'], json_text['name']))
    except Exception:
        print("not a valid JSON")
