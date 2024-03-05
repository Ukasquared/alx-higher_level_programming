#!/usr/bin/python3

""" github API authentication """
from sys import argv
import requests

if __name__ == "__main__":
    name = argv[1]
    PAT = argv[2]
    h_data = {"Authorization": PAT}
    response = requests.get(f"https://api.github.com/{name}", headers = h_data)
    print(response.headers.get('id'))
