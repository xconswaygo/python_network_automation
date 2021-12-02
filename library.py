from getpass import getpass
import ipaddress, macaddress

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
            return ip_address

def get_host_mac_address():
    """ function """
    while True:
        try:
            mac_address = macaddress.MAC(input('enter in a MAC address\n> '))
        except ValueError:
            print('invalid')
            continue
        else:
            return mac_address.replace('-', ':')