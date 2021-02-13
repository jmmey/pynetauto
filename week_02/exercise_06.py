import time
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'secret': password,
    'device_type': 'cisco_ios',
    'session_log': 'my_output.txt'
}

net_connect = ConnectHandler(**device)

print(net_connect.find_prompt())
print()

net_connect.config_mode()
print(net_connect.find_prompt())
print()

net_connect.exit_config_mode()
print(net_connect.find_prompt())
print()

net_connect.write_channel('disable\n')
# print(net_connect.find_prompt())
print()

time.sleep(2)
read = net_connect.read_channel()
print(read)
print()

net_connect.enable()
print(net_connect.find_prompt())
print()

net_connect.disconnect()
