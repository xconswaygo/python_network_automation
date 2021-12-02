#!/usr/bin/python3
""" docstring """
from library import *
import httpx
#import ipdb

get_traffic_stats_url_params = {
    'fields': 'mobility-history/entry'
    }

def http_get(url, username, password, params=''):
    """ function """
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
        }
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
    client_mac_address = get_host_mac_address()
    base_url = f"https://{http_host}:443/restconf/data/"
    get_client_history_url = f"Cisco-IOS-XE-wireless-client-oper:client-oper-data/mm-if-client-history={str(client_mac_address).replace('-', ':')}"
    traffic_stats_response = http_get(base_url + get_client_history_url, username, password, get_traffic_stats_url_params)
    if str(traffic_stats_response) == "<Response [200 OK]>":
        print(traffic_stats_response.text)
    elif str(traffic_stats_response) == "<Response [401 Unauthorized]>":
        print("unauthorized")
    elif str(traffic_stats_response) == "<Response [404 Not Found]>":
        print(traffic_stats_response)
        print("no client found")
    else:
        print(traffic_stats_response)
        print('error')

if __name__ == '__main__':
    main()
