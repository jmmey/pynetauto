#!/usr/bin/env python3

from netmiko import ConnectHandler, file_transfer
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

source_file = 'john_testy.txt'
dest_file = 'john_testy.txt'
direction = 'put'
file_system = 'flash:'

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**cisco3)
# Make the file transfer happen
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True
)

print(transfer_dict)

ssh_conn.disconnect()
