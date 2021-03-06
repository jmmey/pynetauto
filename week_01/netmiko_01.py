#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

my_user = input('Username: ')
my_pass = getpass('Password: ')

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": my_user,
    "password": my_pass
    }

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": my_user,
    "password": my_pass
    }

cisco_devices = [cisco3, cisco4]

for device in cisco_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief")
    # print(f'------{device}------\n')
    print(output + '\n')
    net_connect.disconnect()
