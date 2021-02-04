#!/usr/bin/env python3

import os
from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# my_user = input('Username: ') 
my_user = 'pyclass'
# my_pass = getpass()
my_pass = os.getenv('PYNET_PASSWORD') if os.getenv('PYNET_PASSWORD') else getpass()

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

command = 'ping'

output = net_connect.send_command(command, expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('8.8.8.8', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r':', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'#', strip_prompt=False, strip_command=False)

# output = net_connect.send_command_timing('ping')
# output += net_connect.send_command_timing('\n')
# output += net_connect.send_command_timing('8.8.8.8')
# output += net_connect.send_command_timing('\n')
# output += net_connect.send_command_timing('\n')
# output += net_connect.send_command_timing('\n')
# output += net_connect.send_command_timing('\n')
# output += net_connect.send_command_timing('\n')

net_connect.disconnect()

print()
print(output)
print()

