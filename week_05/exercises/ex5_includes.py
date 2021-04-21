from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates/exercise5')

template_file = 'ios_template.j2'
template = env.get_template(template_file)
#output = template.render(**j2_vars)
output = template.render()
print()
print(output)
print()
