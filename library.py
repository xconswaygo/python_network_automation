from getpass import getpass
import ipaddress

def get_username():
    """ function """
    username_input = str(input('enter in username\n> '))
    while len(str(username_input.strip())) == 0:
        username_input = str(input('enter in username\n> '))
    return str(username_input)

def get_password():
    """ function """
    password_input = str(getpass('enter in password\n> '))
    while len(str(password_input)) == 0:
        password_input = str(getpass('enter in password\n> '))
    return str(password_input)

def get_host_ip_address():
    """ function """
    while True:
        try:
            ip_address = ipaddress.ip_address(input('enter in an ipv4 address (x.x.x.x)\n> '))
        except ValueError:
            continue
        else:
            return ip_address