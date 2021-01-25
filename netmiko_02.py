#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

my_user = input('Username: ')
my_pass1 = getpass('Please enter your password: ')
my_pass2 = getpass('Please confirm your password: ')
my_pass = my_pass2

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

# Validate passwords match
while my_pass1 != my_pass2:
    try_count = 1
    print("It appears you're passwords do not match please reenter your password\n")
    if try_count == 3:
        break
    else:      
        my_pass1 = getpass('Please enter your password: ')
        my_pass2 = getpass('Please confirm your password: ')
        try_count += 1


if my_pass1 == my_pass2:
    net_connect = ConnectHandler(**cisco3)
    output = net_connect.send_command('show ip int bri', use_textfsm=True)
    print('\n')
    print(output) 
    print('\n')
    net_connect.disconnect()
else:
    print('\nPasswords do not match\n')
