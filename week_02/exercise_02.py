#!/usr/bin/env python3

import os
from datetime import datetime
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

my_user = 'pyclass'
my_pass = os.getenv('PYNET_PASSWORD') if os.getenv('PYNET_PASSWORD') else getpass()

# Device Dictionaries
cisco3 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': my_user, 
    'password': my_pass,
    'session_log': 'cisco3_session.txt'
    }

cisco4 = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': my_user, 
    'password': my_pass,
    'session_log': 'cisco4_session.txt'
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
    'password': my_pass,
    'global_delay_factor': 2
    }

net_connect = ConnectHandler(**nxos2)

print(datetime.now())
print('-' * 35)

output = net_connect.send_command('show lldp neighbors detail')

print(datetime.now())
print('-' * 35)


print(datetime.now())
print('-' * 35)

output2 = net_connect.send_command(
    'show lldp neighbors detail',
    delay_factor=8
)

print(datetime.now())
print('-' * 35)

net_connect.disconnect()
