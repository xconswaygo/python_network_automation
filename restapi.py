#!/usr/bin/python3
""" docstring """
from library import *
import httpx
#import ipdb

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

get_access_points_url = "https://10.1.40.11:443/restconf/data/"\
                        "Cisco-IOS-XE-wireless-access-point-oper:access-point-oper-data/capwap-data"

get_access_points_url_params = {
    'fields': 'ip-addr;name;device-detail/static-info/board-data/wtp-enet-mac'
    }

def http_get(url, params, username, password):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.get(
            url, headers=headers, params=params, auth=(username, password)
            )
        return response

def main():
    """ function """
    username = get_username()
    password = get_password()
    http_host = get_host_ip_address()
    response = http_get(get_access_points_url, get_access_points_url_params, username, password)
    print(response)
    #ipdb.set_trace()

if __name__ == '__main__':
    main()
