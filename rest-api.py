#!/usr/bin/python3
""" docstring """
from library import *
import httpx, json
#import ipdb

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

loopback_interface = {
        "Cisco-IOS-XE-native:Loopback": {
            "name": 1000,
            "ip": {
                "address": {
                    "primary": {
                        "address": "192.168.1.1",
                        "mask": "255.255.255.0"
                    }
                }
            }
        }
    }

def menu():
    return str(input("""
please select option:
  [1]  show Loopback1000
  [2]  create interface Loopback1000
  [3]  delete interface Loopback1000
> """))

def http_get(url, username, password, params='',):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.get(url, headers=headers, params=params, auth=(username, password))
        return response

def http_post(url, username, password, body,):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.post(url, headers=headers, data=body, auth=(username, password))
        return response

def http_delete(url, username, password,):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.delete(url, headers=headers, auth=(username, password))
        return response

def main():
    """ function """
    username = get_username()
    password = get_password()
    http_host = get_host_ip_address()
    url = f"https://{http_host}:443/restconf/data/Cisco-IOS-XE-native:native/interface"
    while True:
        user_input = menu()
        if user_input == "1":
            get_response = http_get(url + "/Loopback=1000", username, password)
            print(get_response)
            print(get_response.text)
        elif user_input == "2":
            post_response = http_post(url, username, password, json.dumps(loopback_interface),)
            print(post_response)
        elif user_input == "3":
            delete_response = http_delete(url + "/Loopback=1000", username, password)
            print(delete_response)

if __name__ == '__main__':
    main()
