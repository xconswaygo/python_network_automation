#!/usr/bin/python3
""" docstring """
from library import *
import httpx, json
#import ipdb

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

def http_post(url, username, password, body):
    """ function """
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
        }
    with httpx.Client(verify=False) as http_client:
        response = http_client.post(url, headers=headers, data=body, auth=(username, password))
        return response

def main():
    """ function """
    username = get_username()
    password = get_password()
    http_host = get_host_ip_address()
    url = f"https://{http_host}:443/restconf/data/Cisco-IOS-XE-native:native/interface"
    post_loopback_interface_response = http_post(url, username, password, json.dumps(loopback_interface),)
    print(post_loopback_interface_response)
    if str(post_loopback_interface_response) == "<Response [201 Create]>":
        print("success")
    elif str(post_loopback_interface_response) == "<Response [401 Unauthorized]>":
        print("unauthorized")
    elif str(post_loopback_interface_response) == "<Response [409 Conflict]>":
        print("resource already exists")
    else:
        print('error')

if __name__ == '__main__':
    main()
