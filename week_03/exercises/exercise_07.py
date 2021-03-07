#!/usr/bin/env python3

import yaml
from pathlib import Path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = str(Path.home())
inventory_data = '/.netmiko.yml'

xr_conf = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

parse_conf = CiscoConfParse(xr_conf.splitlines())
neighbors = parse_conf.find_objects_w_parents(
    parentspec=r'router bgp', childspec=r'neighbor'
)

bgp_peers = []

for neighbor in neighbors:
    _, ip_addr = neighbor.text.split()
    for as_num in neighbor.children:
        if 'remote-as' in as_num.text:
            _, as_number = as_num.text.split()
    bgp_peers.append((ip_addr, as_number))

print()
print('BGP Peers:')
print(bgp_peers)
print()
