#!/usr/bin/env python3

import yaml
from pprint import pprint


cisco3 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io'
    }

cisco4 = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io'
    }

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io'
    }

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io'
    }

lab_devices = [cisco3, cisco4, nxos1, nxos2]

for device in lab_devices:
    device['Username'] = 'admin'
    device['Password'] = 'cisco123'


print()
pprint(lab_devices)
print()

filename = 'output.yml'

with open(filename, 'w') as f:
    yaml.dump(lab_devices, f, default_flow_style=False)
