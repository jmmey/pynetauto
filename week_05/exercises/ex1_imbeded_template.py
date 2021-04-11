from jinja2 import Template


bgp_template = """
    router bgp {{ as }}
      neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
        update-source loopback99
        ebgp-multihop 2
        address-family ipv4 unicast
      neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
        address-family ipv4 unicast
"""

template_vars = {
    'as': '10',
    'peer1_ip': '10.1.20.2', 
    'peer1_as': '20',
    'peer2_ip': '10.1.30.2',
    'peer2_as': '30'
}

j2_obj = Template(bgp_template)
output = j2_obj.render(**template_vars)
print()
print(output) 
print()
