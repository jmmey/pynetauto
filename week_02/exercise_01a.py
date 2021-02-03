#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

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


net_connect = ConnectHandler(**cisco4)

# command = 'delete flash:/john_test1.txt'

# net_connect.send_command(command, expect_string=r'Delete filename')
# net_connect.send_command('\n', expect_string=r'confirm')
# net_connect.send_command('y', expect_string=r'#')

output = net_connect.send_command_timing('ping')
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('8.8.8.8')
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('\n')

pprint(output)

# Graceful Disconnect
net_connect.disconnect()
