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

def get_connection_info():
    connection_info = {}
    connection_info['username'] = get_username()
    connection_info['password'] = get_password()
    connection_info['host'] = get_host_ip_address()
    return connection_info

def main():
    """ function """
    user_input = get_connection_info()
    url = f"https://{user_input['host']}:443/restconf/data/Cisco-IOS-XE-native:native/interface"
    while True:
        menu_input = menu()
        if menu_input == "1":
            get_response = http_get(url + "/Loopback=1000", user_input['username'], user_input['password'], headers)
            print(get_response)
            print(get_response.text)
        elif menu_input == "2":
            my_addr = get_ip_address_and_mask()
            interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['address'] = my_addr[0]
            interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['mask'] = my_addr[1]
            print(http_post(url, user_input['username'], user_input['password'], headers, json.dumps(interface_config)))
        elif menu_input == "3":
            print(http_delete(url + "/Loopback=1000", user_input['username'], user_input['password'], headers))

if __name__ == '__main__':
    main()
