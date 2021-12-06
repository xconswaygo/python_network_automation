#!/usr/bin/python3
""" docstring """
from library import *
import httpx, json
#import ipdb

interface_config = {
        f"Cisco-IOS-XE-native:Loopback": {
            "name": 1000,
            "ip": {
                "address": {
                    "primary": {
                        "address": None,
                        "mask": None
                    }
                }
            }
        }
    }

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

def menu():
    return str(input("""
please select option:
  [1]  show Loopback1000
  [2]  create interface Loopback1000
  [3]  delete interface Loopback1000
> """))

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
            my_addr = get_ip_address_and_mask()
            interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['address'] = my_addr[0]
            interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['mask'] = my_addr[1]
            print(http_post(url, username, password, json.dumps(interface_config)))
        elif user_input == "3":
            print(http_delete(url + "/Loopback=1000", username, password))

if __name__ == '__main__':
    main()
