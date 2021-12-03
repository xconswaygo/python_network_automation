#!/usr/bin/python3
""" docstring """
from library import *
import httpx, json
#import ipdb

get_client_history_url_params = {
    'fields': 'mobility-history/entry'
    }

def http_get(url, username, password, params=''):
    """ function """
    headers = {
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json',
        }
    with httpx.Client(verify=False) as http_client:
        response = http_client.get(url, headers=headers, params=params, auth=(username, password))
        return response

def main():
    """ function """
    username = get_username()
    password = get_password()
    http_host = get_host_ip_address()
    client_mac_address = get_host_mac_address()
    base_url = f"https://{http_host}:443/restconf/data/"
    get_traffic_stats_url = f"Cisco-IOS-XE-wireless-client-oper:client-oper-data/traffic-stats={client_mac_address}"
    traffic_stats_response = http_get(base_url + get_traffic_stats_url, username, password,)
    if str(traffic_stats_response) == "<Response [200 OK]>":
        traffic_stats = json.loads(traffic_stats_response.text)['Cisco-IOS-XE-wireless-client-oper:traffic-stats']
        retry_rate = int(traffic_stats['data-retries']) / int(traffic_stats['pkts-tx'])
        print("Retries: {:.2%}".format(retry_rate))
        print(f"Data Rate: {traffic_stats['speed']} Mbps")
        print(f"SNR: {traffic_stats['most-recent-snr']} dB")
    elif str(traffic_stats_response) == "<Response [401 Unauthorized]>":
        print("unauthorized")
    elif str(traffic_stats_response) == "<Response [404 Not Found]>":
        print("no client found")
    else:
        print('error')

if __name__ == '__main__':
    main()
