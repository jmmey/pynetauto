#!/usr/bin/env python3

import os
import pyeapi
import yaml
from getpass import getpass


username = os.getenv("PYNET_USER") if os.getenv("PYNET_USER") else input('Username: ') 
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass('Password: ')

with open('inventory.yml', 'r') as f:
    inventory = yaml.safe_load(f)

inventory = inventory['arista8']
inventory['username'] = username
inventory['password'] = password

connection = pyeapi.client.connect(**inventory)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
ip_entries = output[0]['result']['ipV4Neighbors']

print()
print('IPv4 Address | MAC Address')
print('-' * 28)

for i in ip_entries:
    print(f"{i['address']} | {i['hwAddress']}") 

print()
