from library import *
import json, httpx

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

def main():
    auth = (get_username(), get_password())
    host = get_host_ip_address()
    url = f"https://{host}:443/restconf/data/Cisco-IOS-XE-native:native/interface"
    with httpx.Client(verify=False, headers=headers, auth=auth, base_url=url) as http_client:
        while True:
            menu_input = str(input("please select option:\n  [1]  show Loopback1000\n  [2]  create interface Loopback1000\n  [3]  delete interface Loopback1000\n> "))
            if menu_input == "1":
                get_response = http_client.get(url='/Loopback=1000',)
                print(get_response)
                print(get_response.text)
            elif menu_input == "2":
                my_addr = get_ip_address_and_mask()
                interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['address'] = my_addr[0]
                interface_config['Cisco-IOS-XE-native:Loopback']['ip']['address']['primary']['mask'] = my_addr[1]
                data = json.dumps(interface_config)
                print(http_client.post(url='', data=data))
            elif menu_input == "3":
                print(http_client.delete(url='/Loopback=1000',))

if __name__ == '__main__':
    main()
