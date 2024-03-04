#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}")
