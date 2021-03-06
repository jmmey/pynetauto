#!/usr/bin/env python3

import yaml
from pathlib import Path
from netmiko import ConnectHandler

home_dir = str(Path.home())
inventory_data = '/.netmiko.yml'

with open(home_dir + inventory_data, 'r') as f:
    inv_data = yaml.load(f)

cisco3 = inv_data['cisco3']

net_connect = ConnectHandler(**cisco3)

print(net_connect.find_prompt())
net_connect.disconnect()
