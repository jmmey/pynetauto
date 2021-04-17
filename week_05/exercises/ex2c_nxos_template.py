import time
import re

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
import my_devices import nxos1, nxos2

if __name__ == '__main__':
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader('./templates/exercise2')
    
    nxos1_vars = {
        'device_name': 'nxos1',
        'intf': 'Ethernet1/4',
        'intf_ip': '10.1.100.1',
        'intf_mask': '24',
        'bgp_neighbor_ip': '10.1.100.2',
        'bgp_as': '22',
        'remote_as': '22'
    }
    
    nxos2_vars = {
        'device_name': 'nxos2',
        'intf': 'Ethernet1/4',
        'intf_ip': '10.1.100.2',
        'intf_mask': '24',
        'bgp_neighbor_ip': '10.1.100.1',
        'bgp_as': '22',
        'remote_as': '22'
    }
    
    # Add Jinja2 vars to the Netmiko dictionary so if/then isn't needed
    nxos1['j2_vars'] = nxos1_vars 
    nxos2['j2_vars'] = nxos2_vars 

    print()
    for device in (nxos1, nxos2): 
        # Create a copy so the dictionary can be modified
        tmp_device = device.copy()
        j2_vars = temp_device.pop('j2_vars') 
        # Define the jina2 template file and create template obj
        template_file = 'nxos_config.j2'
        template = env.get_template(template_file)
        cfg = template.render(**j2_vars)
        # Print out some lines so the user knows what is happening
        device_name = temp_device['j2_vars']['device_name']
        print(f' {device_name}'.center(80, '#'))
        print(f'\n>>> Template ouput {device_name}')
        print(cfg)
         
