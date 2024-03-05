#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status and
display header"""
import requests
from sys import argv

if __name__ == "__main__":
    # gets the variables
    url = argv[1]
    try:
        response = requests.get(url)
        # get the status code
        reponse_code = response.status_code
        # check if response code is equal or greater than 400
        if (response_code >= 400):
            print(f"Error code: {response_code}")
        else:
            print(response.text)
    except requests.ConnectionError as e:
        print(e)
