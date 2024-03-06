#!/usr/bin/python3

""" github API authentication """
from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    PAT = argv[2]
    h_data = {"Authorization": f"Bearer {PAT}"}
    # returns object
    link_param = f"https://api.github.com/{username}"
    response = requests.get(link_param,
                            headers=h_data)
    if (response.status_code >= 400):
        print("None")
    else:
        print(response.json()["id"])
