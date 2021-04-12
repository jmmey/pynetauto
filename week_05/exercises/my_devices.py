import os
from getpass import getpass

username = os.getenv("PYNET_USER") if os.getenv("PYNET_USER") else input('Username: ') 
password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass('Password: ')

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.ip',
    'username': username,
    'password': password
}

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.ip',
    'username': username,
    'password': password
}
