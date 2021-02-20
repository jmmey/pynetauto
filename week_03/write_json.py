import json

my_data = {
    'device_type': 'cisco_ios',
    'ip_addr': '1.1.1.1',
    'username': 'admin',
    'password': 'foo'
}

some_list = list(range(10))
my_data['some_list'] = some_list
my_data['null_value'] = None
my_data['a_bool'] = False

filename = 'output.json'
with open(filename, 'wt') as f:
    json.dump(my_data, f, indent=4)

# Print to stdout as Python representation
print('PYTHON')
print('#' * 10)
print(my_data)
print()
# Print to stdout as JSON representation
print('JSON')
print('#' * 10)
print(json.dumps(my_data))
