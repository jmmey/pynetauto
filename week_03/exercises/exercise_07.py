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

xr_conf = xr_conf.splitlines()
parse_conf = CiscoConfParse(xr_conf)
bgp_sec = parse_conf.find_objects_w_child(
    parentspec=r'^router bgp', childspec=r'\s+neighbor\s+\d+'
)

bgp_sec = bgp_sec[0]
bgp_nei = bgp_sec.re_search_children(r'neighbor')

bgp_peers = []

for peer in bgp_nei:
    print(peer.text)
    break
