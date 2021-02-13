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
    'password': my_pass
    }

nxos = [nxos1, nxos2]

for nx in nxos:
    net_connect = ConnectHandler(**nx)
    output = net_connect.send_config_from_file(config_file='nx_vlans.txt')
    print(output)
    print()
    save_out = net_connect.save_config()
    print(save_out)
    net_connect.disconnect()

