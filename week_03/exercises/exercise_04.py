#!/usr/bin/env python3

import json
from pprint import pprint

ARP = 'arista_arp.json'

with open(ARP, 'r') as f:
    arp_json = json.load(f)

arp_data = {}
arp_json = arp_json['ipV4Neighbors']

for i in arp_json:
    ip_addr = i['address']
    mac_addr = i['hwAddress']
    arp_data[ip_addr] = mac_addr

print()
pprint(arp_data)
print()
