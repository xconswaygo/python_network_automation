#!/usr/bin/python3
""" docstring """
from library import *
import httpx
#import ipdb

get_traffic_stats_url_params = {
    'fields': 'speed;most-recent-rssi;most-recent-snr;spatial-stream'
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
    get_traffic_stats_url = f"Cisco-IOS-XE-wireless-client-oper:client-oper-data/traffic-stats={str(client_mac_address).replace('-', ':')}"
    traffic_stats_response = http_get(base_url + get_traffic_stats_url, username, password, get_traffic_stats_url_params)
    print(traffic_stats_response.text)
    #ipdb.set_trace()

if __name__ == '__main__':
    main()
