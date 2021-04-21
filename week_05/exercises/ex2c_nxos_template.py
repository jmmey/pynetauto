#!/usr/bin/env python3

import time
import re

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

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
        j2_vars = tmp_device.pop('j2_vars') 
        # Define the jina2 template file and create template obj
        template_file = 'nxos_config.j2'
        template = env.get_template(template_file)
        cfg = template.render(**j2_vars)
        # Print out some lines so the user knows what is happening
        device_name = device['j2_vars']['device_name']
        print(f' {device_name} '.center(60, '#'))
        print(f'\n>>> Template ouput {device_name}\n')
        print(cfg)
        # Create list of config lines
        cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]
       
        # Establish Netmiko connection
        net_connect = ConnectHandler(**tmp_device)
        # Store connection for later 
        device['ssh_conn'] = net_connect
        # Configure device
        print(f'>>> Configuring {device_name}')
        output = net_connect.send_config_set(cfg_lines)
        print(output)
        print('\n\n')
       
    # Delay for BGP state to establish
    sleep_time = 15
    print(f'Sleeping for {sleep_time} seconds')
    time.sleep(sleep_time)

    print('\n\n')
    print('>>> Testing ping and BGP')
    for device in (nxos1,):
        net_connect = device['ssh_conn']
        remote_ip = device['j2_vars']['bgp_neighbor_ip']

        # Test ping
        output = net_connect.send_command(f'ping {remote_ip}')
        print(output)
        if '64 bytes from' not in output:
            print('\nPing failed!')
        print('\n\n') 
        
        # Test BGP
        bgp_verify = f'show ip bgp summary | include {remote_ip}'
        output = net_connect.send_command(bgp_verify)
        # Retreive the State/PfxRcd field which is the last field
        match = re.search(r"\s+(\S+)\s*$", output)
        prefix_received = match.group(1)
        try:
            # If int, the BGP session reached established state
            int(prefix_received)
            print(
                f'BGP reached the established stated. Prefixes recieved {prefix_received}'
            )
        except ValueError:
            print('BGP failed to reach the established state')

    # All done - disconnect on both devices
    for device in (nxos1, nxos2):
        net_connect = device['ssh_conn']
        net_connect.disconnect()

    print('\n\n')
