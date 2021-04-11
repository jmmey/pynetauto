from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

intf_vars = {
    'nxos1_intf': 'Ethernet1/1',
    'nxos1_ip': '10.1.100.1',
    'nxos1_mask': '24',
    'nxos2_intf': 'Ethernet1/1',
    'nxos2_ip': '10.1.100.2',
    'nxos2_mask': '24',

}

template_file = 'nxos_config.j2'
template = env.get_template(template_file)
output = template.render(**intf_vars)
print()
print(output)
print()
