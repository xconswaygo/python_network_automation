from getpass import getpass
import ipaddress, macaddress


def get_username():
    username_input = str(input('enter in username\n> '))
    while len(str(username_input.strip())) == 0:
        print('invalid')
        username_input = str(input('enter in username\n> '))
    return str(username_input)


def get_password():
    password_input = str(getpass('enter in password\n> '))
    while len(str(password_input)) == 0:
        print('invalid')
        password_input = str(getpass('enter in password\n> '))
    return str(password_input)


def get_host_ip_address():
    while True:
        try:
            ip_address = ipaddress.ip_address(input('enter in an ipv4 address\n> '))
        except ValueError:
            print('invalid')
            continue
        else:
            return str(ip_address)


def get_ip_address_and_mask():
    while True:
        try:
            user_input = ipaddress.IPv4Interface(input('enter in an ipv4 address and mask\n> ')).with_netmask
        except ValueError:
            print('invalid')
            continue
        else:
            return str(user_input.split('/')[0]),str(user_input.split('/')[1])


def get_host_mac_address():
    while True:
        try:
            mac_address = macaddress.MAC(input('enter in a MAC address\n> '))
        except ValueError:
            print('invalid')
            continue
        else:
            return str(mac_address).replace('-', ':')
