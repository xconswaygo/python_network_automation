from library import *
import ipdb

def get_connection_info():
    connection_info = {}
    connection_info['username'] = get_username()
    connection_info['password'] = get_password()
    connection_info['host'] = get_host_ip_address()
    return connection_info

def main():
    user = get_connection_info()
    ipdb.set_trace()
    
if __name__ == '__main__':
    main()
