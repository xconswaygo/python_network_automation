from library import *
import httpx, json

port = 443
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    }

def get_int_type(host, port, headers, auth):
    url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/interface"
    with httpx.Client(verify=False, headers=headers, auth=auth, base_url=url) as http_client:
        interface_types_params = {'depth': 1}
        response = json.loads(http_client.get(url='', params=interface_types_params).text)
        int_types_list = list(response['Cisco-IOS-XE-native:interface'].keys())
        i = list(range(100))
        int_types_dict = dict(zip(i,int_types_list))
        for k, v in int_types_dict.items():
            print(f"[{k}] - {v}")
        int_type = int_types_dict[int(input("\nselect interface type:\n> "))]
        return(int_type)

def get_int_num(host, port, headers, auth, interface_type):
    url = f"https://{host}:{port}/restconf/data/Cisco-IOS-XE-native:native/interface/{interface_type}"
    with httpx.Client(verify=False, headers=headers, auth=auth, base_url=url) as http_client:
        interface_num_params = {'fields': 'name'}
        response = json.loads(http_client.get(url='', params=interface_num_params).text)[f'Cisco-IOS-XE-native:{interface_type}']
        int_num_list = []
        for i in response:
            print(i['name'])
            int_num_list.append(f"{i['name']}")
        while True:
            user_input = input(f"\nenter in interface number\n> ")
            if user_input in int_num_list:
                return user_input
            else:
                continue

def main():
    #auth = (get_username(), get_password())
    #host = get_host_ip_address()
    auth = ('ejwilkerson', 'L0ck3r!291537')
    host = '10.1.40.11'
    interface_type = get_int_type(host, port, headers, auth)
    interface_number = get_int_num(host, port, headers, auth, interface_type)
    print(interface_type + interface_number)
        
if __name__ == '__main__':
    main()
