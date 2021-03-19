from jinja2 import Template

my_template = """
    This is some template with {{ my_var }}.
    It needs to be filled out using variable
    data.

"""

var_dict = {
    'my_var': 'Jinja2'
}

j2_obj = Template(my_template)
rendered_text = j2_obj.render(**var_dict)
print(rendered_text)
