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

net_connect = ConnectHandler(**cisco4)

output1 = net_connect.send_command('show version', use_textfsm=True)
print(output1)

print('\n\n')

output2 = net_connect.send_command('show lldp neighbors', use_textfsm=True)
print(output2)

print()
print('*' * 20)

for nei in output2:
    print('Neighbor ' + str(nei['neighbor']) + ' remote port is ' + str(nei['neighbor_interface']))
    break

print('*' * 20)
print()

net_connect.disconnect()
