from getpass import getpass
import ipaddress, macaddress, httpx

def get_username():
    """ function """
    username_input = str(input('enter in username\n> '))
    while len(str(username_input.strip())) == 0:
        print('invalid')
        username_input = str(input('enter in username\n> '))
    return str(username_input)

def get_password():
    """ function """
    password_input = str(getpass('enter in password\n> '))
    while len(str(password_input)) == 0:
        print('invalid')
        password_input = str(getpass('enter in password\n> '))
    return str(password_input)

def get_host_ip_address():
    """ function """
    while True:
        try:
            ip_address = ipaddress.ip_address(input('enter in an ipv4 address\n> '))
        except ValueError:
            print('invalid')
            continue
        else:
            return str(ip_address)

def get_ip_address_and_mask():
    """ function """
    while True:
        try:
            user_input = ipaddress.IPv4Interface(input('enter in an ipv4 address and mask\n> ')).with_netmask
        except ValueError:
            print('invalid')
            continue
        else:
            return str(user_input.split('/')[0]),str(user_input.split('/')[1])

def get_host_mac_address():
    """ function """
    while True:
        try:
            mac_address = macaddress.MAC(input('enter in a MAC address\n> '))
        except ValueError:
            print('invalid')
            continue
        else:
            return str(mac_address).replace('-', ':')

def http_get(url, username, password, headers, params=''):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.get(url, headers=headers, params=params, auth=(username, password))
        return response

def http_post(url, username, password, headers, body):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.post(url, headers=headers, data=body, auth=(username, password))
        return response

def http_delete(url, username, password, headers):
    """ function """
    with httpx.Client(verify=False) as http_client:
        response = http_client.delete(url, headers=headers, auth=(username, password))
        return response