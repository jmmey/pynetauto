import yaml

my_data = {
    'device_type': 'cisco_ios',
    'ip_addr': '1.1.1.1',
    'username': 'admin',
    'password': 'foo'
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_valuse'] = None
my_data['a_bool'] = False

filename = 'output.yml'
with open(filename, 'wt') as f:
    # Change "default_flow_style=False" for expanded format ouput 
    yaml.dump(my_data, f, default_flow_style=False)
