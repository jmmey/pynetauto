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
bgp_sec = bgp_obj.find_objects_w_child(parentspec=r'^router bgp', childspec=r'\s+neighbor\s+\d+')

bgp_peers = []

for line in bgp_sec:
    
