#!/usr/bin/env python3

import yaml
from pathlib import Path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = str(Path.home())
inventory_data = '/.netmiko.yml'

with open(home_dir + inventory_data, 'r') as f:
    inv_data = yaml.load(f)

cisco4 = inv_data['cisco4']

net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command('show run')
net_connect.disconnect()

run_obj = CiscoConfParse(output.splitlines())
interfaces = run_obj.find_objects_w_child(parentspec=r'^interface', childspec=r'^\s+ip address\s\d+')

for int in interfaces:
    print()
    print(f'Interface Line: {int.text}')
    ip_addr = int.re_search_children(r'address\s+\d+')
    ip_addr = ip_addr[0].text
    print(f'IP Address Line: {ip_addr}')
    print()
