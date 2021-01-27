#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

my_user = input('Username: ') 
my_pass = getpass()

# Device Dictionaries
cisco3 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': my_user, 
    'password': my_pass
    }

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': my_user,
    'password': my_pass
    }

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': my_user,
    'password': my_pass
    }


net_connect = ConnectHandler(**nxos1)

output = net_connect.find_prompt()
print(output) 
