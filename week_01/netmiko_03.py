#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

my_user = input('Username: ')
my_pass = getpass('Please enter your password: ')

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

devices = [cisco3, cisco4]

net_connect = ConnectHandler(**cisco3)
print(net_connect.find_prompt())
