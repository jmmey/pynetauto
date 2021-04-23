#!/usr/bin/env python3

import os
import pyeapi
from getpass import getpass


username = os.getenv("PYNET_USER") if os.getenv("PYNET_USER") else input('Username: ') 
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass('Password: ')


connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username=username,
    password=password,
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
ip_entries = output[0]['result']['ipV4Neighbors']

print('IPv4 Address | MAC Address')
print('-' * 28)

for i in ip_entries:
    print(f"{i['address']} | {i['hwAddress']}") 
