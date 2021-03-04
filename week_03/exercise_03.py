#!/usr/bin/env python3

import json
from pprint import pprint

JSON_FILE = 'napalm_data.json'
with open(JSON_FILE, 'r') as f:
    nxos_data = json.load(f)

ipv4_data = []
ipv6_data = []

for intf, ipaddr_dict in nxos_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict['prefix_length']
            if ipv4_or_ipv6 == 'ipv4':
                ipv4_data.append(f'{ip_addr}/{prefix_length}')
            elif ipv4_or_ipv6 == 'ipv6':
                ipv6_data.append(f'{ip_addr}/{prefix_length}')

print(f'\n IPv4 Addresses: {ipv4_data}')
print()
print(f'\n IPv6 Addresses: {ipv6_data}')
