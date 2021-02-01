#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

my_user = input('Username: ') 
my_pass = getpass()

# Device Dictionaries
cisco3 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': my_user, 
    'password': my_pass,
    'session_log': 'cisco3_session.txt'
    }

cisco4 = {
    'device_type': 'cisco_ios',
    'host': 'cisco4.lasthop.io',
    'username': my_user, 
    'password': my_pass
    }

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': my_user,
    'password': my_pass
    }

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': my_user,
    'password': my_pass
    }

# Netmiko Connections
net_connect = ConnectHandler(**cisco3)

# cfg = 'logging buffered 10001'

# cfg = ['logging buffered 10002', 
#    'clock timezone PDT -7', 
#   'ip ftp source-interface gigabitEthernet 0/0/0'
#]


# output = net_connect.send_config_set(cfg)

output = net_connect.send_config_from_file(config_file='config_file.txt')
print(output)

# Graceful Disconnect
net_connect.disconnect()
